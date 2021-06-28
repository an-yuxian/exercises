import math
g=9.8
L=5.48
m=6426
w=11000/60   
c=10**4

def sqrt(a):
    return math.sqrt(a)

def amp(w,k):
    K=m*g*L+k*L
    return (sqrt((c**2)*(w**2)+(K-m*w)**2))/((K-m*w)**2+(c**2)*(w**2))

for k in [2,3,4,5,6,7]:
    print("When k="+str(k)+" and ω="+str(w*60)+"(RPM),the amplitude:"+str(amp(w,k*10**10)))

