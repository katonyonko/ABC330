import io
import sys
import pdb
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations, accumulate
from heapq import heappush, heappop
sys.setrecursionlimit(10**6)
from bisect import bisect_right, bisect_left
from math import gcd
import math

_INPUT = """\
6
6 5
2 0
5 2
0 3
3 2
3 4
1 5
4 400000000000000
1000000000 1000000000
1000000000 1000000000
1000000000 1000000000
1000000000 1000000000
10 998244353
489733278 189351894
861289363 30208889
450668761 133103889
306319121 739571083
409648209 922270934
930832199 304946211
358683490 923133355
369972904 539399938
915030547 735320146
386219602 277971612
"""
# x=277971612
# m=488281249
# y=[30208889, 133103889, 189351894, 277971612, 304946211, 539399938, 735320146, 739571083, 922270934, 923133355]
# z=[x-y[i] if x>y[i] else y[i]-x-m if y[i]>x+m else 0 for i in range(len(y))]
# print(z,sum(z))
def solve(test):
  N,K=map(int,input().split())
  A=[list(map(int,input().split())) for _ in range(N)]
  X=sorted([a[0] for a in A])
  X2=sorted([-a[0] for a in A])
  Y=sorted([a[1] for a in A])
  Y2=sorted([-a[1] for a in A])
  aX=[0]+list(accumulate(X))
  aX2=[0]+list(accumulate(X2))
  aY=[0]+list(accumulate(Y))
  aY2=[0]+list(accumulate(Y2))
  l,r=-1,10**10
  # print(Y)
  while r-l>1:
    m=(l+r)//2
    now=0
    tmpx=10**20
    for i in range(N):
      while now<N and X[now]<=X[i]+m:
        now+=1
      tmpx=min(tmpx,X[i]*i-aX[i]+(aX[-1]-aX[now])-(N-now)*(X[i]+m))
    now=0
    for i in range(N):
      while now<N and X2[now]<=X2[i]+m:
        now+=1
      tmpx=min(tmpx,X2[i]*i-aX2[i]+(aX2[-1]-aX2[now])-(N-now)*(X2[i]+m))
    now=0
    tmpy=10**20
    for i in range(N):
      while now<N and Y[now]<=Y[i]+m:
        now+=1
      tmpy=min(tmpy,Y[i]*i-aY[i]+(aY[-1]-aY[now])-(N-now)*(Y[i]+m))
      # if m==488281249: print(Y[i]*i-aY[i]+(aY[-1]-aY[now])-(N-now)*(Y[i]+m),now)
    now=0
    for i in range(N):
      while now<N and Y2[now]<=Y2[i]+m:
        now+=1
      tmpy=min(tmpy,Y2[i]*i-aY2[i]+(aY2[-1]-aY2[now])-(N-now)*(Y2[i]+m))
    cnt=tmpx+tmpy
    if cnt<=K:
      r=m
    else:
      l=m
    # print(l,r,cnt<=K,tmpx,tmpy,cnt)
  ans=r
  if test==0:
    print(ans)
  else:
    return None

def random_input():
  from random import randint,shuffle
  N=randint(1,10)
  M=randint(1,N)
  A=list(range(1,M+1))+[randint(1,M) for _ in range(N-M)]
  shuffle(A)
  return (" ".join(map(str, [N,M]))+"\n"+" ".join(map(str, A))+"\n")*3

def simple_solve():
  return []

def main(test):
  if test==0:
    solve(0)
  elif test==1:
    sys.stdin = io.StringIO(_INPUT)
    case_no=int(input())
    for _ in range(case_no):
      solve(0)
  else:
    for i in range(1000):
      sys.stdin = io.StringIO(random_input())
      x=solve(1)
      y=simple_solve()
      if x!=y:
        print(i,x,y)
        print(*[line for line in sys.stdin],sep='')
        break

#0:提出用、1:与えられたテスト用、2:ストレステスト用
main(0)