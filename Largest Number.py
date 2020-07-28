"""

Given a list of non negative integers,
arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

"""

class Solution:
    # @param A : tuple of integers
    
    # @return a strings
    def largestNumber(self, A):
        n = len(A)
        A = list(A)
        self.merges(A, 0, n-1)
        s = ""
        
        for i in A:
            s = s+str(i)
        if(0 == int(s)):
            return 0
        return s
        
    def merges(self, ar,l,h):
        if(l==h):
            return
        mid=(l+h)//2
        self.merges(ar,l,mid)
        self.merges(ar,mid+1,h)
        self.merge(ar,l,mid,h)
    
    def merge(self,ar,l,mid,h):
        p1 = l
        p2 = mid+1
        k = 0
        size = h-l+1
        temp = [0]*size
        while((p1<=mid) and (p2<=h)):
            s1 = str(ar[p1])+str(ar[p2])
            s2 = str(ar[p2])+str(ar[p1])
            if(int(s2)>int(s1)):
                temp[k] = ar[p2]
                k = k+1
                p2 = p2+1
            else:
                temp[k] = ar[p1]
                k = k+1
                p1 = p1+1
                
        while(p1<=mid):
            temp[k] = ar[p1]
            k = k+1
            p1 = p1+1
            
        while(p2<=h):
            temp[k] = ar[p2]
            k = k+1
            p2 = p2+1
        for i in range(l,h+1):
            ar[i] = temp[i-l]
        
