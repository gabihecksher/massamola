def presa_predador(t, Ys):
    a = 100
    b = 0.37
    c = 100
    d = 0.05
    y1 = a * Ys[0] - b * Ys[0] * Ys[1]
    y2 = -1 * c * Ys[1] + d * Ys[0] * Ys[1]
    return [y1, y2]

def soma(a, b):
    d, c, e = [], [], []
    if len(a) > len(b):
        c, e = b, a
    elif len(a) < len(b):
        c, e = a, b
    else:
        c, e = a, b
    for i in range(len(c)):
        d.append(c[i] + e[i])
    return d

def multiplica(num, vet):
    temp = vet
    for i in range(len(vet)):
        temp[i] = vet[i] * num
    return temp

def runge_kuta(h, f, Ys, x):
    Ys1 = []
    count = 0
    while(x != 0.036):
        a = multiplica((h/2),f(x, Ys))
        b = soma(Ys, a)
        c = multiplica(h, f(x + h/2, b))
        d = soma(Ys, c)
        Ys1.append(d)
        Ys = Ys1[count]
        x += h
        count += 1
    return Ys1


runge_kuta(0.002, presa_predador, [1000, 300], 0)