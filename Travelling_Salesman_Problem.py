import time

def distancia(punto1, punto2):
    return ((punto1[0] - punto2[0])**2 + (punto1[1] - punto2[1])**2)** 0.5

def distancia_total(puntos):
    return sum([distancia(punto, puntos[index + 1]) for index, punto in enumerate(puntos[:-1])])

def optimized_tsp(puntos, start=None):
    if start is None:
        start = puntos[0]
    to_visit = puntos
    path = [start]
    to_visit.remove(start)
    while to_visit:
        nearest = min(to_visit, key=lambda x: distancia(path[-1], x))
        path.append(nearest)
        to_visit.remove(nearest)
    return path

def main():
    f = open("ca4663.txt", 'r')
    list =[[float(line.split()[0]), float(line.split()[1])] for line in f]
    answer = distancia_total(optimized_tsp(list))
    print("The solution is " + str(int(answer)))

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))