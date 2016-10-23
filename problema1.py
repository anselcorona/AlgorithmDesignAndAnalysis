NumeroDeClusters = 4
n = 500

Aristas = open("clustering1.txt")
line = Aristas.readline()
line = line.split()
ListaGrafo = []
line = Aristas.readline()
while line:
    Conneccion = [int(i) for i in line.split()]
    ListaGrafo.append([Conneccion[-1]] + Conneccion[0:-1])
    line = Aristas.readline()
print "Este grafo tiene "+ str(len(ListaGrafo))+ " conecciones."
ListaGrafo.sort()

#SEPARAR LOS NODOS E INICIALIZAR UN DICCIONARIO DE CLUSTERS POR CADA NODO
#ESTE SE IRA REDUCIENDO HASTA 4 MAS ADELANTE

clus = [(i, i) for i in range(1, n+1)]
DiccionarioNodos = dict(clus)
clus = [(i, [i]) for i in range(1, n+1)]
DiccionarioClusters = dict(clus)
DistanciaMax = 0


#LA ULTIMA DISTANCIA AGREGADA SERA LA MAYOR YA QUE SIEMPRE SE BUSCA UNIFICAR CON LA MENOR.
while True:
    nodo = ListaGrafo.pop(0)
    assert nodo[0] >= DistanciaMax
    DistanciaMax = nodo[0]
    if DiccionarioNodos[nodo[1]] == DiccionarioNodos[nodo[2]]:
        continue
    if len(DiccionarioClusters[DiccionarioNodos[nodo[1]]]) >= len(DiccionarioClusters[DiccionarioNodos[nodo[2]]]):
        p = DiccionarioClusters.pop(DiccionarioNodos[nodo[2]])
        DiccionarioClusters[DiccionarioNodos[nodo[1]]] += p
        c = DiccionarioNodos[nodo[1]]
        for n in p:
            DiccionarioNodos[n] = c
    else:
        p = DiccionarioClusters.pop(DiccionarioNodos[nodo[1]])
        DiccionarioClusters[DiccionarioNodos[nodo[2]]] += p
        c = DiccionarioNodos[nodo[2]]
        for n in p:
            DiccionarioNodos[n] = c

    #IMPRIMIR LOS CLUSTERS ENCONTRADOS CUANDO SEA IGUAL AL TAMANO REQUERIDO
    if len(DiccionarioClusters) == NumeroDeClusters:
        print "Los ultimos "+str(NumeroDeClusters)+" clusters estan compuestos de los siguientes nodos:"
        for a in DiccionarioClusters.values():
            print a

    if len(DiccionarioClusters) < NumeroDeClusters:
        break


print "La distancia maxima es: "+ str(DistanciaMax)