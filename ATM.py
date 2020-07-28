l = input().split()

A = int(l[0])

B = float(l[1])

if((A<B)and(A%5==0)and (A<=2000)):
    print("%.2f"%(B-A-0.5))
if((B>A)or(A==B)):
    print("%.2f"%(B))
