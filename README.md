**This is the outline of an old attempt ot write a package manage for Fortran.
It was eventually decided to instead write a set of packages for the existing 
[spack](https://spack.readthedocs.io/en/latest/) package manager. These packages 
can be found in their 
[own repository](https://github.com/Fortran-FOSS-Programmers/FLATPack). This 
repository is kept as a record of previous work.**

# Fortran Library, Application, and Tool Packaging (FLATPack)

This is a (proposed) project to write a package manager for Fortran projects.
This would be similar to `pip`/PyPI, `gem`, or `npm` and would allow
dependencies to be specified between packages.


## Motivation
For the most part, the benefits to such a system should be obvious; after all,
such systems exist for many other languages. Three, in particular, are outlined
below.

### Convenience
If a project depends on another library, then that must be installed by the
user. If the user has root permissions and the library is in a distribution's
repositories, then this is trivial. However, even then, this would only allow
the package to be used with a particular compiler (presumably the system's
default version of gfortran). Otherwise, the user will have to compile the
software themselves, and ensure that all of its dependencies are also met.

### Efficiency
If someone writes a library to do something (such as
[handle command-line arguments](https://github.com/szaghi/FLAP) or
[parse JSON](https://github.com/jacobwilliams/json-fortran)) then, for the
most part, anyone using that library in their software will have to include
a copy of it there. This increases the size of the software, makes the library
appear to be less of a standard, and means that the latest version of a
library may not be the one distributed.

### Compilers
Due to the lack of an ABI for Fortran, one compiler can not use the version of
a library produced by another. While the near monopoly of gcc/g++ ameliorates
this issue for C/C++ libraries, a more diverse range of compilers is used
for Fortran. A package manager would provide an opportunity to manage
different binaries for different compilers and versions of compilers.


## Approach
This provides only a basic sketch of how such a package manager would be
implemented. Everything here would be open to discussion.

- Source code for the various packages would be hosted on GitHub in its
  own repository. Ideally this could be achieved in such a way that existing
  repositories would require no changes except, perhaps, the inclusion of an
  extra configuration file.
- A database would contain information on each package. This information would
  include dependencies (and required versions of dependencies), supported
  compilers, location of the GitHub repository containing the source code, the
  commits for the different versions of the package, and compilation
  instructions.
- This database could potentially take the form of a git repository containing
  JSON (or XML, YAML, pickle, or other data files) for each package, which
  FLATPack users could then clone locally and push changes to with their own
  packages. FLATPack could then add files (whose extensions would be in
  .gitignore) describing which packages had been installed, what versions, and
  for what compiler.
- The user would install packages with some variation of the command
  `flatpack install <package-name>`. FLATPack would then clone the source
  code from the specified git repository and compile it according to
  instuctions. If any dependencies were required, then these would be insalled
  first, in a recursive fashion.
- Options specifying where to perform compilation, what compiler to use, whether
  to keep source and object files once compilation has been completed, where
  to place binaries, and where to place header and module files could be
  set/changed from their defaults in a `.flatpack` file in the home directory.
  A command-line option could be provided to specify an alternative file
  (specifying how to go about using a different compiler, for example) and
  these various options could be over-ridden from the command-line.
- A different way to achieve the effects being able to specify a different
  settings file would be to use something like Python's
  virtualenv system

I envision the implementation being done in Python as (next to Fortran, which
is clearly unsuitable) that is the language which I am most comfortable with.
There is the further advantage that there are excellent Python libraries
available for interacting with JSON (or XML or whatever structured-data
approach we might choose), git, and the wider system generally.

