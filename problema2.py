import itertools

k = 2
b = 24
n = 20000

edges = open("clustering2.txt")
line = edges.readline()
line = line.split()
NodosLeidos = {}
Puntos = []
line = edges.readline()
m = 0
while line:
    w = "".join(line.split())
    if w not in NodosLeidos:
        m += 1
    NodosLeidos[w] = m
    Puntos.append([m, [int(i) for i in line.split()]])

    line = edges.readline()

print len(NodosLeidos)
print len(Puntos)

def invertir(b):
    if b =='1':
        return '0'
    elif b == '0':
        return '1'


Nodos = {}
for w in NodosLeidos:
    Nodos[NodosLeidos[w]] = []
    for i in range(1, k+1):
        j = itertools.combinations(range(0,b), i)
        for p in j:
            Aux = w
            for q in p:
                Aux = Aux[:q] + invertir(Aux[q]) + Aux[q+1:]
            if Aux in NodosLeidos:
                Nodos[NodosLeidos[w]].append(NodosLeidos[Aux])

ListadoNodos = dict([(i, i) for i in range(1, m+1)])
ListadoClusters = dict([(i, [i]) for i in range(1, m+1)])
for w in Nodos:
    if len(Nodos[w]) > 0:
        for q in Nodos[w]:
            if ListadoNodos[q] == ListadoNodos[w]:
                continue
            a = [True, q,w]
            if len(ListadoClusters[ListadoNodos[a[1]]]) >= len(ListadoClusters[ListadoNodos[a[2]]]):
                p = ListadoClusters.pop(ListadoNodos[a[2]])
                ListadoClusters[ListadoNodos[a[1]]] += p
                c = ListadoNodos[a[1]]
                for n in p:
                    ListadoNodos[n] = c
            else:
                p = ListadoClusters.pop(ListadoNodos[a[1]])
                ListadoClusters[ListadoNodos[a[2]]] += p
                c = ListadoNodos[a[2]]
                for n in p:
                    ListadoNodos[n] = c

print ListadoClusters
print "Cantidad de Clusters:"
print len(ListadoClusters)