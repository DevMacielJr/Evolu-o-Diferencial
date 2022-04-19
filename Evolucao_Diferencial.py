import random

def sorteia(dim, minimum, maximum):
    lista = []

    for i in range(dim):
        lista.append(random.uniform(minimum, maximum))

    return lista


def ed(dim, x, a, b, c):
    y = x.copy()
    F = 0.8
    CR = 0.9
    R = random.randrange(dim)

    for i in range(dim):
        r = random.random()
        if r < CR or i == R:
            y[i] = a[i] + F * (b[i] - c[i])

    return y


def main():
    dim = (5)
    x = sorteia(dim, -10, 10)
    a = sorteia(dim, -10, 10)
    b = sorteia(dim, -10, 10)
    c = sorteia(dim, -10, 10)

    print(ed(dim, x, a, b, c))
    print(x)
    print(a)
    print(b)
    print(c)


if __name__ == '__main__':
    main()


def populate():
    pop = 5
    R = []
    for i in range(x):
        R.append(random.choice(range(20)))

    return pop
