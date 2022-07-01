import random
import numpy as np

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

def run_ed(dim, populacao, goal):
    best_fitness = None
    steps = 0
    
    # Ele pega o melhor fitness da função é conta quantas vezes precisou rodar para achar o best_fitness.
    while best_fitness is None or best_fitness > goal:
        print(f"função run_ed")
        populacao = ed_step(dim, populacao)
        best_fitness = min([sphere(x) for x in populacao])
        steps += 1

        # Menor número do fitness // min(s)

    return best_fitness, steps

    # Loop de todos os vetores da população.
    # Impressao do vetor populacao 1, 2, 3
    # O enumerate irá retornar alguns valores.

def ed_step(dim, populacao):

    for idx, x in enumerate(populacao):
        # print(f'populacao[{idx}] = {x}') # F = Formatar uma string
        sem_x = populacao[:idx] + populacao[idx+1:]
        # print(sem_x)
        abc = random.sample(sem_x, 3) # abc cria uma lista abc = {a, b, c}
        # print(abc)

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

    #Criar um loop que varia de 10 em 10 ate 100 individuos, criar media e desvio padrão do desvio padrão até optimizar
    pop_size = 10 # Número de população


    for statistics in range(20):
        populacao = populate(pop_size, dim, -10, 10)
        best_fitness, steps = run_ed(dim, populacao, goal)

    bf = np.array([best_fitness])
    #Média e Desvio Padrão do pop_size + best_fitness
    print(f'{pop_size} {np.mean(bf)} {np.std(bf)}')

    st = np.array([steps])
    #Média e Desvio Padrão do pop_size + steps
    print(f'{pop_size} {np.mean(st)} {np.std(st)}')

if __name__ == '__main__':
    main()