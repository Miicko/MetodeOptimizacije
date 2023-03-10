import numpy as np
import matplotlib.pyplot as plt
import math
import numpy.linalg as lin


#Njutn Rapsonov Metod
def newtonRaphson(x0, tol):
    x_novo = x0
    x_pre = math.inf
    iter = 0

    while (abs(x_pre - x_novo) > tol):
        iter += 1
        x_pre = x_novo
        x_novo = x_pre - dfunc(x_pre) / ddfunc(x_pre)

    xopt = x_novo
    fopt = func(xopt)
    return xopt, fopt, iter


def func(x):
    f = -(x ** 4 - 5 * x ** 3 - 2 * x ** 2 + 24 * x)
    return f


def dfunc(x):
    f = -(4 * x ** 3 - 15 * x ** 2 - 4 * x + 24)
    return f


def ddfunc(x):
    f = -(12 * x ** 2 - 30 * x - 4)
    return f


# Test Njutn
tol = 0.0001
init_guess = 1
[xopt, fopt, iter] = newtonRaphson(init_guess, tol)
print("Njutn-Rapsonov metod",xopt, fopt, iter)

x = np.linspace(0, 4, 1000)
f = np.linspace(0, 0, len(x))

for i in range(0, len(x), 1):
    f[i] = func(x[i])

p = plt.plot(x, f, 'b--')
p = plt.plot(xopt, fopt, 'om', label='max[f(x)]', markersize=15, markeredgewidth=3)
plt.show()


#Metod secice
def secica(x1, x0, tol):
    x_pre = x0
    x_ppre = math.inf
    x_novo = x1
    iter = 0

    while (abs(x_novo - x_pre) > tol):
        iter += 1
        x_ppre = x_pre
        x_pre = x_novo
        x_novo = x_pre - dfunc(x_pre) * (x_pre - x_ppre) / (dfunc(x_pre) - dfunc(x_ppre))

    xopt = x_novo
    fopt = func(xopt)
    return xopt, fopt, iter


def func(x):
    f = -(x ** 4 - 5 * x ** 3 - 2 * x ** 2 + 24 * x)
    return f


def dfunc(x):
    f = -(4 * x ** 3 - 15 * x ** 2 - 4 * x + 24)
    return f


#Test Secica
tol = 0.0001
init_guess1 = 0
init_guess2 = 3

[xopt, fopt, iter] = secica(init_guess1, init_guess2, tol)
print("Metod secice",xopt, fopt, iter)
x = np.linspace(0, 4, 1000)
f = np.linspace(0, 0, len(x))

for i in range(0, len(x), 1):
    f[i] = func(x[i])

p = plt.plot(x, f, 'b--')
p = plt.plot(xopt, fopt, 'om', label='max[f(x)]', markersize=15, markeredgewidth=3)
plt.show()


#Fibonacijev metod
def fibonaci_metod(a, b, tol):
    n = 1
    while ((b - a) / tol) > fibonaci_broj(n):
        n += 1

    x1 = a + fibonaci_broj(n - 2) / fibonaci_broj(n) * (b - a)
    x2 = a + b - x1

    for i in range(2, n + 1):
        if func(x1) < func(x2):
            b = x2
            x2 = x1
            x1 = a + b - x2
        else:
            a = x1
            x1 = x2
            x2 = a + b - x1

    if func(x1) < func(x2):
        xopt = x1
        fopt = func(xopt)
    else:
        xopt = x2
        fopt = func(x2)

    return xopt, fopt, n


def fibonaci_broj(n):
    if n < 3:
        f = 1
    else:
        fp = 1
        fpp = 1

        for i in range(3, n + 1):
            f = fp + fpp
            fpp = fp
            fp = f

    return f


def func(x):
    f = -(x ** 4 - 5 * x ** 3 - 2 * x ** 2 + 24 * x)
    return f


#Test Fibonaci
a = 0
b = 3
tol = 0.0001
[xopt, fopt, n] = fibonaci_metod(a, b, tol)
print("Fibonacijev metod",xopt, fopt, n)

x = np.linspace(0, 4, 1000)
f = np.linspace(0, 0, len(x))

