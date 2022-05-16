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


def sphere(s):
    soma = 0
    for componente in s:
        soma += componente * componente
        return soma


def main():
    dim = 3  # Dimensões da população
    pop_size = 10  # Número de população

    populacao = populate(pop_size, dim, -10, 10)

    print(populacao)

    y = ed_step(dim, populacao[0], populacao[1], populacao[2], populacao[3])

    print(y)

    fitness_y = sphere(y)
    fitness_x = sphere(populacao[0])

    print(f'{fitness_x=} {fitness_y=}')

    if fitness_y < fitness_x:
        populacao[0] = y

    print(populacao)


if __name__ == '__main__':
    main()
