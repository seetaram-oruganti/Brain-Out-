 def toh(n,src, dest, temp):
    if(n==0):
        return
    toh(n-1, src, temp, dest )
    print("Move {} from {} to {}".format(n, src, dest))
    toh(n-1, temp, dest, src)


for _ in range(int(input())):
    n = int(input())
    src = "A"
    dest = "C"
    temp = "B"
    print(2**n-1)    # no.of shifts required 
    toh(n,src, dest, temp)
    
    
