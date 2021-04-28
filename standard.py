import sys
from math import (floor,ceil,factorial as fact,pow,log2,log10,log,pi as PI)
testcases=True
# testcases=False
MOD=int(pow(10,9)+7)
################################ Main Code ################################

def solve():
    l=linput()
    print()






################################### END ###################################
def isprime(n):
    if(n<=1):return False
    if(n<=3):return True
    if(n%2==0 or n%3==0):return False
    i=5
    while(i*i<=n):
        if(n%i==0 or n%(i+2)==0):return False
        i=i+6
    return True
    
def sortbyindex(a,ind,rev=False):
    return sorted(a,key=lambda a:a[ind],reverse=rev)

def linput():
    return list(map(int,sys.stdin.readline().strip().split()))
    

__=1
if(testcases):
    __=int(input())
for _ in range(__):
    solve()
    

'''
Python Template:
by
🅼🆄🅺🅴🆂🅷003

https://github.com/1-mukesh-1/CP-Templates
'''
