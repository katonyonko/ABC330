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
8 5
2 0 2 2 1 1 2 5
4 3
4 4
6 3
8 1000000000
2 1
"""

class SegTree:
    X_unit = 1 << 30
    X_f = min
 
    def __init__(self, N):
        self.N = N
        self.X = [self.X_unit] * (N + N)
 
    def build(self, seq):
        for i, x in enumerate(seq, self.N):
            self.X[i] = x
        for i in range(self.N - 1, 0, -1):
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])
 
    def set_val(self, i, x):
        i += self.N
        self.X[i] = x
        while i > 1:
            i >>= 1
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])
 
    def fold(self, L, R):
        L += self.N
        R += self.N
        vL = self.X_unit
        vR = self.X_unit
        while L < R:
            if L & 1:
                vL = self.X_f(vL, self.X[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.X_f(self.X[R], vR)
            L >>= 1
            R >>= 1
        return self.X_f(vL, vR)

    def get_val(self,idx):
        return self.X[idx+self.N]

def solve(test):
  N,Q=map(int, input().split())
  A=list(map(int, input().split()))
  st=SegTree(2*10**5+1)
  st.build([i for i in range(2*10**5+1)])
  cnt=[0]*(2*10**5+1)
  for i in range(N):
    if A[i]<=2*10**5:
      cnt[A[i]]+=1
      if cnt[A[i]]==1: st.set_val(A[i],st.X_unit)
  for i in range(Q):
    id,x=map(int, input().split())
    if A[id-1]<=2*10**5:
      cnt[A[id-1]]-=1
      if cnt[A[id-1]]==0:
        st.set_val(A[id-1],A[id-1])
    A[id-1]=x
    if A[id-1]<=2*10**5:
      cnt[A[id-1]]+=1
      if cnt[A[id-1]]==1: st.set_val(A[id-1],st.X_unit)
    print(st.fold(0,2*10**5+1))

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