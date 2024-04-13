## Fortran code on GitHub -- also see [fortran-lang package index](https://fortran-lang.org/packages/)

* [Art and Music](#art-and-music)

* [Astronomy and Astrophysics](#astronomy-and-astrophysics)

* [Benchmarks](#benchmarks)

* [Biology and Medicine](#biology-and-medicine)

* [Climate and Weather](#climate-and-weather)

* [Code Tools](#code-tools)

* [Compiler Tests](#compiler-tests)

* [Computational Chemistry](#computational-chemistry)

* [Computational Fluid Dynamics](#computational-fluid-dynamics)

* [Containers and Generic Programming](#containers-and-generic-programming)

* [Cryptography](#cryptography)

* [Databases](#databases)

* [Dates and Times](#dates-and-times)

* [Earth Science](#earth-science)

* [Economics](#economics)

* [Engineering](#engineering)

* [Error Handling](#error-handling)

* [Expression Parsers](#expression-parsers)

* [Fast Fourier Transform](#fast-fourier-transform)

* [File I/O](#file-io)

* [Finite Elements](#finite-elements)

* [Fortran Books and Tutorials](#fortran-books-and-tutorials)

* [Games and Puzzles](#games-and-puzzles)

* [Graphics, Plotting and User Interfaces](#graphics-plotting-and-user-interfaces)

* [General Purpose](#general-purpose)

* [Interoperability](#interoperability)

* [Interpolation](#interpolation)

* [Linear Algebra](#linear-algebra)

* [Materials Science](#materials-science)

* [Molecular Dynamics](#molecular-dynamics)

* [Mesh Generation](#mesh-generation)

* [Neural Networks and Machine Learning](#neural-networks-and-machine-learning)

* [Numerical](#numerical)

* [Numerical Integration (Quadrature)](#numerical-integration-quadrature)

* [Ordinary Differential Equations](#ordinary-differential-equations)

* [Optimization](#optimization)

* [Parallel Programming](#parallel-programming)

* [Partial Differential Equations](#partial-differential-equations)

* [Particle Physics](#particle-physics)

* [Physics](#physics)

* [Plasma Physics](#plasma-physics)

* [Random Number Generation](#random-number-generation)

* [Reactor Physics](#reactor-physics)

* [Regular Expressions](#regular-expressions)

* [Quantum Chemistry and Electronic Structure](#Quantum-Chemistry-and-Electronic-Structure)

* [Sorting](#sorting)

* [Statistics](#Statistics)

* [Strings](#strings)

* [Time Series](#time-series)

* [Unclassified](#unclassified)

* [Unit Testing](#unit-testing)

* [Web Programming](#web-programming)

* [XML](#xml)

## Art and Music

[formidi](https://github.com/vmagnin/formidi): small Fortran MIDI sequencer for composing music and exploring algorithmic music, by Vincent Magnin

[forsynth](https://github.com/vmagnin/forsynth): small Fortran synthesizer to explore sound synthesis, sound effects, electronic music, algorithmic music, etc, by Vincent Magnin

[TapTempo Fortran](https://github.com/vmagnin/TapTempo-Fortran): command line taptempo written in modern Fortran, by Vincent Magnin. Listen to a song and hit enter key with style and you'll get the corresponding number of beats per minute (BPM). 

## Astronomy and Astrophysics

[aquila astrophotography package](https://github.com/gronki/aquila): small LRGB astrophotography reduction and processing package, by Dominik Gronkiewicz. The package consists of the programs aqstack for stacking and reduction of monochromatic CCD images and aqlrgb for compositing images from many filters into one color picture.

[astro-fortran](https://github.com/jacobwilliams/astro-fortran): modern Fortran implementations of standard models used in fundamental astronomy, by Jacob Williams. It is a refactoring of [IAU SOFA](https://github.com/jacobwilliams/IAU_SOFA).

[Fortran-Astrodynamics-Toolkit](https://github.com/jacobwilliams/Fortran-Astrodynamics-Toolkit): aims to be a comprehensive library, written in modern Fortran (Fortran 2003/2008), of all the standard orbital mechanics algorithms, by Jacob Williams

[halo](https://github.com/jacobwilliams/halo): orbit solver that can be used to generate long-duration Earth-Moon halo orbits in the ephemeris model. Reference: J. Williams et al., [Targeting Cislunar Near Rectilinear Halo Orbits for Human Space Exploration](https://www.researchgate.net/publication/322526659_Targeting_Cislunar_Near_Rectilinear_Halo_Orbits_for_Human_Space_Exploration), 27th AAS/AIAA Space Flight Mechanics Meeting, 2017

[img2nc](https://github.com/ShinobuAmasaki/img2nc): converts planetary Digital Elevation Model (DEM) data into NetCDF, allowing one to draw a topographic map of the Moon,

[Naval Observatory Vector Astrometry Software (NOVAS)](https://github.com/jacobwilliams/NOVAS): integrated package of routines for computing various commonly needed quantities in positional astronomy, refactored by Jacob Williams. The package can provide, in one or two subroutine or function calls, the instantaneous coordinates of any star or planet in a variety of coordinate systems.

[radbelt](https://github.com/jacobwilliams/radbelt): AE-8/AP-8 Van Allen belt model, describing the differential or integral, omnidirectional fluxes of electrons (AE-8) and protons (AP-8) in the inner and outer radiation belts, by Jacob Williams

## Benchmarks

[ForBenchmark](https://github.com/gha3mi/forbenchmark): a Fortran library for benchmarking (with support for coarrays). There are [dot_product](https://github.com/gha3mi/forbenchmark/tree/main/benchmarks/dot) benchmark results, by Seyed Ali Ghasemi

## Biology and Medicine

[Motility Analysis of T-Cell Histories in Activation (MATCHA)](https://github.com/BerkeleyLab/matcha): designs virtual T cells that move like biological T cells, from  BerkeleyLab and Northern New Mexico College. The virtual T cells will match the speed and turning angle distributions of biological cells.

## Climate and Weather

[VenusPT-tables](https://github.com/Razumovskyy/VenusPT-tables): atmospheric absorption coefficient calculator: Utilizing [HITRAN](https://hitran.org/) and custom spectroscopy for Venus and Mars radiative transfer studies, by Mikhail Razumovskiy. Also [PrecisionSpec-Analyzer](https://github.com/Razumovskyy/PrecisionSpec-Analyzer), a high-precision tool for atmospheric absorption calculations over narrow spectral ranges, focusing on detailed spectroscopic analysis using HITRAN and HITEMP data with standard and custom line shapes for terrestrial atmospheric studies.

## Code Tools

[AD_dnSVM](https://github.com/lauvergn/AD_dnSVM): Fortran Automatic Differentiation tool using forward mode for scalars (S), Vectors (V) and Matrices (M), by David Lauvergnat. It has no limit in terms of the number of independent variables (this number is defined at runtime) and can compute up to third derivatives.

[Auto-Diff](https://github.com/zoziha/Auto-Diff): implementation in Modern Fortran of backward mode automatic differentiation, by zoziha

[Fortran Debug Utilities](https://github.com/plevold/fortran-debug-utils): collection of some utilities useful for debugging code, by Pål Levold

[fortran-git](https://github.com/interkosmos/fortran-git): Fortran 2008 ISO C binding interfaces to [libgit2](https://github.com/libgit2/libgit2), by interkosmos

[forwarddiff](https://github.com/Nicholaswogan/forwarddiff): allows for the computation for derivatives, gradients and Jacobians of Fortran subroutines or functions using forward mode automatic differentiation (AD), by Nicholas Wogan, inspired by [DNAD](https://github.com/joddlehod/dnad) and [ForwardDiff.jl](https://github.com/JuliaDiff/ForwardDiff.jl)

[prep](https://github.com/urbanjost/prep): streamlined pre-processor primarily designed for use with Fortran, by urbanjost. It does not support procedural macros but does support variable substitution and reusable free-format text blocks which allows for basic templating as well as easy construction of multi-line CHARACTER variables; and is quite capable of supporting traditional conditional compilation.

[progress-bar](https://github.com/zoziha/progress-bar): simple progress bar module that is typically used to display the time integration process, by zoziha

[symengine.f90](https://github.com/symengine/symengine.f90): Fortran wrappers by Rikard Nordgren and Ondřej Čertík of SymEngine, a fast symbolic manipulation library, written in C++

[to_f90](https://github.com/jbdv-no/to_f90): Alan Miller's tool for converting Fortran 77 code to free-form Fortran 90 code, from jbdv-no

[version-f](https://github.com/minhqdao/version-f): implementation of [Semantic Versioning 2.0.0](https://semver.org/) by Minh Dao that aims to be a user-friendly tool for handling versions in Fortran projects.

## Compiler Tests

## Computational Chemistry

[ciaaw](https://github.com/MilanSkocic/ciaaw): library providing the standard and abridged atomic weights, the isotopic abundance and the isotopes' standard atomic weights, by Milan Skocic. It also provides a API for the C language.

[ecx](https://github.com/MilanSkocic/ecx): library providing formulas for electrochemistry with a C API, by Milan Skocic

[fenvelopes](https://github.com/ipqa-research/fenvelopes): calculate phases boundaries of multicomponent systems using Equations of State, currently supporting PT envelopes and PX envelopes with partial three-phase-behaviour, by Federico E. Benelli

[forsus](https://github.com/ipqa-research/forsus): provides a simple API to read json files containing pure component information, which can be used in other projects, by José Antonio Scilipoti

[GWMlib](https://github.com/dmr-dj/GWMlib): Generic Water isotope Modelling Library, by Didier M. Roche

[International Association for the Properties of Water and Steam (iapws)](https://github.com/MilanSkocic/iapws): library providing the formulas for computing light and heavy water properties, by Milan Skocic, with interfaces to C and (in [pyiapws](https://github.com/MilanSkocic/pyiapws)) Python

[kanon](https://github.com/aslozada/kanon): program to compute chirality indices and assess molecular symmetry, by Asdrubal Lozada-Blanco

[Modular computation tool chain library (mctc-lib)](https://github.com/grimme-lab/mctc-lib): common tool chain to use molecular structure data in various applications, from grimme-lab. This library provides a unified way to perform operations on molecular structure data, like reading and writing to common geometry file formats.

[mstore](https://github.com/grimme-lab/mstore): molecular structure store for testing, from grimme-lab

[numsa](https://github.com/grimme-lab/numsa): solvent accessible surface area calculation, from grimme-lab

[YA_EoS](https://github.com/fedebenelli/yaeos): thermodynamic equations of state library with both automatic and analytical derivation capabilities, by Federico E. Benelli

## Containers and Generic Programming

[any](https://github.com/degawa/any): user-defined type for mimicking procedures that can return different types, by Tomohiro Degawa

[array_range](https://github.com/degawa/array_range): provides user-defined types array_range{1|2|3}d_type to improve the manipulation of bounds of Fortran arrays, by Tomohiro Degawa

[collections](https://github.com/jchristopherson/collections): set of types supporting collections in Fortran, by Jason Christopherson. Currently, the library contains a generic, dynamically sizable list and a generic linked-list type.

[enhanced-allocatables](https://github.com/PierUgit/enhanced-allocatables): proposal to extend allocatable arrays to be dynamically reallocatable/resizable, with an implementation that calls C++, by PierUgit

[Fortran_competitive_library](https://github.com/osada-yum/Fortran_competitive_library): library for solving [AtCoder](https://atcoder.jp/) problems, implementing a binary indexed tree, hash table, linked list, tuples, and merge and selection sort

[enumul](https://github.com/degawa/enumul): incomplete typed enumerator emulator for Fortran, by Tomohiro Degawa

[fhash](https://github.com/LKedward/fhash): hash table with support for generic keys and values, by Laurence Kedward

[flinkedlist](https://github.com/sakamoti/flinkedlist): object-oriented library providing an simple linked list, with the ability to sort elements with a user-defined function, apply a user-defined function in each node, and a convenience method to aid print debugging by automatically displaying variables of built-in types and providing a dedicated display function for user-defined types, by Yuichiro Sakamoto

[flist](https://github.com/jacobwilliams/flist): modern Fortran linked lists using unlimited polymorphic derived types, by Jacob Williams

[fortranDF](https://github.com/jaiken17/fortranDF): data frame that can have columns of different types, by Joshua Aiken

[fortran_vector](https://github.com/Euler-37/fortran_vector): derived type for vector of integers, with procedures `init`, `append`, `size`, `pop`, `remove`, `delete`, `unique`, `sort`, `cut`, and `clear`, by Euler-37

[list](https://github.com/grofz/list): easy-to-use implementation of Python-like lists, with methods append(), clear(), copy(), count(), extend(), insert(), pop(), remove(), reverse(), sort(), by Zdenek Grof

[maps](https://github.com/degawa/maps): wrapper by Tomohiro Degawa for [stdlib_hashmaps](https://stdlib.fortran-lang.org/page/specs/stdlib_hashmaps.html) that simplifies adding a key-value mapping and getting the value mapped to a key

[Multidimensional Array Containers (MAC)](https://github.com/irukoa/MAC): library to create and manipulate arrays of any rank, by Álvaro R. Puente-Uriona, meant to serve as a building block for codes that expand on "rank-agnostic" programming

[repot](https://github.com/degawa/repot): abstract data types designed for the repository pattern for reading configuration files in Fortran, by Tomohiro Degawa. The repository pattern is a design pattern that makes an object persistent in a repository and reconstructs it from the repository. [Repot_examples](https://github.com/degawa/repot_examples) has practical usage examples.

[rearrayfx](https://github.com/aradi/rearrayfx): demonstrates a reallocatable array structure with overprovision at re-allocation in order to decrease the number of reallocations, by Bálint Aradi

[slinked-list](https://github.com/zoziha/slinked-list): simple generic singly linked list module for in-memory storage of small amounts of data, by zoziha

[smart-pointers](https://github.com/sourceryinstitute/smart-pointers): tracks references to program resources and automates the freeing of those resources if and only if the reference count drops to zero, by Damian Rouson et al. Most commonly, the reference is a pointer and the resource is memory.

## Computational Fluid Dynamics

[interpolate-fields](https://github.com/p-costa/interpolate-fields): interpolates DNS data to a new grid using linear interpolation, by Pedro Costa. It can run and store the interpolated data in a massively-parallel setting using MPI I/O. For now, it assumes two regular Cartesian grids with the file format of CaNS.

[Navier_Stokes_Spectral_Method](https://github.com/Minard-Jules/Navier_Stokes_Spectral_Method): Navier Stokes simulation using the spectral method, visualized with [gtk-fortran](https://github.com/vmagnin/gtk-fortran), by Jules Minard

[Smoothed Particle Hydrodynamics（SPH)](https://github.com/zoziha/SPH): uses code from the book [Smooth Particle hydrodynamics - A Meshfree Particle Method](https://www.worldscientific.com/worldscibooks/10.1142/5340) as a starting point, by zoziha

## Cryptography

[sodium](https://github.com/freevryheid/sodium): Fortran bindings by Andre Smit for [libsodium](https://github.com/jedisct1/libsodium), a C library for encryption, decryption, signatures, password hashing, etc.

## Databases

[fortran-sqlite3](https://github.com/interkosmos/fortran-sqlite3): Fortran 2018 interface bindings to SQLite 3, by interkosmos

[fpq](https://github.com/freevryheid/fpq): modules with PostgreSQL (libpq) Fortran bindings, by Andre Smit

[libpq-fortran](https://github.com/ShinobuAmasaki/libpq-fortran): interface by ShinobuAmasaki to the PostgreSQL [libpq C Library](https://www.postgresql.org/docs/current/libpq.html)

[SQLite for Fortran (sqliteff)](https://github.com/everythingfunctional/sqliteff): thin wrapper around the SQLite library, by Brad Richardson. The sqliteff_* functions are effectively identical to the sqlite3_* functions that would be called from C, but with Fortran intrinsics and types.

## Dates and Times

[datetime](https://github.com/patti-favaron/datetime): library for simple, time-zone-independent date and time management, by Patrizia Favaron

[datetime-fortran](https://github.com/milancurcic/datetime-fortran): time and date manipulation facilities, by milancurcic

[m_time](https://github.com/urbanjost/M_time): displays dates in a variety of formats and performs basic date and time computation, by urbanjost

[time-f](https://github.com/0382/time-f): wraps time.h of the C standard library, by 0382

## Earth Science

[gravmod3d](https://github.com/ofmla/gravmod3d): 3D forward modeling of bodies discretized by rectangular prisms with parabolic density contrast, an implementation by Oscar Mojica of the three-dimensional gravity modeling with parabolic density contrast presented in the paper [3-D forward gravity modeling of basement interfaces above which the density contrast varies continuously with depth](https://www.sciencedirect.com/science/article/abs/pii/S0098300401000802) by V. Chakravarthi et al., Computers & Geosciences (2002)

[Maptran 3D](https://github.com/geospace-code/maptran3d): Modern Fortran 3D coordinate conversions for geospace ecef enu eci, from geospace-code.  Similar to Python PyMap3D and Matlab Matmap3d.

[PICO_Fortran](https://github.com/dmr-dj/PICO_Fortran): implementation by Didier M. Roche of the Potsdam Ice-shelf Cavity mOdel from the paper [Antarctic sub-shelf melt rates via PICO](https://tc.copernicus.org/articles/12/1969/2018/), by Ronja Reese et al., (2018).

## Economics

[econ-toolchain](https://github.com/renatomatz/econ-toolchain): general tools used for structural macroeconomic modeling, including codes for global optimization, I/O, Markov chains, finding roots, golden-section search, and unit testing, by Renato Zimmermann. 

## Engineering

[Deformation Monitoring Package (DMPACK)](https://github.com/dabamos/dmpack): package for sensor control and automated time series processing in geodesy and geotechnics, consisting of a library libdmpack and additional programs based on it which serve as a reference implementation of solutions to various problems in deformation monitoring, by Philipp Engel

## Error Handling

[assert](https://github.com/sourceryinstitute/assert): simple assertion utility taking advantage of the Fortran 2018 standard's introduction of variable stop codes and error termination inside pure procedures, by Damian Rouson

[erloff](https://github.com/everythingfunctional/erloff): errors and logging for Fortran, by Brad Richardson. The basic usage is that a procedure can have intent(out) message and/or error list arguments, or as a component of its return value.

[errstat](https://github.com/degawa/errstat): error status and message handling library for Modern Fortran, by Tomohiro Degawa. Also [fassert](https://github.com/degawa/fassert), a simple assertion library

[ferror](https://github.com/jchristopherson/ferror): library to assist with error handling in Fortran projects

[Fortran Error Handler](https://github.com/samharrison7/fortran-error-handler): universal and comprehensive solution for applications requiring functional and robust error handling, utilising the power of modern object-oriented Fortran, by Sam Harrison and KellerV

[Fortran Error Handling](https://github.com/SINTEF/fortran-error-handling): makes error handling easier by providing a type, error_t, to indicate if a procedure invocation has failed, from SINTEF. Errors can be handled gracefully and context can be added while returning up the call stack. It is also possible to programmatically identify and handle certain types or errors without terminating the application. It generate stacktraces along with any error when combined with the [Fortran Stacktrace](https://github.com/SINTEF/fortran-stacktrace) library, which enables generation of stacktraces for Fortran by wrapping the C++ library [backward-cpp](https://github.com/bombela/backward-cpp).

## Expression Parsers

[Fortran Equation Parser (feqparse)](https://github.com/FluidNumerics/feq-parse): equation parser Fortran class that is used to interpret and evaluate functions provided as strings, by Joe Schoonover 

[fortran_function_parser](https://github.com/jacobwilliams/fortran_function_parser): function parser module by Jacob Williams is intended for applications where a set of mathematical fortran-style expressions is specified at runtime and is then evaluated for a large number of variable values. This is done by compiling the set of function strings into byte code, which is interpreted efficiently for the various variable values.

[Fortran Function Parser (ffp)](https://github.com/jacobwilliams/ffp): evaluates a string containing a mathematical expression that can be formed by numbers, brackets, functions, and variables, by Wilton P. Silva and Ivomar B. Soares

[hp](https://github.com/sgeard/hp): rpn calclulator with a maximum stack size of 5, by sgeard It has full support for real and complex numbers and will calculate summary statistics for a set of reals of real pairs.

[M_calculator](https://github.com/urbanjost/M_calculator): parse Fortran-like double precision scalar expressions, by urbanjost

[M_matrix](https://github.com/urbanjost/M_matrix): Fortran callable version of old matlab-like interface, by urbanjost

[shunting-yard-fortran](https://github.com/14NGiestas/shunting-yard-fortran): small expression parser using shunting yard algorithm, by Ian Giestas Pauli

## Fast Fourier Transform

[fftpack](https://github.com/fortran-lang/fftpack): double precision version of original fftpack, from fortran-lang

[FFTPack](https://github.com/keurfonluu/FFTPack): easily usable package of functions using wrapping the Fortran 77 FFTPack library, by keurfonluu

[kissfft-f](https://github.com/zoziha/kissfft-f): wrapper by zozhia for [KISS FFT](https://github.com/mborgerding/kissfft), a mixed-radix Fast Fourier Transform in C

## File I/O

[fmmap](https://github.com/PierUgit/fmmap): provides some of the features of the C posix or Windows memory mapped files under a simple and unique Fortran interface, by PierUgit.

[flibcsv](https://github.com/freevryheid/flibcsv): bindings by Andre Smit to [libcsv](https://github.com/rgamble/libcsv), a fast and flexible CSV library written in pure ANSI C that can read and write CSV data

[fortran_huffman](https://github.com/Euler-37/fortran_huffman): Huffman code compression, by Euler-37

[fortran-messagepack](https://github.com/Sinfaen/fortran-messagepack): prototype library for [MessagePack](https://msgpack.org/index.html) (an efficient binary serialization format) support in Fortran, by Kelly Schultz

[fortran-sperr](https://github.com/ofmla/fortran-sperr): interface bindings by Oscar Mojica to [SPERR](https://github.com/NCAR/SPERR), a lossy scientific (floating-point) data compressor in C and C++ that produces one of the best rate-distortion curves

[fortran-zstd](https://github.com/interkosmos/fortran-zstd): Fortran 2018 interface bindings to selected [Zstandard](https://facebook.github.io/zstd/) functions, by interkosmos. Zstandard is a fast compression algorithm, providing high compression ratios.

[High Performance Parallel Data Interface to HDF5 (h5part)](https://github.com/zoziha/h5part): interface to the structured HDF5 data format that stores multiple time-step data for particle simulation scenarios and can be used for ParaView / VisIt visualization, by zoziha

[IO Fortran Library](https://github.com/acbbullock/IO-Fortran-Library): module providing high level routines for doing internal and external IO, by Austin C. Bullock. In particular, the module provides a handful of generic interfaces for performing string-based and array-based IO that are useful for recording program data, reading data into programs, and for writing formatted logs and output. 

[io_utilities](https://github.com/arjenmarkus/io_utilities): modules to help with input and output, by Arjen Markus: <b>cmdparse</b> parser for minimalistic commands (keyword and zero or more arguments), <b>keyvars</b> read in INI-files and fill in the values of the variables automatically, can also save the data in an INI-file, <b>progressbar</b> presents a progress bar on the screen (supports different styles)

[json-fortran-benchmarks](https://github.com/jacobwilliams/json-fortran-benchmarks): benchmarks for JSON Fortran parsers, by jacobwilliams. Also comparison to Python. Discussed [here](https://fortran-lang.discourse.group/t/a-new-json-library/2197/11)

[h5fortran-mpi](https://github.com/scivision/h5fortran-mpi): HDF5-MPI parallel Fortran object-oriented interface, from scivision

[hdf5-benchmark](https://github.com/scivision/hdf5-benchmark): benchmarking speed of HDF5 writes from MPI parallel workers, by scivision

[h5fortran](https://github.com/geospace-code/h5fortran): Simple, robust, thin HDF5 polymorphic Fortran read/write interface, by geospace-code

[nc4fortran](https://github.com/geospace-code/nc4fortran): object-oriented Fortran NetCDF4 interface, by geospace-code

[NetCDF Input-Output (NCIO)](https://github.com/alex-robinson/ncio): simple Fortran interface to NetCDF reading and writing, by alex-robinson

[Return of JSON for Fortran (rojff)](https://github.com/everythingfunctional/rojff): with an interface inspired by [jsonff](https://gitlab.com/everythingfunctional/jsonff), the data semantics and parser are redesigned to allow for high performance, by Brad Richardson and kmorris

[Self-Baked-Fortran-NetCDF-Library](https://github.com/han190/Self-Baked-Fortran-NetCDF-Library): light-weight NetCDF C Library wrapper and an intermediate interface, by Han Tang. The major difference between this library and most of the other implementations (for example nc4fortran) is that this library is built on top of NetCDF C library directly.

[stl-fortran](https://github.com/jacobwilliams/stl-fortran): Fortran STL (stereolithography) File I/O, by Jacob Williams

[toml-f](https://github.com/toml-f/toml-f): TOML parser implementation for data serialization and deserialization in Fortran. [jonquil](https://github.com/toml-f/jonquil) provides a compatibility layer to enable TOML Fortran using libraries to consume JSON as well as allow JSON consuming libraries to try out TOML.

[VTKFortran](https://github.com/szaghi/VTKFortran): parse and emit files conforming VTK (XML) standard, by szaghi et al.

## Finite Elements

[metis-fpm](https://github.com/gnikit/metis-fpm): Fortran API and a source repackaging by gnikit of [METIS](https://github.com/KarypisLab/METIS), a set of serial programs for partitioning graphs, partitioning finite element meshes, and producing fill reducing orderings for sparse matrices, from KarypisLab

[ParMETIS for fpm](https://github.com/gnikit/parmetis-fpm): Fortran API and a source repackaging by gnikit of [ParMETIS](https://github.com/KarypisLab/ParMETIS), an MPI-based library for partitioning graphs, serial programs for partitioning graphs, partitioning finite element meshes, and producing fill reducing orderings for sparse matrices, from KarypisLab

## Fortran Books and Tutorials

[fortran2018-examples](https://github.com/scivision/fortran2018-examples): Fortran 2018 standard examples with broad applications, from SciVision

[githubactions_intro](https://github.com/ofmla/githubactions_intro): introduces Github Actions as a tool for lightweight automation of scientific data workflows, with examples in Python and Fortran using gnuplot, by Oscar Mojica

[M_intrinsics](https://github.com/urbanjost/M_intrinsics): man(1) pages for the standard Fortran intrinsics, with a secondary goal of providing a tested working example program for each intrinsic

## Games and Puzzles

[blocktran](https://github.com/fortran-gaming/blocktran): falling-block object-oriented Fortran 2018 game, with resizable playfield, from fortran-gaming

[fortran-raylib](https://github.com/interkosmos/fortran-raylib): interface bindings to raylib 4.5, for 2-D and 3-D game programming, by interkosmos

[mastermind](https://github.com/fortran-gaming/mastermind): classic MasterMind game in modern Fortran 2008, from fortran-gaming

[ForSudoku](https://github.com/vmagnin/ForSudoku): sudoku generator and solver, by Vincent Magnin

## General Purpose

[argparse-f](https://github.com/0382/argparse-f): Modern Fortran command line parser, implemented with OOP, by 0382 and zoziha

[argv-fortran](https://github.com/jacobwilliams/argv-fortran): a better get_command_argument for Fortran that returns the argument in an allocatable character string, by Jacob Williams

[BeFoR64](https://github.com/szaghi/BeFoR64): Base64 encoding/decoding library for FoRtran poor men, is a pure Fortran (KISS) library for base64 encoding/decoding for modern (2003+) Fortran projects

[FACE](https://github.com/szaghi/FACE): Ansi Colors and Styles Environment, by szaghi et al.

[FLAP](https://github.com/szaghi/FLAP): command Line Arguments Parser for poor people, by szaghi et al. A KISS pure Fortran Library for building powerful, easy-to-use, elegant command line interfaces

[forbear](https://github.com/szaghi/forbear): progress bar environment by szaghi and jhykes

[ForClust](https://github.com/gha3mi/forclust): manage and control a Linux system, such as adjusting the settings of the CPU and other components, by Seyed Ali Ghasemi

[Fortran pathlib](https://github.com/scivision/fortran-pathlib): Filesystem path manipulation utilities for standard Fortran, from scivision. Inspired by Python pathlib and C++17 filesystem.

[fortran-sleep](https://github.com/scivision/fortran-sleep): OS/compiler-independent "sleep" Fortran subroutine that calls c_sleep, from scivision

[fortran_utilities](https://github.com/lewisfish/fortran_utilities): procedures to add colour to output via ANSI colour codes, create a progress bar, turn variables into strings, and print the time, by Lewis McMillan

[fortran-zlib](https://github.com/interkosmos/fortran-zlib): collection of Fortran 2018 ISO_C_BINDING interfaces to selected zlib functions, by interkosmos. Zlib is a lossless data-compression library.

[ForTime](https://github.com/gha3mi/fortime): provides a timer object for measuring elapsed time, by Seyed Ali Ghasemi. It includes procedures for starting and stopping the timer, as well as calculating and printing the elapsed time in seconds.

[functional-fortran](https://github.com/wavebitscientific/functional-fortran): library for functional programming in modern Fortran

[fwalk](https://github.com/freevryheid/fwalk): Fortran bindings by Andre Smit for [libcwalk](https://github.com/likle/cwalk), a lightweight C path manipulation library for Unix and Windows

[general-purpose-fortran](https://github.com/urbanjost/general-purpose-fortran): non-numeric tasks such as command-line parsing, string functions, date-and-time manipulation and display, interfacing to the C POSIX system routines, by urbanjost

[json-fortran](https://github.com/jacobwilliams/json-fortran): user-friendly, thread-safe, and object-oriented API for reading and writing JSON files, written in modern Fortran, by Jacob Williams

[M_CLI2](https://github.com/urbanjost/M_CLI2): cracks the command line when given a prototype string that looks very much like an invocation of the program, by urbanjost. A call to get_args(3f) or one of its variants is then made for each parameter name to set the variables appropriately in the program.

[M_history](https://github.com/urbanjost/M_history): input line history editor, by urbanjost

[M_kracken95](https://github.com/urbanjost/M_kracken95): Fortran 95 version of the kracken(3f) procedure (and related routines) for command line parsing, by urbanjost

[M_msg](https://github.com/urbanjost/M_msg): convert all common variables to a string in Fortran using unlimited polymorphic variables, by urbanjost. 

[M_sets](https://github.com/urbanjost/M_sets): basic set functions reminiscent of those in Matlab: `union`, `unique`, `intersect`, `setdiff`, `ismember`, `setxor`, by urbanjost

[oolong](https://github.com/EdHone/oolong): object-oriented logging system by Ed Hone that aims to provide a simple, flexible logging interface that will enable a wide range of logging functionality for a wide range of model paradigms

[paramcard](https://github.com/tueda/paramcard): command-line parameter input made simple, by Takahiro Ueda

[PENF](https://github.com/szaghi/PENF): Fortran (standard 2003) module useful to achieve portable codes. The module makes available portable kind-parameters and some useful procedures to deal with them

[QDUtilLib](https://github.com/lauvergn/QDUtilLib): modules for numerical parameters, strings, reading and write matrices, and linear algebra, by lauvergn

[Quantities for Fortran (quaff)](https://github.com/everythingfunctional/quaff): makes math with units more convenient, by Brad Richardson et al. This library provides all the functionality necessary to almost treat quantities with units associated with them as though they were just intrinsic real values

[reference-counter](https://github.com/sourceryinstitute/reference-counter): object-oriented, extensible reference-counting utility for Fortran, by Damian Rouson et al.

[SM3-Fortran](https://github.com/zoziha/SM3-Fortran): library with a Fortran interface SM3 by zoziha of GmSSL and its usage examples. The SM3 password hashing algorithm is a hash algorithm similar to SHA-256, which belongs to the Chinese national standard. 

[sourcery](https://github.com/sourceryinstitute/sourcery): utilities such as array functions, assertions, emulated intrinsic functions: findloc, emulated collective subroutines: co_sum, co_broadcast, user-defined collective subroutines: co_all, string functions, and classes for parallel data partitioning and gathering and the (Co-)Object pattern abstract parent, by Damian Rouson and Brad Richardson

[tictoc_fortran](https://github.com/wcota/tictoc_fortran): TicToc (timer) class that calls `cpu_time`, by Wesley Cota

[timer](https://github.com/zoziha/timer): module to get the number of seconds between two timestamps, by zoziha

## Graphics, Plotting, and User Interfaces

[cairo-fortran](https://github.com/vmagnin/cairo-fortran): libcairo bindings for Fortran from the gtk-fortran project available as a separate fpm package, by Carlos Une

[ForCAD](https://github.com/gha3mi/forcad): library for geometric modeling, supporting B-Spline, NURBS, Bezier, and Rational Bezier curves, surfaces, and volumes, by Seyed Ali Ghasemi

[ForColormap](https://github.com/vmagnin/forcolormap): small colormap library independent of any graphical toolkit, by Vincent Magnin et al. It just converts a real value to RGB values, that can be used with any toolkit offering bitmap drawing..

[ForImage](https://github.com/gha3mi/forimage): library for working with image files ([PNM format](https://en.wikipedia.org/wiki/Netpbm)) and managing colors effectively, by Seyed Ali Ghasemi

[fortran-dialog](https://github.com/interkosmos/fortran-dialog): wrapper module by interkosmos around [dialog](https://invisible-island.net/dialog/) to create text user interfaces in Fortran 2008, similar to [pythondialog](https://pythondialog.sourceforge.io/) for Python

[Fortran Intuitive Graphics (fig)](https://github.com/AnonMiraj/fig): provide intuitive graphics capabilities, by Aِl-Mi'raj. It offers basic 2D primitives such as lines, circles, ellipsis, and rectangles for creating graphical representations.

[fortran-sdl2](https://github.com/interkosmos/fortran-sdl2): collection of ISO C binding interfaces to Simple DirectMedia Layer 2.0 (SDL 2.0), for 2D and 3D game programming in Fortran, by interkosmos

[fortran-grace](https://github.com/interkosmos/fortran-grace): collection of Fortran 2018 interfaces to the scientific plotting tool [Grace](https://plasma-gate.weizmann.ac.il/Grace/)/XmGrace, by interkosmos. This library covers the FORTRAN 77 and the C API of Grace. This library covers the FORTRAN 77 and the C API of Grace.

[fortran-motif](https://github.com/interkosmos/fortran-motif): collection of ISO C binding interfaces to X/Motif, to create graphical user interfaces for Unix in Fortran 2008, by interkosmos. The library includes selected bindings to Xlib, Xt, Xm, and the XmHTML widget to render HTML 3.2 inside a Motif widget (optional).

[fortran-simplify](https://github.com/jaiken17/fortran-simplify): module to reduce the over-sampled resolution of a [polyline](https://en.wikipedia.org/wiki/Polygonal_chain), implementing the nth_point, radial_distance, perpendicular distance, and Reumann-Witkam algorithms, by Joshua Aiken. This process can be useful when working with data that is noisy but usable with a significantly reduced resolution.

[fortran_stb_image](https://github.com/lewisfish/fortran_stb_image): bindings by Lewis McMillan for [stb_image](https://github.com/nothings/stb) and stb_image_write, for reading, loading, and processing images

[Fortran Terminal (fortty)](https://github.com/awvwgk/fortty): create colorful terminal applications in Fortran, by Sebastian Ehlert

[fortran-xlib](https://github.com/interkosmos/fortran-xlib): collection of ISO C binding interfaces to Xlib for Fortran 2003, by interkosmos. Currently, only a subset of Xlib is implemented. In order to work with XPM files, interfaces to libxpm are included.

[fplot](https://github.com/jchristopherson/fplot): provides a convenient interface for plotting with Gnuplot, by jchristopherson

[gtk-fortran](https://github.com/vmagnin/gtk-fortran): cross-platform library to build Graphical User Interfaces (GUI), by Vincent Magnin et al. Gtk-fortran is a partial GTK / Fortran binding 100% written in Fortran, thanks to the ISO_C_BINDING module for interoperability between C and Fortran. [gtk-fortran-extra](https://github.com/vmagnin/gtk-fortran-extra) has extra examples under an MIT license

[M_attr](https://github.com/urbanjost/M_attr): set terminal text attributes using ANSI escape sequences

[M_color](https://github.com/urbanjost/M_color): convert between RGB color values and other common color models, by urbanjost

[M_draw - low level vector graphics library](https://github.com/urbanjost/M_draw): base graphics library intended for use with Fortran although largely written in C. It is based on the public domain VOGLE graphics library. It allows for creating vector-based graphics with a variety of output devices.

[M_fixedform](https://github.com/urbanjost/M_fixedform): simplifies creating a TUI (Terminal User Interface) with Ncurses from Fortran, by urbanjost. It facilitates creating simple forms in terminal windows.

[M_ncurses](https://github.com/urbanjost/M_ncurses): module that allows use of the C Ncurses library for controlling and formatting terminal displays, by urbanjost

[M_pixel](https://github.com/urbanjost/M_pixel): creates pixel images with a vector-oriented graphics library that emulates a subset of the [M_draw](https://github.com/urbanjost/M_draw) vector graphics library, by urbanjost. It is supplemented with additional modules that read and write GIF files, including animated GIFs.

[ogpf](https://github.com/kookma/ogpf): Object-Based Interface to GnuPlot from Fortran, by kookma

[PlPlotLib](https://github.com/zoziha/PlPlotLib): wrapper for PlPlot inspired by the interface of matplotlib, by zoziha. It is intended to fill the need for rapid feedback while developing numerical simulations, and does not replace more sophisticated packages such as matplotlib or even direct use of PlPlot.

[pyplot-fortran](https://github.com/jacobwilliams/pyplot-fortran): generate plots from Fortran using Python's [matplotlib.pyplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html), by jacobwilliams

## Interoperability

[arrow-fortran](https://github.com/ludnic/arrow-fortran): automatic bindings by Ludovico Nicotina and Vincent Magnin to the C API for the arrow project. [Arrow](https://arrow.apache.org/) is a language-independent columnar memory format for flat and hierarchical data, organized for efficient analytic operations on modern hardware like CPUs and GPUs. 

[dynload-julia](https://github.com/yundantianchang/dynload-julia): dynamically load Julia from Fortran, by brocolis

[fcppstring](https://github.com/willdickson/fcppstring): Fortran wrapper for C++ strings, by Will Dickson

[fortran-c-cpp-interface](https://github.com/scivision/fortran-c-cpp-interface): interoperability examples between C, C++ and Fortran, from scivision. Uses the standard C binding to define variable and bind functions/subroutines.

[fortran-curl](https://github.com/interkosmos/fortran-curl): collection of ISO C binding interfaces to libcurl for Fortran 2008, by interkosmos. Compilation has been tested with GNU Fortran 10 and cURL 7.74.0.

[fortran-lua54](https://github.com/interkosmos/fortran-lua54): Fortran 2008 interface bindings to Lua 5.4, from interkosmos. There is also [fortran-lua53](https://github.com/interkosmos/fortran-lua53).

[fortran-tcl86](https://github.com/interkosmos/fortran-tcl86): ISO_C_BINDING interface library for interoperability with Tcl/Tk 8.6, by interkosmos, allowing the user to embed Tcl into Fortran, create Tcl extensions in Fortran (with Tcl Stubs), access (a subset of) the Tcl/Tk C API from Fortran, use Tcl as an evaluatable configuration file format, and add graphical user interfaces to Fortran programs.

[fortran-unix](https://github.com/interkosmos/fortran-unix): Fortran 2008 ISO C binding interfaces to selected POSIX and SysV types, functions, and routines on 64-bit Unix-like operating systems, by interkosmos

[hwinfo-fortran](https://github.com/ShinobuAmasaki/hwinfo-fortran): provides access to hardware information using OS APIs for Unix-like operating systems, by Shinobu Amasaki

[M_process](https://github.com/urbanjost/M_process): read and write lines to or from a process from Fortran via a C wrapper, by urbanjost

[M_system](https://github.com/urbanjost/M_system): module that allows Fortran to call commonly available C routines that perform basic system operations like creating and deleting files and directories, changing and querying file permits, getting basic ID and process information, ... and other POSIX system requests, by urbanjost

[popen-fortran](https://github.com/jacobwilliams/popen-fortran): module for popen() by Jacob Williams, which executes a command specified by a string argument, creates a pipe between the calling program and the executed command, and returns a pointer to a stream that can be used to either read from or write to the pipe.

[uint-fortran](https://github.com/ShinobuAmasaki/uint-fortran): unsigned integer, 16 or 32 bit, that is interoperable with C, by Shinobu Amasaki

## Interpolation

[bspline-fortran](https://github.com/jacobwilliams/bspline-fortran): Multidimensional B-Spline Interpolation of Data on a Regular Grid, by Jacob Williams

[finterp](https://github.com/jacobwilliams/finterp): performs multidimensional (1D-6D) linear interpolation of data on a regular grid, by Jacob Williams. The code is written in modern Fortran (2003/2008) and is object-oriented and thread safe.

[interpolation](https://github.com/furstj/interpolation): Matlab/Octave-like interpolation functions such as linear and PCHIP (Piecewise Cubic Hermite Interpolating Polynomial), by Jiří Fürst

[PCHIP](https://github.com/jacobwilliams/PCHIP): piecewise cubic Hermite interpolation of data, by Jacob Williams. It features software to produce a monotone and "visually pleasing" interpolant to monotone data.

[regridpack](https://github.com/jacobwilliams/regridpack): routines for interpolating values between one-, two-, three-, and four-dimensional arrays defined on uniform or nonuniform orthogonal grids, from Jacob Williams

## Linear Algebra

[blas-interface](https://github.com/awvwgk/blas-interface): interface declarations for basic linear algebra subprograms, by Sebastian Ehlert

[ForBLAS](https://github.com/gha3mi/forblas): compile the BLAS and their drivers using the Fortran Package Manager, by Seyed Ali Ghasemi. [ForLAPACK](ForLAPACK) does so for LAPACK. 

[ForSVD](https://github.com/gha3mi/forsvd) provides functions and subroutines for calculating the singular value decomposition (SVD) of a matrix, calling LAPACK. [ForEig](https://github.com/gha3mi/foreig) calculates eigenvalues and eigenvectors using LAPACK or MKL. [ForPCA](https://github.com/gha3mi/forpca) does principal component analysis (PCA).

[ForInv](https://github.com/gha3mi/forinv) calculates the inverse and pseudoinverse of a matrix.

[ForDot](https://github.com/gha3mi/fordot): overloads the dot_product function to enable efficient dot product with/without coarrays, by Seyed Ali Ghasemi

[ForMatMul](https://github.com/gha3mi/formatmul): library that overloads the matmul function to enable efficient matrix multiplication with coarrays, by Seyed Ali Ghasemi

[fortran-lapack](https://github.com/perazz/fortran-lapack): modern Fortran implementation of the Reference-LAPACK library, by Federico Perini. The reference Fortran 77 library is automatically downloaded from its master repository, and processed to create Modern Fortran modules with full explicit typing features.

[FSPARSE](https://github.com/jalvesz/FSPARSE): object-oriented API for sparse matrices with some basic kernels and utility functions, such as conversion from dense matrices and matrix-vector products, by jalvesz. Supported sparse matrix types are COordinate Sparse format (COO), Compressed Sparse Row format (CSR), Compressed Sparse Column format (CSC), and [ELLPACK](https://people.math.sc.edu/Burkardt/data/sparse_ellpack/sparse_ellpack.html) (ELL).

[libsparse](https://github.com/jvdp1/libsparse): Fortran 2003 library that provides objects to create and handle rectangular and square sparse matrices using different formats: Linked List, COOrdinate storage (with elements stored using a hashing function), or Compressed Row Storage, by Jeremie Vandenplas. The library relies on different libraries, such as BLAS/LAPACK libraries, PARDISO (at this stage, Intel MKL PARDISO), and METIS 5. 

[LIBXSMM](https://github.com/hfp/libxsmm): library for specialized dense and sparse matrix operations as well as for deep learning primitives such as small convolutions, from hfp

[LightKrylov](https://github.com/nekStab/LightKrylov): provides a simple set of Krylov-based techniques to study the spectral properties of the exponential propagator. Associated paper: R. S. Frantz, J.-Ch. Loiseau, and J.-Ch. Robinet. [Krylov methods for large-scale dynamical systems: applications in fluid dynamics.](https://asmedigitalcollection.asme.org/appliedmechanicsreviews/article-abstract/75/3/030802/1156502/Krylov-Methods-for-Large-Scale-Dynamical-Systems?redirectedFrom=fulltext) Appl. Mech. Rev., 2023.

[linalg](https://github.com/jchristopherson/linalg): linear algebra library that provides a user-friendly interface to several BLAS and LAPACK routines, by jchristopherson

[linalg_fortran](https://github.com/Euler-37/linalg_fortran): interface to Lapack procedures that invert matrices, compute determinants, compute eigenvalues and eigenvectors of symmetric or Hermitian matrices, and compute U*A*U.T, by Euler-37

[LSMR](https://github.com/jacobwilliams/LSMR): code for sparse equations and least squares, originally by David Fong and Michael Saunders, updated by Jacob Williams

[LSQR](https://github.com/jacobwilliams/LSQR): Fortran 2008 edition of [LSQR](https://web.stanford.edu/group/SOL/software/lsqr/), a conjugate-gradient type method for solving sparse linear equations and sparse least-squares problems, by Jacob Williams.

[mfi](https://github.com/14NGiestas/mfi): modern Fortran Interfaces to BLAS and LAPACK, by 14NGiestas

[M_LA](https://github.com/urbanjost/M_LA): small collection of linear algebra routines, including reshaping an array, creating a [magic square](https://en.wikipedia.org/wiki/Magic_square) array, and computing the determinant and inverse of a matrix, by urbanjost

[minres](https://github.com/willdickson/minres): implementation of MINRES by Will Dickson based on the original Fortran 90 code by Chris Paige, Sou-Cheng Choi, and Michael Saunders, which solves sparse symmetric systems Ax = b

[sparse_fortran](https://github.com/Euler-37/sparse_fortran): derived types for sparse matrices in COO and CSR format with functions for matrix multiplication, by Euler-37

## Materials Science

## Mesh Generation

[geompack](https://github.com/jchristopherson/geompack): modernization by Jason Christopherson of the [GEOMPACK](https://www.sciencedirect.com/science/article/abs/pii/0961355291900364) Fortran 77 library by Barry Joe for computing Delaunay triangulations

[gmsh-fpm](https://github.com/gnikit/gmsh-fpm): provides access to the Fortran F2018 API of Gmsh, examples of how to use the Fortran API, and a Fortran compiled executable for Gmsh itself, by gnikit

## Molecular Dynamics

[Packmol](https://github.com/m3g/packmol): creates an initial point for molecular dynamics simulations by packing molecules in defined regions of space, from Martinez Molecular Modeling Group. The packing guarantees that short range repulsive interactions do not disrupt the simulations.

## Neural Networks and Machine Learning

[Adaptive Training for High Efficiency Neural Network Applications (ATHENA)](https://github.com/nedtaylor/athena): library for developing and handling neural networks (with a focus on convolutional neural networks), by Ned Taylor

[forncnn](https://github.com/mizu-bai/forncnn): experimental Fortran binding for [ncnn](https://github.com/Tencent/ncnn) c_api, by mizu-bai. Ncnn is a high-performance neural network inference framework optimized for the mobile platform.

[Fortran FLANN binding](https://github.com/ivan-pi/fortran-flann): Fortran bindings to the FLANN library for performing fast approximate nearest neighbor searches in high dimensional spaces, by ivan-pi

[Inference-Engine](https://github.com/BerkeleyLab/inference-engine): software library by Damian Rouson et al. for researching ways to efficiently propagate inputs through deep, feed-forward neural networks exported from Python by the companion package nexport

[neural-fortran](https://github.com/modern-fortran/neural-fortran): parallel neural net microframework, from modern-fortran

## Numerical

[amosf90](https://github.com/Euler-37/amosf90): module for [AMOS](https://www.netlib.org/amos/), a package for Bessel functions of a complex argument and nonnegative order, by Euler-37

[fastconv](https://github.com/gronki/fastconv): simple library for 1D and 2D convolutions, by Dominik Gronkiewicz

[fastmath](https://github.com/perazz/fastmath): library for fast, approximate math functions: exp, log, 1/sqrt, by Federico Perini. These functions provide fast, approximate evaluations of the exponential, logarithm and normalization functions in 64-bit precision.

[fast_math](https://github.com/jalvesz/fast_math): collection of functions for fast number crunching, including a fast and precise sum and dot_product for 1D arrays, a reciprocal square root, the logarithm, and trigonometric functions, by jalvesz

[ForDiff](https://github.com/gha3mi/fordiff): numerical differentiation using the complex step method or finite differences, by Seyed Ali Ghasemi

[forlab](https://github.com/zoziha/forlab): module that provides a lot of functions for scientific computing mostly inspired by Matlab and Python's module NumPy, by zoziha

[ForSolver](https://github.com/gha3mi/forsolver): solves linear and nonlinear equations, by Seyed Ali Ghasemi. For nonlinear equations the available methods are newton, newton-modified, newton-quasi-fd, newton-quasi-fd-modified, newton-quasi-cs, and newton-quasi-cs-modified, where "fd" and "cs" stand for the finite difference and complex step methods.

[fortran-bessels](https://github.com/perazz/fortran-bessels): Fortran port (stub) of the Bessels.jl repository, by Federico Perini et al.

[fortran-primes](https://github.com/perazz/fortran-primes): library to return the nth prime number, the prime numbers in a range, test if a number is prime, return the nth prime number greater than a specified number, and factor a number into primes, by Federico Perini, based in part on codes by Michal Forisek, David Deley and Primes.jl

[GaussJacobiQuad](https://github.com/HaoZeke/GaussJacobiQuad): routines for the Gauss-Jacobi Quadrature, by Rohit Goswami and Ondřej Čertík

[NAFPack](https://github.com/Minard-Jules/NAFPack): numerical analysis package, offering a comprehensive set of algorithms for diverse numerical computations, by Jules Minard. These computations include Fast Fourier Transform, linear system solving, and eigenvalue/eigenvector calculations.

[Nonlinear Equation Solver with Modern Fortran (nlesolver-fortran)](https://github.com/jacobwilliams/nlesolver-fortran): basic Newton-Raphson type nonlinear equation solver for dense systems with m functions of n input variables, by Jacob Williams. Uses LAPACK routines (dgesv or dgels) to solve the linear system.

[NumDiff](https://github.com/jacobwilliams/NumDiff): modern Fortran numerical differentiation library, by Jacob Williams

[Numerical_utilities](https://github.com/osada-yum/Numerical_utilities): Kahan algorithms for the sum, variance, and covariance, using MPI, by osada-yum

[polyroots-fortran](https://github.com/jacobwilliams/polyroots-fortran): modern Fortran library for finding the roots of polynomials, by Jacob Williams

[rational_number](https://github.com/art-rasa/rational_number): procedures for rational numbers, such as arithmetic operations, conversion to and from real variables, and conversion to a string, by art-rasa

[roots-fortran](https://github.com/jacobwilliams/roots-fortran): library for finding the roots of continuous scalar functions of a single real variable, by Jacob Wiliams

[rpn-calc-fortran](https://github.com/scivision/rpn-calc-fortran): Fortran 2018 Reverse Polish Notation (RPN) calculator from scivision. Over 100 functions not in standard Fortran

[specfun](https://github.com/jacobwilliams/specfun): modernization by Jacob Williams of [specfun.f](https://github.com/scipy/scipy/blob/main/scipy/special/specfun/specfun.f) from SciPy from the book [Computation of Special Functions](https://www.amazon.com/Computation-Special-Functions-Shanjie-Zhang/dp/0471119636), by Shanjie Zhang and Jianming Jin, Wiley (1996).

[specfunc-fullerton](https://github.com/arjenmarkus/specfunc-fullerton): library for evaluating special mathematical function, based on the [fn](http://www.netlib.org/fn/index.html) library of Wayne Fullerton, modernised by Arjen Markus. It has Airy functions, modified Bessel functions, beta functions, exponential and logarithmic integrals, gamma functions, inverse cosine and cosine hyperbolic integrals, miscellaneous functions, and Pochhammer symbols

## Numerical Integration (Quadrature)

[integrate_fortran](https://github.com/Euler-37/integrate_fortran): Gauss–Legendre quadrature for 1D and multidimensional integrals, by Euler-37

[kronrod](https://github.com/jacobwilliams/kronrod): generates [Gauss-Kronrod](https://en.wikipedia.org/wiki/Gauss%E2%80%93Kronrod_quadrature_formula) coefficients, by Jacob Williams

[Quadpack2](https://github.com/jacobwilliams/quadpack): update by Jacob Williams and Sebastian Ehlert of QUADPACK, a FORTRAN subroutine package for the numerical computation of definite one-dimensional integrals

[quadrature-fortran](https://github.com/jacobwilliams/quadrature-fortran): adaptive Gaussian quadrature with modern Fortran, by jacobwilliams

## Ordinary Differential Equations

[ddeabm](https://github.com/jacobwilliams/ddeabm): modern object-oriented Fortran implementation of the DDEABM Adams-Bashforth-Moulton ODE solver, by Jacob Williams and web-flow

[dop853](https://github.com/jacobwilliams/dop853): modern Fortran (2003/2008) implementation of Hairer's DOP853 ODE solver, by Jacob Williams. The original FORTRAN 77 code has been extensively refactored, and is now object-oriented and thread-safe, with an easy-to-use class interface. DOP853 is an explicit Runge-Kutta method of order 8(5,3) due to Dormand & Prince (with stepsize control and dense output).

[dvode](https://github.com/jacobwilliams/dvode): Modern Fortran Edition of the [DVODE](https://computing.llnl.gov/projects/odepack) ODE Solver, by Jacob Williams

[Fortran Library for numerical INTegration of differential equations (FLINT)](https://github.com/princemahajan/FLINT): modern object-oriented fortran library that provides four adaptive step-size explicit Runge-Kutta (ERK) methods of order 5, 6, 8, and 9 along with dense-output and multiple event-detection support for each of the methods, by Bharat Mahajan. The code is written such that any other ERK method can be implemented by including its coefficients with minimum changes required in the code. 

[ODEPACK](https://github.com/jacobwilliams/odepack): collection of solvers for the initial value problem for ordinary differential equation systems

[odepack](https://github.com/Nicholaswogan/odepack): Modern Fortran interface by Nick Wogan for the LSODA and LSODAR routines in ODEPACK, which is for solving ordinary differential equation initial value problems. This repository contains a modified version of ODEPACK which is threadsafe.

[rkf45](https://github.com/zoziha/rkf45): Fehlberg fourth-fifth order Runge-Kutta method, adapted by zoziha from the code at Netlib

[rklib](https://github.com/jacobwilliams/rklib): Fixed and variable-step Runge-Kutta solvers in Modern Fortran, by Jacob Williams

[stiff3](https://github.com/ivan-pi/stiff3): subprogram for solving stiff autonomous systems of ordinary differential equations (ODE's) using a semi-implicit Runge-Kutta method with three steps (SIRK3), by Ivan Pribec and Sebastian Ehlert. The stiff3 source code was originally published in the following book: Villadsen, J., & Michelsen, M. L. (1978). [Solution of differential equation models by polynomial approximation](http://www.gbv.de/dms/ilmenau/toc/011270667.PDF). Prentice-Hall, Inc.

[twopnt](https://github.com/perazz/twopnt): modern Fortran translation by Federico Perini of the [TWOPNT](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=dcf780dafc70adedeff9a9348d5e5e2225031326) program for boundary value problems

## Optimization

[conmax](https://github.com/jacobwilliams/conmax): general nonlinearly constrained function minimization

[fmin](https://github.com/jacobwilliams/fmin): derivative-free 1D function minimizer in modern Fortran, by Jacob Williams

[lbfgsb](https://github.com/jacobwilliams/lbfgsb): limited memory code for solving bound constrained optimization problems, by Jorge Nocedal and Jose Luis Morales 

[libdogleg-f](https://github.com/ivan-pi/libdogleg-f): Fortran bindings to libdogleg - a large-scale nonlinear least-squares optimization library, by Ivan Pribec. Currently only the dense optimizer calls are supported.

[Minpack](https://github.com/certik/minpack): library for solving nonlinear equations and nonlinear least squares problems, with with CMake makefiles and examples by certik et al.

[Minpack](https://github.com/jacobwilliams/minpack): modernization of the original Fortran 77 code, by Jacob Williams

[nlopt-f](https://github.com/awvwgk/nlopt-wrap): Fortran bindings for the NLopt library, by awvwgk. While the NLopt library supports Fortran by using implicit interface calling conventions, those are not type-safe. 

[nonlin](https://github.com/jchristopherson/nonlin): solves systems of nonlinear equations, by jchristopherson

[pikaia](https://github.com/jacobwilliams/pikaia): Modern Fortran Edition of the Pikaia Genetic Algorithm by Jacob Williams

[PowellOpt](https://github.com/jacobwilliams/PowellOpt): collection of derivative-free optimization algorithms by M.J.D. Powell. 

[pso](https://github.com/Konrad1991/pso): particle swarm optimization in Fortran, by Konrad1991

[SEISCOPE optimization toolbox wrapper](https://github.com/ofmla/seiscope_opt_toolbox_w_ctypes): demonstrates how to use the [SEISCOPE optimization toolbox](https://seiscope2.osug.fr/SEISCOPE-OPTIMIZATION-TOOLBOX?lang=en) from Python. The original code is public domain and was written by Ludovic Métivier and Romain Brossier.

[slsqp](https://github.com/jacobwilliams/slsqp): Modern Fortran edition of the [SLSQP](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.512.2567&rep=rep1&type=pdf) optimizer, by Jacob Williams

[simulated-annealing](https://github.com/jacobwilliams/simulated-annealing): Simulated Annealing with Modern Fortran by Jacob Williams 

## Parallel Programming

[cafut](https://github.com/renatomatz/cafut): provides a simple, object-oriented unit testing framework meant for applications using Coarray Fortran, by Renato Zimmermann

from the companion website to the book [CUDA Fortran for Scientists and Engineers](http://store.elsevier.com/product.jsp?isbn=9780124169708)

[Emulators](https://github.com/sourceryinstitute/emulators): emulated collectives collection: collective subroutines and other procedures designed to emulate or extend standard language features, by Damian Rouson. Emulated features include the Fortran 2008 intrinsic function findloc and the Fortran 2018 collective subroutines co_sum and co_broadcast.

[Framework for Extensible Asynchronous Task Scheduling (FEATS)](https://github.com/sourceryinstitute/FEATS): project to develop a parallel Fortran 2018 asynchronous, task-scheduling framework for use in a range of applications, from sourceryinstitute

## Partial Differential Equations

## Particle Physics

## Plasma Physics

## Physics

[codata](https://github.com/MilanSkocic/codata): provides the codata constants 2010, 2014 and 2018, by Milan Skocic. The raw codata from http://physics.nist.gov/constants are parsed line by line where the columns name, value, uncertainty and unit are formatted to be conform to Fortran double precision. [pycodata](https://github.com/MilanSkocic/pycodata) is a Python wrapper.

[electron-phonon Boltzmann transport (elphbolt)](https://github.com/nakib/elphbolt): Fortran 2018 code for solving the coupled electron and phonon Boltzmann transport equations (BTEs), by nakib. Using ab initio electron-phonon and phonon-phonon interactions and a fully wave vector and electron band/phonon branch resolved formulation of the BTEs, elphbolt can calculate the phonon and electronic thermal conductivities; electronic conductivity; phonon and electronic contributions to the thermopower; and effect of the mutual electron-phonon drag on the transport coefficients listed above.

[fundamental_constants](https://github.com/vmagnin/fundamental_constants): modules with the CODATA fundamental physical constants, generated by a Python script from the NIST website, by Vincent Magnin

[Neural-Network-Quantum-States](https://github.com/acbbullock/Neural-Network-Quantum-States): machine learning demonstration of neural network quantum states, by acbbullock

[signedMCRT](https://github.com/lewisfish/signedMCRT): use of signed distance fields in Monte Carlo Radiative Transfer, by Lewis McMillan. This allows modelling of smooth surfaces without the need to use triangle or similar meshes.

## Quantum Chemistry and Electronic Structure

[dftd4](https://github.com/dftd4/dftd4): Generally Applicable Atomic-Charge Dependent London Dispersion Correction

[Finite Element Solvers for Atomic Structure Calculations (featom)](https://github.com/atomic-solvers/featom): library implementing accurate and efficient radial Schrödinger and Dirac finite element solvers, by Ondřej Čertík, Rohit Goswami, and Isuru Fernando. The formulation admits general potentials and meshes: uniform, exponential, or other.

[General Quantum Chemistry Properties Grabber (gpg)](https://github.com/lukaswittmann/gpg): obtains a wide range of properties, including molecular geometries, electronic energies, dipole moments, vibrational frequencies, from the output files of popular quantum chemistry software packages, including ORCA, Qchem and Turbomole, by Lukas Wittmann

[hartree-fock](https://github.com/lukaswittmann/hartree-fock): simple implementation of the Hartree-Fock algorithm, by Lukas Wittmann. STO-nG basis sets are used, which are generated from Slater exponents given in the input file. Some parts like the input reader and straightforward functions were taken from Marvin Friede's [hartree-fock](https://github.com/marvinfriede/hartree-fock) implementation. 

[HoneyTools](https://github.com/QcmPlab/HoneyTools) modules by Gabriele Bellomia to easily deal with nontrivial honeycomb structures in real-space: generate the coordinates, compute all the neighbor-shells, get direct access to logical masks for nearest and next-nearest neighbors (nth-order can be easily computed from the shell table), hence readily build tight-binding hamiltonians, or any other lattice quantity requiring real-space geometrical information.

[libconeangle](https://github.com/kjelljorner/libconeangle): library for calculating exact ligand cone angles according to the paper Bilbrey, J. A.; Kazez, A. H.; Locklin, J.; Allen, W. D. [Exact Ligand Cone Angles.](https://onlinelibrary.wiley.com/doi/abs/10.1002/jcc.23217) Journal of Computational Chemistry 2013, 34 (14), 1189–1197.

[Molecular Orbital KIT (MOKIT)](https://github.com/1234zou/MOKIT): utilities and modules to transfer MOs among various quantum chemistry software packages, by jxzou. In addition, the automr program in MOKIT can set up and run common multi-reference calculations in a block-box way.

[Quantum chemistry Utility for Benchmark Evaluation (QUBE)](https://github.com/lukaswittmann/qube): extracts energies from the output files of quantum chemistry calculations for large benchmark sets, by Lukas Wittmann. It utilizes reference energies for statistical evaluation and comparison of the results obtained from the benchmark sets.

[WannInt](https://github.com/irukoa/WannInt): library of utilities for Wannier interpolation, meant to serve as a building block for codes that compute the resolution of quantum mechanical operators in the Brillouin zone of a crystal, by Álvaro R. Puente-Uriona

## Random Number Generation

[mersenne-twister-fortran](https://github.com/jacobwilliams/mersenne-twister-fortran): Mersenne Twister pseudorandom number generator, by Jacob Williams

[pointsets](https://github.com/arjenmarkus/pointsets): modules to construct points in N-dimensional space, such as methods to visit grid points in N-dimensional space, generate points in N-dimensional space based on Latin hypercube samping, generate regularly spaced and pseudo-random points in N-dimensional space, generate quasi-random points in Euclidean N-dimensional space, unit circle, disk, sphere or ball, and return an array of integers in a random order, by Arjen Markus

[rngff](https://github.com/Archaeologic-Inc/rngff): unified abstract interface for an object-oriented random number generator and a collection of implementations using various algorithms, by Brad Richardson

[rndgen-fortran](https://github.com/wcota/rndgen-fortran): module for the [KISS](https://en.wikipedia.org/wiki/KISS_(algorithm)) random number generator that allows the use of multiple independent random number generators at the same time, by Wesley Cota, based on a code by Thomas Vojta. Module `rndgenPL_mod`, adapted from code by Silvio C. Ferreira, extends the generator to an integer power-law distribution.

## Reactor Physics

## Regular Expressions

[forgex](https://github.com/ShinobuAmasaki/forgex): regular expression engine using a deterministic finite automaton ([DFA](https://en.wikipedia.org/wiki/Deterministic_finite_automaton)) approach, by Shinobu Amasaki. It provides `.in.` and `.match.` operators to detect if a pattern is contained in or exactly matches a string.

[fortran-pcre2](https://github.com/interkosmos/fortran-pcre2): Fortran 2018 ISO_C_BINDING interfaces to Perl-compatible Regular Expressions 2 (PCRE2), by interkosmos

[fortran-regex](https://github.com/perazz/fortran-regex): port by Federico Perini of the [tiny-regex-c](https://github.com/kokke/tiny-regex-c) library for regular expressions. It is based on the original C implementation, but the API is modelled in Fortran style, which is similar to the intrinsic index function.

[Fregex](https://github.com/14NGiestas/fregex): Perl Compatible Regular Expressions (PCRE) wrapper for Fortran by Ian Giestas Pauli

[M_match](https://github.com/urbanjost/M_match): basic implementation in Fortran of a subset of regular expressions as described in "Software Tools" by Kernighan and Plauger, 1976.

[M_regex](https://github.com/urbanjost/M_regex): Fortran interface by urbanjost to the POSIX 1003.2 regular expression library using ISO_C_BINDING

## Sorting

[fortran-search-and-sort](https://github.com/jacobwilliams/fortran-search-and-sort): Searching and sorting with modern Fortran, by Jacob Williams

[M_sort](https://github.com/urbanjost/M_sort): collection of Fortran procedures that do simple sorts, by urbanjost

[orderpack](https://github.com/urbanjost/orderpack): clone by urbanjost of [Orderpack 2.0](http://www.fortran-2000.com/rank/) from Michel Olagnon that has been restructured so as to be useable as an fpm package. It provides order and unconditional, unique, and partial ranking, sorting, and permutation.

[stringsort](https://github.com/jacobwilliams/stringsort): sorting routines for strings, by Jacob Williams

## Statistics

[200+ R packages with Fortran code](https://github.com/cran?q=&type=&language=fortran&sort=): R is a free software environment for statistical computing and graphics

[fitpack](https://github.com/perazz/fitpack): modern Fortran translation by Federico Perini of the [FITPACK](http://www.netlib.org/dierckx) package for curve and surface fitting by Paul Dierckx

[fstats](https://github.com/jchristopherson/fstats): modern statistical library containing routines for computing basic statistical properties, hypothesis testing, regression, special functions, and even experimental design, by Jason Christopherson

[gslib2.0: Geostatistical Software Library](https://github.com/exepulveda/gslib2.0): aims to create a modern version of the original GSLIB source code, by exepulveda

[lib_statistics](https://github.com/sebastiandyrda/lib_statistics): code for logistic regression, by Alan Miller, packaged for FPM by Sebastian Dyrda

[M_datapac](https://github.com/urbanjost/M_datapac): NIST [DATAPAC](https://www.nist.gov/itl/sed/datapac) package modularized and made available as an fpm(1) package, by urbanjost, original code by James Filliben. There are routines for computing various probability functions.

[peaks](https://github.com/jchristopherson/peaks): peak detection library meant to locate peaks and valleys in a signal, by Jason Christopherson. This library works on both smooth data and on noisy data where other routines, especially those that rely upon derivatives, have difficulties.

## Strings

[enclose](https://github.com/degawa/enclose): procedures for enclosing a string in brackets, by Tomohiro Degawa

[fortran202x_split](https://github.com/milancurcic/fortran202x_split): Fortran implementation of the Fortran 202X split intrinsic subroutine, by Milan Curcic and Sebastian Ehlert

[fortran-shlex](https://github.com/perazz/fortran-shlex): port by Federico Perini of Python's [shlex](https://docs.python.org/3/library/shlex.html) shell-like lexer. The interface comes with two functions, `split` which parses a command-like string and returns an array of allocatable character strings; and `shlex` that performs the same, but returns a list of `type(shlex_token)` tokens.

[Fortran-String-to-Real](https://github.com/Carltoffel/Fortran-String-to-Real): converts strings to reals without using an internal read, by Carltoffel. [Fortran-String-to-Num](https://github.com/jalvesz/Fortran-String-to-Num) is a fork by jalvesz that aims for further improvements on the ASCII to numerical data conversion.

[fsys](https://github.com/jchristopherson/fsys): library by Jason Christopherson containing system operations and supporting types: `string`, similar to the `iso_varying_string`, but with a few differences and a few additional operations, and `string_builder`, a type that allows concatenating strings while minimizing memory reallocation operations, that behaves similarily to the .NET `StringBuilder` class

[iso_varying_string](https://github.com/everythingfunctional/iso_varying_string): implementation of the ISO_VARYING_STRING module as defined in the ISO standard, by Brad Richardson

[M_io](https://github.com/urbanjost/M_io): collection of procedures that create a simple interface for common I/O tasks not conveniently done with intrinsic I/O procedures, by urbanjost

[M_strings](https://github.com/urbanjost/M_strings): modules for processing strings. Routines for parsing, tokenizing, changing case, substituting new strings for substrings, locating strings with simple wildcard expressions, removing tabs and line terminators and other string manipulations are included

[parff](https://github.com/everythingfunctional/parff): functional style parser combinator library, by Brad Richardson and Patrick Raynaud. By using a library like this, it is possible to implement parsers for complex formats by composing independent little pieces. 

[ryu_fortran](https://github.com/St-Maxwell/ryu_fortran): Ryu algorithm which converts floating point numbers to decimal strings, by St Maxwell. It is more effective than internal file approach. This implementation is based on the Scala version of Ryu.

[scanner](https://github.com/freevryheid/scanner): text scanner for parsing, by Andre Smit

[strff](https://github.com/everythingfunctional/strff): library of string functions, by Brad Richardson

[StringiFor](https://github.com/szaghi/StringiFor): Strings Fortran Manipulator with steroids, by szaghi

[strith](https://github.com/degawa/strith): converts a variable representing a long integer into a string by performing arithmetic operations on numbers in strings, by Tomohiro Degawa

[utf8-f](https://github.com/St-Maxwell/utf8-f): UTF-8 manipulation, by St-Maxwell. The underlying data in a utf8_string object is a deferred-length string of <br>`character(len=:, kind=c_char)` type.

## Time Series

[fortsa](https://github.com/zoziha/fortsa): univariate time series analysis and ARIMA modeling package, by zoziha

[spectrum](https://github.com/jchristopherson/spectrum): library containing signal analysis routines with a focus towards spectral routines, by Jason Christopherson

[wavepack](https://github.com/zoziha/wavepack): computes the wavelet transform of a time series, and significance levels, by zoziha

## Unclassified

[DAGLIB](https://github.com/jacobwilliams/daglib): modern Fortran module for creating and manipulating directed acyclic graphs (DAGs), by Jacob Williams and Damian Rouson. It includes a toposort feature, and also the ability to generate files in the GraphViz "dot" notation.

[strengthcalc](https://github.com/piotrbajdek/strengthcalc): strengthcalc employs mathematical formulae from Mayhew et al. (1992) and Wathen (1994) to estimate the maximum weight one can lift in a single repetition of a physical exercise (known as 1RM: one repetition maximum), by Piotr Bajdek

## Unit Testing

[ForUnitTest](https://github.com/gha3mi/forunittest): simple, object-oriented unit testing framework, by Seyed Ali Ghasemi.

[ForDebug](https://github.com/gha3mi/fordebug): library designed for debugging Fortran code, especially within pure procedures, by Seyed Ali Ghasemi

[fortran_test_helper](https://github.com/jchristopherson/fortran_test_helper): library to provide assistance to testing, by Jason Christopherson

[Fortran Unit Testing Objects (Fortuno)](https://github.com/aradi/fortuno): flexible and extensible Fortran unit testing framework for testing serial, MPI-parallelized and coarray-parallelized applications, by Bálint Aradi

[M_framework](https://github.com/urbanjost/M_framework): aggregate of Fortran modules useful for creating terminal messages, comparing expected values to results, writing logfiles and playback journals and performing unit tests for Fortran, by urbanjost

[par-funnel](https://github.com/degawa/par-funnel): unit test parameterizer using namelist, by Tomohiro Degawa. Par-funnel is not a unit test framework but is intended to be used with other unit test frameworks.

[test-drive](https://github.com/fortran-lang/test-drive): lightweight, procedural unit testing framework based on nothing but standard Fortran, by Sebastian Ehlert and Jeremie Vandenplas. Integration with meson, cmake and Fortran package manager (fpm) is available.

[Veggies](https://github.com/everythingfunctional/veggies): unit testing framework written using functional programming principles, with the ability to test parallel code, by Brad Richardson et al. As many of its procedures as possible are marked with the pure keyword, while still allowing the framework to test impure code. 

## Web Programming

[ForOpenAI](https://github.com/gha3mi/foropenai): library to access the OpenAI API, by Seyed Ali Ghasemi

[ForCompile](https://github.com/gha3mi/forcompile): library to access the Compiler Explorer API, by Seyed Ali Ghasemi

[github-org-analyzer](https://github.com/rajkumardongre/github-org-analyzer): procedures to analyze GitHub organizations and retrieve valuable information about their repositories, by Rajkumar Dongre. By leveraging the power of the http-client package, this analyzer fetches data from the GitHub API to generate insightful reports.

[http-client](https://github.com/fortran-lang/http-client): HTTP client library, by Rajkumar Dongre and Milan Curcic

## XML

[FoXy](https://github.com/Fortran-FOSS-Programmers/FoXy): XML parser, from Fortran-FOSS-Programmers

time elapsed (s): 511.44
