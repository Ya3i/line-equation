p1=[1,1]
p2=[2,4]

y0=p2[1]-p1[1]
x0=p1[0]-p2[0]

c=p1[1]*p2[0]-p1[0]*p2[1]
if(x0>0):
    print(f"{y0}x+{x0}y = {c}")
else:
    print(f"{y0}x{x0}y = {c}")