import random

#Função para sortear variáveis aleatórias.
def sorteia(dim, minimum, maximum):
    lista = []

    for i in range(dim):
        lista.append(random.uniform(minimum, maximum))

    return lista

# Função do y.
def get_y(dim, x, a, b, c):
    y = x.copy()
    F = 0.8
    CR = 0.9
    R = random.randrange(dim)

    for i in range(dim):
        r = random.random()
        if r < CR or i == R:
            y[i] = a[i] + F * (b[i] - c[i])

    return y

# Função da população que gera dimensão, máximo é minimo.
def populate(pop_size, dim, minimum, maximum):
    pop = []
    for i in range(pop_size):
        pop.append(sorteia(dim, minimum, maximum))

    return pop

# Função da esfera onde soma componentes
def sphere(s):
    soma = 0
    for componente in s:
        soma += componente * componente
    return soma

def run_ed(dim, populacao):
    run = []
    s = 2
    c = 0
    
    while s > 1:
        populacao = random.random()
        run = ed_step(populacao, dim)
        s = sphere(run)
        c+=1
    return run;

    # Loop de todos os vetores da população.
    # Impressao do vetor populacao 1, 2, 3
    # O enumerate irá retornar alguns valores.

def ed_step(populacao, dim):

    for idx, x in enumerate(populacao):
        print(f'populacao[{idx}] = {x}') # F = Formatar uma string
        sem_x = populacao[:idx] + populacao[idx+1:]
        print(sem_x)
        abc = random.sample(sem_x, 3) # abc cria uma lista abc = {a, b, c}
        print(abc)

        # Sorteio com random.sample
        # X não pode sair nos resultados
        # get_y criar um vetor novo de y novo, usando a formula.
        y = get_y(dim, x, abc[0], abc[1], abc[2]) # x não precisa de um compenente pois ele já foi dado

        # Impressão da vetor populacao 0
        # Compara x é y e imprime o melhor resultado.
        fitness_y = sphere(y)
        fitness_x = sphere(x) # O paramêtro foi escolhido pois comparamos com um elemento da população.

        if fitness_y < fitness_x:
            populacao[idx] = y

        print(y)

        print(f'{fitness_x=} {fitness_y=}')
        print(populacao)
    return populacao

# Função principal do código, onde puxa as funções acima para gerar seu resultado.
def main():
    dim = 3 # Dimensões da população
    pop_size = 10 # Número de população

    populacao = populate(pop_size, dim, -10, 10)

    print(populacao)
    ed_step(populacao, dim)
    run_ed(populacao, dim)

if __name__ == '__main__':
    main()
