from cmath import sqrt
import math
def solve_quadratic (a, b, c):

    disc=b**2 - 4*a*c 
    if disc <0: 
        return None
    if disc==0:
        return -b / 2*a
    x1=(-b+math.sqrt (disc))/2*a
    x2=(-b-math.sqrt(disc))/2*a
    return (x1,x2)
print (solve_quadratic(1,-5,6))



print (solve_quadratic(1,4,4))


print (solve_quadratic(1,0,1))




    
        

print (solve_quadratic (1,2,1))
     
