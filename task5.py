import math
import sys
def autotest():
    if(autotest1() and autotest2() and autotest3()) == 1:
        return 0
    else:
        return 1
def autotest1():
    number = [0,0,1,3,4,1,-3,-4,1]
    nr1 = 2.5
    nr2 = 2.5
    nr3 = 2.5
    cntrl = func(number)
    if (nr1 == cntrl[0]) and (nr2 == cntrl[1]) and (nr3 == cntrl[2]):
        print("Autotest1 passed")
        return 1
    else:
        print("Autotest1 failed!!")
        return 0
def autotest2():
    number = [0,0,1,3,4,1,0.5,0,0.25,0,0,1]
    nr1 = 1
    nr2 = 4
    nr3 = 0.5
    nr4 = 1
    cntrl = func(number)
    if(nr1 == cntrl[0]) and (nr2 == cntrl[1]) and (nr3 == cntrl[2]) and(nr4 == cntrl[3]):
        print("Autotest2 passed")
        return 1
    else:
        print("Autotest2 failed")
        return 0
def autotest3():
    number = [0,0,1,0,0,1]
    nr1 = 1
    nr2 = 1
    cntrl = func(number)
    if(nr1 == cntrl[0]) and (nr2 == cntrl[1]):
        print("Autotest3 passed")
        return 1
    else:
        print("Autotest3 failed")
        return 0
def funcread(filename):
    number = []
    try:
        with open(filename,'r') as f:
            text = f.read()
            words = text.split()
        for b in words:
            try:
                number.append(float(b))
            except ValueError:
                print("Bad value")
                return [-1,-1]
        return func(number)
    except FileNotFoundError:
        print("Can't open the file")
        return [-1,-1]
def func(number):
    if number == []:
        print("Pystoy file")
        return [-1,-1]
    else:
        if len(number) % 3 == 0:
            for i in range(2,len(number),3):
                if number[i] < 0:
                    print("Nepravilnie radiusi")
                    return [-1,-1]
            n = len(number) // 3
            r = []
            x = []
            y = []
            v = []
            for i in range(0,n):
                v.append(1)
            for i in range(0,n):
                x.append(number[3*i])
                y.append(number[3*i +1])
                r.append(number[3*i+2])
            for i in range(0,n-1):
                for b in range(i + 1,n):
                    l = ((x[i] - x[b])**2 + (y[i] - y[b])**2)**(1/2)
                    if(l <= r[i] + r[b]):
                        if(r[i] >= r[b]):
                            if l >= r[i]:
                                v[i] = 0
                                v[b] = 0
                            else:
                                if (l + r[b]) >= r[i]:
                                    v[i] = 0
                                    v[b] = 0
                        else:
                            if l >= r[b]:
                                v[i] = 0
                                v[b] = 0
                            else:
                                if(l + r[i]) >= r[b]:
                                    v[i] = 0
                                    v[b] = 0
            cntrl = 0
            while cntrl != n*(n-1)/2:
                n1 = -1
                n2 = -1
                minim = int(sys.float_info.max)
                for i in range(0,n - 1):
                    for b in range(i + 1,n):
                        if (v[i] != 0) or (v[b] != 0):
                            l = ((x[i] - x[b])**2 + (y[i] - y[b])**2)**(1/2)
                            l = l - r[i] - r[b]
                            if l > 0:
                                if l < minim:
                                    minim = l
                                    n1 = i
                                    n2 = b
                            else:
                                if (v[i] != 0) or (v[b] != 0):
                                    if r[i] > r[b]:
                                        if v[i] == 0:
                                            minim = l
                                            n1 = i
                                            n2 = b
                                    else:
                                        if v[b] == 0:
                                            minim = l
                                            n1 = i
                                            n2 = b
                if (n1 != -1) and (n2 != -1):
                    if minim > 0:
                        if (v[n1] != 0) and (v[n2] != 0):
                            r[n1] += (minim / 2)
                            r[n2] += (minim / 2)
                            v[n1] = 0
                            v[n2] = 0
                        else:
                            if v[n1] == 0:
                                r[n2] += minim
                                v[n2] = 0
                            else:
                                r[n1] += minim
                                v[n1] = 0
                    else:
                        if r[n1] > r[n2]:
                            r[n2] = (-1)*r[n2] - minim
                            v[n2] = 0
                        else:
                            r[n1] = (-1)*r[n1] - minim
                            v[n1] = 0
                cntrl += 1
            for i in range(0,n):
                if v[i] != 0:
                    r[i] = -2
            return r
        else:
            print("Nepravilnoe kolvo")
            return [-1]
if autotest() == 0:
    filename = input("enter filename:")
    cntrl = funcread(filename)
    if(cntrl[0] != -1):
        for i in range(0,len(cntrl)):
            if cntrl[i] < 0:
                print("beskonechno rastet")
            else:
                print(cntrl[i])