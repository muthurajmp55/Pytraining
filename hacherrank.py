#!/bin/python3

import sys


def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    ao=0
    bo=0
    in1={}
    for i in range(3):
        k = locals()
        in1["a"+str(i)]=k["a"+str(i)]
        in1["b"+ str(i)] = k["b"+ str(i)]
        if k["a"+str(i)] > k["b"+ str(i)] :
            ao=ao+1
        if k["a"+str(i)] < k["b"+ str(i)] :
            bo=bo+1
    arr=[ao,bo]
    return arr



a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print(" ".join(map(str, result)))