for i in range(0, len(x), 1):
    f[i] = func(x[i])

p = plt.plot(x, f, 'b--')
p = plt.plot(xopt, fopt, 'om', label='max[f(x)]', markersize=15, markeredgewidth=3)
plt.show()


#Metoda zlatnog preseka
def zlatniPresek(a, b, tol):
    c = (3 - math.sqrt(5)) / 2
    x1 = a + c * (b - a)
    x2 = a + b - x1
    n = 1

    while (b - a) > tol:
        n += 1
        if func(x1) <= func(x2):
            b = x2
            x1 = a + c * (b - a)
            x2 = a + b - x1
        else:
            a = x1
            x1 = a + c * (b - a)
            x2 = a + b - x1

    if func(x1) < func(x2):
        xopt = x1
        fopt = func(x1)
    else:
        xopt = x2
        fopt = func(x2)

    return xopt, fopt, n


def func(x):
    f = -(x ** 4 - 5 * x ** 3 - 2 * x ** 2 + 24 * x)
    return f


#Test zlatni presek
a = 0
b = 3
tol = 0.0001
[xopt, fopt, n] = zlatniPresek(a, b, tol)
print("Metod zlatnog preseka",xopt, fopt, n)

x = np.linspace(0, 4, 1000)
f = np.linspace(0, 0, len(x))

for i in range(0, len(x), 1):
    f[i] = func(x[i])

p = plt.plot(x, f, 'b--')
p = plt.plot(xopt, fopt, 'om', label='max[f(x)]', markersize=15, markeredgewidth=3)
plt.show()


# Metod parabole
def parabola(x1, x3, tol):
    X = np.array([x1, (x1 + x3) / 2, x3]).transpose()
    pom = np.array([1, 1, 1]).transpose()
    Y = np.array([pom, X, X * X]).transpose()
    # x = [x1 x2 x3]' pom = [1 1 1]'
    # Y = [1 1 1; x1 x2 x3; x1^2 x2^2 x3^2]
    F = np.linspace(0, 0, len(X))

    for i in range(0, len(X), 1):
        F[i] = func(X[i])

    abc = lin.solve(Y, F)
    x = -abc[1] / 2 / abc[2]
    fx = func(x)
    n = 0

    while np.abs(np.dot([1, x, x ** 2], abc) - fx) > tol:
        if (x > X[1]) and (x < X[2]):
            if (fx < F[1]) and (fx < F[2]):
                X = np.array([X[1], x, X[2]])
                F = np.array([F[1], fx, F[2]])
            elif (fx > F[1]) and (fx < F[2]):
                X = np.array([X[0], X[1], x])
                F = np.array([F[0], F[1], fx])
            else:
                print('Greska!')

        elif (x > X[0]) and (x < X[2]):
            if (fx < F[0]) and (fx < F[1]):
                X = np.array([X[0], x, X[2]])
                F = np.array([F[0], fx, F[2]])
            elif (fx > F[1]) and (fx < F[0]):
                X = np.array([x, X[1], X[2]])
                F = np.array([fx, F[1], F[2]])
            else:
                print('Greska!')
        else:
            print('x lezi van granica!')

        pom = np.array([1, 1, 1]).transpose()
        Y = np.array([pom, X, X * X]).transpose()
        F = np.linspace(0, 0, len(X))

        for i in range(0, len(X), 1):
            F[i] = func(X[i])

        abc = lin.solve(Y, F)
        x = -abc[1] / 2 / abc[2]
        fx = func(x)
        n = n + 1

    return x, fx, n


def func(x):
    f = -(x ** 4 - 5 * x ** 3 - 2 * x ** 2 + 24 * x)
    return f


#Test metode parabole
a = 0
b = 2
tol = 0.001

[xopt, fopt, n] = parabola(a, b, tol)
print("Metod parabole",xopt, fopt, n)

x = np.linspace(0, 4, 1000)
f = np.linspace(0, 0, len(x))

for i in range(0, len(x), 1):
    f[i] = func(x[i])

p = plt.plot(x, f, 'b--')
p = plt.plot(xopt, fopt, 'om', label='max[f(x)]', markersize=15, markeredgewidth=3)
plt.show()