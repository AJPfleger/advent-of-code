# Set up and use Z3 in Octave

(Created with assistance of ChatGPT 3.5)

## Install Z3

Download and install Z3 from the official Z3 GitHub repository: https://github.com/Z3Prover/z3

```shell
python3.12 -m venv venv
source venv/bin/activate
git clone https://github.com/Z3Prover/z3.git
cd z3

python scripts/mk_make.py --prefix=/opt/z3
cd build
make
make install
```

Set library path:

```shell
export DYLD_LIBRARY_PATH=/opt/z3/lib:$DYLD_LIBRARY_PATH
```

## Compile MEX File

Compile the MEX file using the `mkoctfile` command:

```shell
mkoctfile --mex -I/opt/z3/include -L/opt/z3/lib -R/opt/z3/lib -lz3 mexZ3solver.cpp
```
