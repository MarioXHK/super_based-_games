# Recommended imports for all problems
# Some problems may require more
import sys
import math
import string
cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    V = float(input())
    X = float(input())
    if X/V <= 1:
        print("SWERVE")
    elif X/V <= 5:
        print("BRAKE")
    else:
        print("SAFE")