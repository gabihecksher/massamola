from matplotlib import pyplot as plt

def presa_predador(t, Ys):
    a = 100
    b = 0.37
    c = 100
    d = 0.05
    y1 = a * Ys[0] - b * Ys[0] * Ys[1]
    y2 = -1 * c * Ys[1] + d * Ys[0] * Ys[1]
    return [y1, y2]

def massa_mola_amortecedor(t, Ys):
    f1, f2, c1, c2, c3, k1, k2, k3, m1, m2 = 0, 0, 0.5, 0.5, 0.5, 1, 1, 1, 1, 1
    y1 = Ys[2]
    y2 = Ys[3]
    y3 = (f1 - (c1 + c2) * Ys[2] - (k1 + k2) * Ys[0] + k2 * Ys[1] + c2 * Ys[3]) / m1
    y4 = (f2 - (c2 + c3) * Ys[3] - (k2 + k3) * Ys[1] + c2 * Ys[2] + k2 * Ys[0]) / m2
    return [y3, y4, y1, y2]

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

def correcao(f, Y, Y_, h, x):
    a = f(x, Y)
    b = f(x+h, Y_)
    c = soma(a, b)
    d = multiplica(h/2, c)
    e = soma(Y, d)
    return e

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




resultado1 = runge_kuta(0.002, presa_predador, [1000, 300], 0)

resultado2 = runge_kuta(0.002, massa_mola_amortecedor, [1, 1, 0, 0], 0, 1000)

fig = plt.gcf()
fig.set_size_inches([9,6])
plt.plot(resultado1[1], resultado1[0])
plt.savefig("grafico_presa_predador")

fig = plt.gcf()
fig.set_size_inches([9,6])
plt.plot(resultado2[1], resultado2[0])
plt.savefig("grafico_massa_mola_amortecedor")