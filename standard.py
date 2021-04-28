import sys
from math import floor,ceil,factorial as fact,pow,log2,log10,log

def isprime(n):
    if(n<=1):return False
    if(n<=3):return True
    if(n%2==0 or n%3==0):return False
    i=5
    while(i*i<=n):
        if(n%i==0 or n%(i+2)==0):return False
        i=i+6
    return True
def linput():
    return list(map(int,sys.stdin.readline().strip().split()))


for _ in range(int(input())):
    l=linput()
    print(l)
    print(isprime(13))





'''
Python Template:
by
🅼🆄🅺🅴🆂🅷003

https://github.com/1-mukesh-1/CP-Templates
'''
