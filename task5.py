import math
import sys
def autotest():
    if(autotest1() and autotest2() and autotest3()) == 1:
        return 0
    else:
        return 1
def autotest1():
    number = [1,2,1,5,2,1]
    nr1 = 2.0
    nr2 = 2.0
    cntrl = func(number)
    if (nr1 == cntrl[0]) and (nr2 == cntrl[1]):
        print("Autotest1 passed")
        return 1
    else:
        print("Autotest1 failed!!")
        return 0
def autotest2():
    number = [3,0,0.4,0,4,0.6]
    nr1 = 2.0
    nr2 = 3.0
    cntrl = func(number)
    if(nr1 == cntrl[0]) and (nr2 == cntrl[1]):
        print("Autotest2 passed")
        return 1
    else:
        print("Autotest2 failed")
        return 0
def autotest3():
    number = [3,0,0.1,0,4,0.1]
    nr1 = 2.5
    nr2 = 2.5
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
        if len(number) != 6:
            print("Nepravilnoe kolvo")
            return [-1,-1]
        else:
            x1 = number[0]
            y1 = number[1]
            v1 = number[2]
            x2 = number[3]
            y2 = number[4]
            v2 = number[5]
            if (v1 < 0) or (v2 < 0) or ((v1 == 0) and(v2==0)):
                print("Nepravilnaya skorost'")
                return [-1,-1]
            else:
                l = math.sqrt((x2-x1)**2 +(y2-y1)**2)
                t = l / (v1 + v2)
                if t == 0:
                    print("Slishkom malenkoe otnoshenie")
                    return [-1,-1]
                else:
                    r1 = t*v1
                    r2 = t*v2
                    return [r1,r2]
if autotest() == 0:
    filename = input("enter filename:")
    cntrl = funcread(filename)
    if(cntrl[1] != -1):
        print("r1 = "+str(cntrl[0]))
        print("r2 = "+str(cntrl[1]))