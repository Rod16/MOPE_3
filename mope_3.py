from random import *
import numpy as np
import scipy.stats
x1min = 10
x1max = 50
x2min = -20
x2max = 60
x3min = -20
x3max = 20
xAvmax = x1max+x2max+x3max/3
xAvmin = x1min+x2min+x3min/3
ymax = int(200+xAvmax)
ymin = int(200+xAvmin)


print("Y max= ",round(ymax,2))
print("Y min= ",round(ymin,2), "\n")


print("Кодовані значення X:")
print("{:<5} {:<5} {:<5} {:<5}".format("№","X1","X2","X3"))
X11 = ["-1", "-1", "+1", "+1"]
X22 = ["-1", "+1", "-1", "+1"]
X33 = ["-1", "+1", "+1", "-1"]
for i in range(4):
    print("{:<5} {:<5} {:<5} {:<5}".format(i+1,X11[i],X22[i],X33[i]))
print("\n")

print("Матриця для m=3")
print("{:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5}".format("№","X1","X2","X3","Y1","Y2","Y3"))
X1 = [x1min, x1min, x1max, x1max]
X2 = [x2min, x2max, x2min, x2max]
X3 = [x3min, x3max, x3max, x3min]
Y1 = [randint(round(ymin,2),round(ymax,2)) for i in range(4)]
Y2 = [randint(round(ymin,2),round(ymax,2)) for i in range(4)]
Y3 = [randint(round(ymin,2),round(ymax,2)) for i in range(4)]
for i in range(4):
    print("{:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5}".format(i+1,X1[i],X2[i],X3[i],Y1[i],Y2[i],Y3[i]))
print("\n")

print("Середнє значення відгуків функцій по кожному з рядків:")
y1av1 = (Y1[0]+Y2[0]+Y3[0])/3
y2av2 = (Y1[1]+Y2[1]+Y3[1])/3
y3av3 = (Y1[2]+Y2[2]+Y3[2])/3
y4av4 = (Y1[3]+Y2[3]+Y3[3])/3

mx1 = sum(X1)/4
mx2 = sum(X2)/4
mx3 = sum(X3)/4

my = (y1av1 + y2av2 + y3av3 + y4av4)/4

a1 = (X1[0]*y1av1 + X1[1]*y2av2 + X1[2]*y3av3 + X1[3]*y4av4)/4
a2 = (X2[0]*y1av1 + X2[1]*y2av2 + X2[2]*y3av3 + X2[3]*y4av4)/4
a3 = (X3[0]*y1av1 + X3[1]*y2av2 + X3[2]*y3av3 + X3[3]*y4av4)/4

a11 = (X1[0]*X1[0] + X1[1]*X1[1] + X1[2]*X1[2] + X1[3]*X1[3])/4
a22 = (X2[0]*X2[0] + X2[1]*X2[1] + X2[2]*X2[2] + X2[3]*X2[3])/4
a33 = (X3[0]*X3[0] + X3[1]*X3[1] + X3[2]*X3[2] + X3[3]*X3[3])/4
a12 = a21 = (X1[0]*X2[0] + X1[1]*X2[1] + X1[2]*X2[2] + X1[3]*X2[3])/4
a13 = a31 = (X1[0]*X3[0] + X1[1]*X3[1] + X1[2]*X3[2] + X1[3]*X3[3])/4
a23 = a32 = (X2[0]*X3[0] + X2[1]*X3[1] + X2[2]*X3[2] + X2[3]*X3[3])/4

b01 = np.array([[my, mx1, mx2, mx3], [a1, a11, a12, a13], [a2, a12, a22, a32], [a3, a13, a23, a33]])
b02 = np.array([[1, mx1, mx2, mx3], [mx1, a11, a12, a13], [mx2, a12, a22, a32], [mx3, a13, a23, a33]])
b0 = np.linalg.det(b01)/np.linalg.det(b02)

b11 = np.array([[1, my, mx2, mx3], [mx1, a1, a12, a13], [mx2, a2, a22, a32], [mx3, a3, a23, a33]])
b12 = np.array([[1, mx1, mx2, mx3], [mx1, a11, a12, a13], [mx2, a12, a22, a32], [mx3, a13, a23, a33]])
b1 = np.linalg.det(b11)/np.linalg.det(b12)

b21 = np.array([[1, mx1, my, mx3], [mx1, a11, a1, a13], [mx2, a12, a2, a32], [mx3, a13, a3, a33]])
b22 = np.array([[1, mx1, mx2, mx3], [mx1, a11, a12, a13], [mx2, a12, a22, a32], [mx3, a13, a23, a33]])
b2 = np.linalg.det(b21)/np.linalg.det(b22)

b31 = np.array([[1, mx1, mx2, my], [mx1, a11, a12, a1], [mx2, a12, a22, a2], [mx3, a13, a23, a3]])
b32 = np.array([[1, mx1, mx2, mx3], [mx1, a11, a12, a13], [mx2, a12, a22, a32], [mx3, a13, a23, a33]])
b3 = np.linalg.det(b31)/np.linalg.det(b32)

