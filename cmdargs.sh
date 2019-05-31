#!/bin/bash

echo '$0 is ' $0
echo -n "basename is: "
basename $0
echo '$1 is ' $1
echo '$2 is ' $2
echo '$9 is ' $9
echo '$10 is ' ${10}
echo '$# is ' $#
echo '$* is ' $*
echo '$@ is ' $@

echo 'Processing $*'
for arg in "$*"
do
  echo "Argument is: " $arg
done

echo 'Processing $@'
for arg in "$@"
do
  echo "Argument is: " $arg
done
