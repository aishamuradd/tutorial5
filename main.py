

def solveCubic(a,b,c,d):
    A = ((-b ** 3 / (27 * a ** 3)) + (b * c / (6 * a ** 2)) - (d / (2 * a)))
    B = (((((-b ** 3 / (27 * a ** 3)) + (b * c / (6 * a ** 2)) - (d / 2 * a)) ** 2) + (
                ((c / (3 * a)) - (b ** 2 / (9 * a ** 2))) ** 3)) ** (1 / 2))

    C = ((A + B) ** (1 / 3))
    D = (((A - B) ** (1 / 3)) - (b / (3 * a)))
    E = (C + D)
    x = E.real
    return x


name =(input("What is your name ?"))

a = int (input("What is your a ?"))
b = int (input ("What is your b ?"))
c = int (input ("What is your c ?"))
d = int (input ("What is your d ?"))

def CubicEquation(a,b,c,d):
    answer = (((int a*x)"**3")+((int b*x)"**2")+(int c*x)+(int d )"= 0")
    return answer. replace("+-","-").replace("-1x","+x").replace("+0x","").replace("-0","")



print("Hello",name.capitalize(),", I will solve",CubicEquation,)
print("The root of the cubic is",solveCubic(a,b,c,d),)
