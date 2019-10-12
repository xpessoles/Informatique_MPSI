# for i in range(1,11):
#     print(i,'x 9 =',i*9)
#     #print(str(i)+'x'+str(9)+'='+str(i*9))

# f=1
# for i in range(2,17):
#     f=f*i
#     print(f//i,'x',i,'=',f)
    
    
def f(x):
    if -4<=x<=-2:
        return 2
    elif -2<x<=0:
        return -x
    elif 0<x<=4:
        return 0
    else:
        print('fonction non définie')
        
        
import matplotlib.pyplot as plt
x = [1, 3, 4, 2]
y = [2, 1, 4, 2]
plt.clf()
plt.plot(x,y)
plt.savefig("ex_base_01.png")