import numpy as np
class gauss:
    def __init__(self,A,b,eps):
        self.A=A
        self.b=b
        self.eps=eps
        self.n=A.shape[0]
    def swap_row(self,k,u):
        self.A[k][k:self.n],self.A[u][k:self.n]=self.A[u][k:self.n],self.A[k][k:self.n].copy()
        self.b[k],self.b[u]=self.b[u],self.b[k]
    def elimination(self,k):
        for i in range(k+1,self.n):
            m=self.A[i][k]/self.A[k][k]
            self.A[i][i:]-=m*self.A[k][i:]
            self.b[i]-=m*self.b[k]
    def back(self):
        self.b[self.n-1]/=self.A[self.n-1][self.n-1]
        for i in range(self.n-2,-1,-1):
            self.b[i]=(self.b[i]-np.sum(self.A[i][i+1:]*self.b[i+1:]))/self.A[i][i]
        return self.b
    def solve(self):
        for  k in range(self.n-1):
            u=self.maxk(k,k)
            if abs(self.A[u][k])<self.eps:
                print("无解")
                return 
            if u!=k:
                self.swap_row(k,u)
#             print(self.A)
            self.elimination(k)
#             print(self.A)
        if self.A[self.n-1][self.n-1]==0:
            print('无解')
            return
        self.back()
    def maxk(self,u,k):
        ix=k
        pivot=self.A[k][k]
        for i in range(k,self.n):
            if abs(pivot)<=abs(self.A[i][k]):
                pivot=self.A[i][k]
                ix=i
        return ix