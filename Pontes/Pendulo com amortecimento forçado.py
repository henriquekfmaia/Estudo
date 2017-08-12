import numpy as np
import scipy.interpolate as interp
import pylab as pyl

a, b = 0, 1

w1 = 1
w2 = 1
a1 = np.pi/2
a2 = np.pi*3/2
p = 0.1

Wx = []
Wy = []

Ax = []
Ay = []

count = 0

def f1(omega):
    return omega

def f2(teta):
    return -(9.81*np.sin(teta))

for i in range(0,100):
    if (count%10 == 0):
        print np.sin(0)
    count = count+1
    w1 = w1 + p*f2(a1)
    w2 = w2 + p*f2(a2)
    a1 = a1 + p*f1(w1)
    a2 = a2 + p*f1(w2)
    Wx.append(w1)
    Wy.append(w2)
    Ax.append(a1)
    Ay.append(a2)



margemh = (np.amax(Wx) - np.amin(Wx))/20
margemv = (np.amax(Wy) - np.amin(Wy))/20

pyl.plot(Wx, Wy, 'b-', label = 'W')
#pyl.plot(Ax, Ay, 'r--', label = 'A')
pyl.title('W e A')
pyl.legend(loc='lower left')
pyl.grid(True)
pyl.xticks((a,b))
pyl.axhline(y=0, color='k')
pyl.axvline(x=0, color='k')
#pyl.axis([np.amin(Wx)-margemh, np.amax(Wx)+margemh, np.amin(Wy)-margemv, np.amax(Wy)+margemv])
pyl.show()
pyl.close()
