import random

def sorteia(dim, minimum, maximum):
    lista = []

    for i in range(dim):
        lista.append(random.uniform(minimum, maximum))

    return lista

def ed_step(dim, x, a, b, c):
    y = x.copy()
    F = 0.8
    CR = 0.9
    R = random.randrange(dim)

    for i in range(dim):
        r = random.random()
        if r < CR or i == R:
            y[i] = a[i] + F * (b[i] - c[i])

    return y

def populate(pop_size, dim, minimum, maximum):
    pop = []
    for i in range(pop_size):
        pop.append(sorteia(dim, minimum, maximum))

    return pop

def main():
    dim = 5
    pop_size = 4

    populacao = populate(pop_size, dim, -10, 10)

    print(populacao)

    y = ed_step(dim, populacao[0], populacao[1], populacao[2], populacao[3])

    print(y)

if __name__ == '__main__':
    main()
