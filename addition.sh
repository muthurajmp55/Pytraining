#!/bin/bash

echo -n "Enter the first number :"

read n1

echo -n "Enter the second number :"

read n2

echo -n "The sum of $n1 and $n2 is: "
expr $n1 + $n2
