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
    #f1, f2, c1, c2, c3, k1, k2, k3, m1, m2 = 10, 1, 0.5, 0.5, 0.5, 1, 1, 1, 1, 1
    f1, f2, c1, c2, c3, k1, k2, k3, m1, m2 = 0, 0, 1, 1, 1, 1, 1, 1, 1, 1
    y1 = Ys[2]
    y2 = Ys[3]xd
    y3 = (f1 - (c1 + c2) * Ys[2] - (k1 + k2) * Ys[0] + k2 * Ys[1] + c2 * Ys[3]) / m1
    y4 = (f2 - (c2 + c3) * Ys[3] - (k2 + k3) * Ys[1] + c2 * Ys[2] + k2 * Ys[0]) / m2
    return [y1, y2, y3, y4]

def soma(a, b):
    return [x + y for x, y in zip(a, b)]

def multiplica(num, vet):
    return [x * num for x in vet]

def correcao(f, Y, Y_, h, x):
    a = f(x, Y)
    b = f(x+h, Y_)
    c = soma(a, b)
    d = multiplica(h/2, c)
    e = soma(Y, d)
    return e

def runge_kuta(h, f, Ys, x, passos):
    Ys1 = []
    Xs = []
    count = 0
    while(count <= passos):
        a = multiplica((h/2),f(x, Ys))
        b = soma(Ys, a)
        c = multiplica(h, f(x + h/2, b))
        d = soma(Ys, c)
        d = correcao(f, Ys, d, h, x)
        d = correcao(f, Ys, d, h, x)
        Ys1.append(d)
        Ys = Ys1[count]
        x += h
        Xs.append(x)
        count += 1
    return Ys1, Xs


# resultado1 = runge_kuta(0.002, presa_predador, [1000, 300], 0, 1000)

resultado2 = runge_kuta(0.02, massa_mola_amortecedor, [1, 0, 0, 0], 0, 1000)

# fig = plt.gcf()
# fig.set_size_inches([9,6])
# plt.plot(resultado1[1], resultado1[0])
# plt.savefig("grafico_presa_predador")

fig = plt.gcf()
fig.set_size_inches([9,6])
plt.plot(resultado2[1], resultado2[0])
plt.savefig("grafico_massa_mola_amortecedor")
