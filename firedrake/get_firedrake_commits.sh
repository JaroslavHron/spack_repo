#!/usr/bin/bash
mkdir tmp
pushd tmp

#for i in `grep -l Firedrake_ ../karlin/firedrake/packages/*/*.py` ; do grep git ${i} ; done

for g in 'https://github.com/coneoproject/COFFEE' 'https://github.com/firedrakeproject/fiat' 'https://github.com/FInAT/FInAT' 'https://github.com/firedrakeproject/firedrake' "https://github.com/firedrakeproject/loopy" "https://github.com/firedrakeproject/petsc" 'https://github.com/OP2/PyOP2' "https://github.com/firedrakeproject/petsc4py" "https://github.com/firedrakeproject/slepc4py" "https://github.com/firedrakeproject/slepc" 'https://github.com/firedrakeproject/tsfc' 'https://github.com/firedrakeproject/ufl'
do
git clone ${g}
done

for g in 'COFFEE' 'fiat' 'FInAT' 'firedrake' "loopy" "petsc" 'PyOP2' "petsc4py" "slepc4py" "slepc" 'tsfc' 'ufl'
do
pushd ${g} && git pull && popd
done

date="Oct 18 2019"

for i in loopy petsc petsc4py slepc slepc4py
do
h=`cd ${i} && git rev-list -1 --before="${date}" firedrake`
echo ${i} ${h}
done

# branch firedrake


for i in COFFEE fiat FInAT firedrake PyOP2 tsfc ufl
do
h=`cd ${i} && git rev-list -1 --before="${date}" master`
echo ${i} ${h}
done

# branch master
