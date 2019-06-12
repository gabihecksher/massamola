from matplotlib import pyplot as plt

#---------------Variavel Global---------------#
constantes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Y_s = [0, 0, 0, 0]

#---------------Muda Variavel Global constantes---------------#
def lê_constantes():
    arquivo = open("entrafa_MMA_RKI", 'r')
    i = 0
    r = 0
    global constantes
    for linha in arquivo:
        if i > 0 and i <= 10:
            temp = linha.split()
            constantes[r] = float(temp[2])
            #print(temp[0], temp[2])
            r += 1
        i += 1
    arquivo.close()
    return constantes

#---------------Muda Variavel Global Y_s---------------#
def lê_ys():
    arquivo = open("entrafa_MMA_RKI", 'r')
    i = 0
    r = 0
    global Y_s
    for linha in arquivo:
        if i > 12 and i <= 17:
            temp = linha.split()
            Y_s[r] = float(temp[2])
            print(temp[0], temp[2])
            r += 1
        i += 1
    arquivo.close()
    return Y_s

#---------------Presa Predador---------------#
#dy1/dt = aY1 - b * Y1 * Y2
#dy2/dt = -cY2 + d * Y1 * Y2

def presa_predador(t, Ys):
    a, b, c, d = 100, 0.37, 100, 0.05
    #Y[0] = Y1
    #Y[1] = Y2
    #y1 = dy1/dt
    #y2 = dy2/dt
    y1 = a * Ys[0] - b * Ys[0] * Ys[1]
    y2 = -1 * c * Ys[1] + d * Ys[0] * Ys[1]
    return [y1, y2]

#---------------Massa Mola Amortecedor---------------#
#w1' = V1
#w2' = V2
#v1' = 1/m1 * (-(c1 + c2) * V1 + c2 * V2 - (k1 + k2) * W1 + k * W2 + f1)
#v1' = 1/m1 * (-(c1 + c2) * V2 + c2 * V1 - (k1 + k2) * W2 + k * W1 + f2)


def massa_mola_amortecedor(t, Ys):
    f1, c1, k1, m1 = constantes[0], constantes[1], constantes[2], constantes[3]
    f2, c2, k2, m2 = constantes[4], constantes[5], constantes[6], constantes[7]
    c3, k3 = constantes[8], constantes[9]
    #Y[0] = W1
    #Y[1] = W2
    #Y[2] = V1
    #Y[3] = V2
    y1 = Ys[2] 
    y2 = Ys[3]
    y3 = (f1 - (c1 + c2) * Ys[2] - (k1 + k2) * Ys[0] + k2 * Ys[1] + c2 * Ys[3]) / m1
    y4 = (f2 - (c2 + c3) * Ys[3] - (k2 + k3) * Ys[1] + c2 * Ys[2] + k2 * Ys[0]) / m2
    #y1 = w1'
    #y2 = w2'
    #y3 = v1'
    #y4 = v2'
    return [y1, y2, y3, y4]

#---------------Auxiliar---------------#
def soma(a, b):
    return [x + y for x, y in zip(a, b)]

def multiplica(num, vet):
    return [x * num for x in vet]


#---------------Metodo inplicito---------------#
#Yk+1 = Yk + h/2 * (f(Xk, Yk) + F(Xk + h, Yk+1))
#                  |___a____|
#                              |______b_______|
#                  |_____________c____________|
#           |________________d________________|
#       |__________________e__________________|

def correcao(f, Y, Y_, h, x):
    a = f(x, Y)
    b = f(x+h, Y_)
    c = soma(a, b)
    d = multiplica(h/2, c)
    e = soma(Y, d)
    return e

#---------------Metodo Runge-Kutta---------------#
#Yk+1 = Yk + h * F(Xk + h/2, Yk + h/2 * F(Xk, Yk))
#                                |_______a______|
#                           |_________b_________|
#           |_________________c_________________|
#       |___________________d___________________|

def runge_kuta(h, f, Ys, x, passos):
    Ys1 = []
    Xs = []
    count = 0
    while(count <= passos):
        a = multiplica((h/2),f(x, Ys))
        b = soma(Ys, a)
        
        d = soma(Ys, c)
        d = correcao(f, Ys, d, h, x)
        d = correcao(f, Ys, d, h, x)
        Ys1.append(d)
        Ys = Ys1[count]
        x += h
        Xs.append(x)
        count += 1
    return Ys1, Xs

#---------------Chama funcoes para mudar variaveis globais---------------#
lê_constantes()
lê_ys()

#---------------Chama metodo runge_kuta para massa_mola_amortecedor---------------#
#variavel  =    métolo   h           funcao            w1 w2 v1 v2  x passos
resultado2 = runge_kuta(0.02, massa_mola_amortecedor, Y_s, 0, 1000)

#---------------Cria arquivo com o grafico---------------#
fig = plt.gcf()
fig.set_size_inches([9,6])
plt.plot(resultado2[1], resultado2[0])
plt.savefig("grafico_massa_mola_amortecedor")