print("y1av1="+str(round(b0 + b1*X1[0] + b2*X2[0] + b3*X3[0],2))+"="+ str(round(y1av1,2)))
print("y2av2="+str(round(b0 + b1*X1[1] + b2*X2[1] + b3*X3[1],2))+"="+ str(round(y2av2,2)))
print("y3av3="+str(round(b0 + b1*X1[2] + b2*X2[2] + b3*X3[2],2))+"="+ str(round(y3av3,2)))
print("y4av4="+str(round(b0 + b1*X1[3] + b2*X2[3] + b3*X3[3],2))+"="+ str(round(y4av4,2)))
print("Значення збігаються\n")

print("Дисперсія по рядках:")
d1 = ((Y1[0] - y1av1)**2 + (Y2[0] - y2av2)**2 + (Y3[0] - y3av3)**2)/3
d2 = ((Y1[1] - y1av1)**2 + (Y2[1] - y2av2)**2 + (Y3[1] - y3av3)**2)/3
d3 = ((Y1[2] - y1av1)**2 + (Y2[2] - y2av2)**2 + (Y3[2] - y3av3)**2)/3
d4 = ((Y1[3] - y1av1)**2 + (Y2[3] - y2av2)**2 + (Y3[3] - y3av3)**2)/3
print("d1=", round(d1,2),"d2=", round(d2,2),"d3=", round(d3,2),"d4=", round(d4,2))


cohran = {1: 0.9065, 2: 0.7679, 3: 0.6841, 4: 0.6287, 5: 0.5892, 6: 0.5598, 7: 0.5365, 8: 0.5175, 9: 0.5017,
                 10: 0.4884, range(11, 17): 0.4366, range(17, 37): 0.3720, range(37, 145): 0.3093}

dlist = [d1, d2, d3, d4]

m = 3
Gp = max(dlist)/sum(dlist)
print("f1 = 2, f2 = 4")
q=0.05
p=1-q

for i in range(m, 20, 1):
    f1 = m-1
    f2 = N = 4
    print("Gp = ",Gp)
    for key in cohran.keys():
        if f1 == key:
            value = cohran.get(key)
            break
    else:
        value = 2500
    print("Gt = ",value)

    if Gp < value:
        print("Gp < Gt, дисперсія є однорідною за критерієм Кохрена при m = ", m)
        break
    else:
        print("Gp > Gt, дисперсія є неоднорідною за критерієм Кохрена при m = ", m)
        m = m + 1
        print("\n")
        continue
print("\n")
print("Критерій Стьюдента:")
sb = sum(dlist)/N
ssbs = sb/N*m
sbs = ssbs**0.5

beta0 = (y1av1*1 + y2av2*1 + y3av3*1 + y4av4*1)/4
beta1 = (y1av1*(-1) + y2av2*(-1) + y3av3*1 + y4av4*1)/4
beta2 = (y1av1*(-1) + y2av2*1 + y3av3*(-1) + y4av4*1)/4
beta3 = (y1av1*(-1) + y2av2*1 + y3av3*1 + y4av4*(-1))/4

t0 = abs(beta0)/sbs
t1 = abs(beta1)/sbs
t2 = abs(beta2)/sbs
t3 = abs(beta3)/sbs


f3 = f1*f2
ttabl = scipy.stats.t.ppf((1 + (1 - q)) / 2, f3)
print("tтабл = ", ttabl)
print("f3 = f1*f2 = 8")
print("ts: ",t0,t1,t2,t3)
if (t0<ttabl):
    print("t0<ttabl, b0 не значимий")
    b0=0
if (t1<ttabl):
    print("t1<ttabl, b1 не значимий")
    b1=0
if (t2<ttabl):
    print("t2<ttabl, b2 не значимий")
    b2=0
if (t3<ttabl):
    print("t3<ttabl, b3 не значимий")
    b3=0

yy1 = b0 + b1*x1min + b2*x2min + b3*x3min
yy2 = b0 + b1*x1min + b2*x2max + b3*x3max
yy3 = b0 + b1*x1max + b2*x2min + b3*x3max
yy4 = b0 + b1*x1max + b2*x2max + b3*x3min
print("\n")
print("Критерій Фішера:")
d = 2
print(d," значимих коефіцієнтів")
f4 = N - d
print("f4 = ", f4)
print("d1=", round(d1, 2), "d2=", round(d2, 2), "d3=", round(d3, 2), "d4=", round(d4, 2), "d5=", round(sb, 2))
sad = ((yy1 - y1av1)**2 + (yy2 - y2av2)**2 + (yy3 - y3av3)**2 + (yy4 - y4av4)**2)*(m/(N-d))
Fp = sad/sb
print("Fp=", round(Fp,2))
Ft=scipy.stats.f.ppf(p, f4, f3)
print("Ft = ",Ft)
if Fp>Ft:
    print("Fp> Ft, рівняння не є адекватним оригіналу")

else:
    print("Fp< Ft, рівняння є адекватним оригіналу")
