#!/usr/bin/env python3

"""
name     : xfpm_c.py
source   : https://github.com/Beliavsky/Fortran-packages-list
author   : Beliavsky, Norwid Behrnd
license  : MIT
last edit: [2024-05-10 Fri]
purpose  : report projects that can be built with the Fortran Package Manager
"""

import argparse
import datetime
import os
import re
import sys

from multiprocessing import Pool
from time import perf_counter

from github import Github

os.environ["PYTHONIOENCODING"] = "utf-8"

# Access the GitHub token from environment variable
github_token = os.environ.get("GH_TOKEN")
# github_token = "ghp_..."  # alternative: enter the token

# Initialize PyGithub with the token
g = ""
try:
    g = Github(github_token)
except Exception:
    print("The github_token is not accessible to the script, exit.")
    sys.exit()


def get_args():
    """get the command-line arguments"""

    parser = argparse.ArgumentParser(
        description="""List projects, organized by topic, that can be built with
        the Fortran Package Manager.  For this, file README.md of project
        'Directory of Fortran codes on GitHub' curated by Beliavsky et al. (see
        https://github.com/Beliavsky/Fortran-code-on-GitHub) is processed as
        input for this script.  If used outside an automated GitHub action,
        the API key as to be provided manually.""",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file",
        help="said README.md file",
        metavar="FILE",
        type=argparse.FileType("rt", encoding="utf-8"),
        default=None,
    )

    parser.add_argument(
        "-d",
        "--debug",
        help="activate the scripts internal debugger",
        action="store_true",
    )

    parser.add_argument(
        "-t",
        "--test",
        help="constrain a test run to 300 lines output",
        action="store_true",
    )

    return parser.parse_args()


def check_setup(g, test=False):
    """check the connection to the GitHub API"""
    if test:

        # Check if login was successful
        if g.get_user():
            print("Login to GitHub API successful.")
        else:
            print("Failed to login to GitHub API.")

        # Display rate limit information
        rate_limit = g.get_rate_limit()
        print("GitHub API rate limit:")
        print(f"Limit: {rate_limit.core.limit}")
        print(f"Remaining: {rate_limit.core.remaining}")
        print(f"Reset Time: {rate_limit.core.reset}")

        # For a typical project in question
        repo_owner = "vmagnin"
        repo_name = "ForSudoku"
        repo = g.get_repo(f"{repo_owner}/{repo_name}")
        principal_branch = repo.default_branch
        print(f"The principal branch of {repo_name} is: {principal_branch}")

        # Check if the principal branch has a fpm.toml file
        branch = repo.get_branch(principal_branch)
        tree = repo.get_git_tree(sha=branch.commit.sha, recursive=True)
        readme_exists = any(entry.path == "fpm.toml" for entry in tree.tree)
        if readme_exists:
            print("fpm.toml exists in the principal branch.")
        else:
            print("fpm.toml does not exist in the principal branch.")


def file_reader(infile="", debug=False, test=False):
    """iterate on the input file till reaching the threshold"""

    max_lines = 300 if test else 10**6  # allow a constrained test run
    raw_data = [line.strip() for line in infile]
    array_prior_test_condition = len(raw_data)

    if test:
        raw_data = raw_data[:max_lines]
    array_after_test_condition = len(raw_data)

    if debug:
        print("lines in raw_data to process:")
        print(f"array_prior_test_condition: {array_prior_test_condition}")
        print(f"array_after_test_condition: {array_after_test_condition}")

        pattern = re.compile("^\[")  # signature of project lines in raw_data
        projects = list(filter(pattern.match, raw_data))
        print(f"up to {len(projects)} projects to consider\n")

    return raw_data


def extract_owner_and_repo(text, debug=False):
    """extract the owner and repository from address of project line"""
    # text in parentheses after first after first set of brackets
    match = re.search(r"\[.*?\]\((.*?)\)", text)
    # Extract the match, if it exists
    url_address = match.group(1) if match else None

    url_address = url_address[:-1] if url_address.endswith("/") else url_address
    repo_owner, repo_name = url_address.split("/")[-2:]

    if debug:
        print("read by extract_owner_and_repo:")
        print(f"url_address: {url_address}")
        print(f"repo_owner: {repo_owner}")
        print(f"repo_name: {repo_name}\n")

    return repo_owner, repo_name


def check_project(entry, debug=False):
    """Check if a project contains a 'fpm.toml' file"""
    repo_owner, repo_name = extract_owner_and_repo(entry, debug)
    try:
        repo = g.get_repo(f'{repo_owner}/{repo_name}')
        principal_branch = repo.default_branch
        search_toml = repo.get_contents(path="./fpm.toml", ref=principal_branch)
        return entry if search_toml else None
    except Exception:
        if debug:
            print(f"no check for {entry}")
        return None


def report_projects(intermediate_register, previous_section_title, debug=False):
    """report sections about projects if there are projects"""
    if debug:
        print(f"{len(intermediate_register)} entries to check")

    pool = Pool()  # Create a Pool of processes
    results = pool.map(check_project, intermediate_register)  # Distribute tasks across processes
    pool.close()
    pool.join()

    affirmative_tests = [result for result in results if result]

    if affirmative_tests:
        affirmative_tests = sorted(affirmative_tests, key=str.casefold)
        print("".join([previous_section_title, "\n"]))
        for entry in affirmative_tests:
            print("".join([entry, "\n"]))


def triage_lines(raw_data, debug=False):
    """identify lines with addresses to check on GitHub for a fpm.toml file"""
    previous_section_title = ""
    intermediate_register = []

    for i, line in enumerate(raw_data):
        # lines with less work ahead:
        if line.startswith("## Fortran code on GitHub"):
            print("".join([line, "\n"]))
        if line.startswith("* ["):
            print("".join([line, "\n"]))

        # lines with more work ahead
        # projects eventually to visit on GitHub
        if line.startswith("["):
            intermediate_register.append(line)

        # sections like "Art and Music", "Astronomy and Astrophysics", etc.
        if line.startswith("##"):
            if line.startswith("## Fortran code on GitHub") is False:
                if intermediate_register:
                    report_projects(intermediate_register, previous_section_title, debug)
                    intermediate_register = []
                previous_section_title = line

        # Equally report a section if a line about a project happens to be the
        # ultimate line of the raw_data read:
        if i == len(raw_data) - 1:
            report_projects(intermediate_register, previous_section_title, debug)


def main():
    """join the functionalities"""

    args = get_args()
    infile = args.file
    debugger_level = args.debug
    test_level = args.test

    check_setup(g, args.test)

    start = perf_counter()
    raw_data = file_reader(infile, debugger_level, test_level)
    triage_lines(raw_data, debugger_level)
    end = perf_counter()

    print(f"last update: {datetime.date.today()}")
    print(f"time elapsed (s): {(end - start):.2f}")


if __name__ == "__main__":
    main()
