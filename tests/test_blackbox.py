#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# name:   test_blackbox.py
# author: nbehrnd@yahoo.com
# date:   [2021-02-04 Tue]
# edit:   [2025-07-21 Mon]
#
"""tests for saturate_murcko_scaffolds.py

This script checks results by script `saturate_murcko_scaffolds.py` with
pytest.  The coverage is incomplete, already because checks currently don't
import individual functions, i.e. only black box-tests (`pytest -k blackbox`)
are run.

There are additional SMILES in sub folder `demo` which serve for a more
extended demonstration of the script's working rather than (pytest based)
checks if the script works correctly.
"""

import os
import subprocess as sub

import pytest

SCRIPT = os.path.join(
    "src", "app", "xfpm.py"
)


@pytest.mark.blackbox
def test_program_exists():
    """Check for the presence of saturate_murcko_scaffolds.py."""

    assert os.path.isfile(SCRIPT)

# END
