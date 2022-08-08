import random
import numpy as np

#Funcao para sortear variaveis aleatorias

def sorteia(dim, minimum, maximum):
    lista = []

    for i in range(dim):
        lista.append(random.uniform(minimum, maximum))

    return lista

# Funcao do y.
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

# Funcao da populacao que gera dimensao, maximo e minimo.
def populate(pop_size, dim, minimum, maximum):
    pop = []
    for i in range(pop_size):
        pop.append(sorteia(dim, minimum, maximum))

    return pop

# Funcao da esfera onde soma componentes
def sphere(s):
    soma = 0
    for componente in s:
        soma += componente * componente
    return soma

def run_ed(dim, populacao, goal, max_steps=10000):
    
    best_fitness = None
    steps = 0
    
    # Ele pega o melhor fitness da funcao e conta quantas vezes precisou rodar para achar o best_fitness.
    while best_fitness is None or best_fitness > goal and steps < max_steps:
        #print(f"funcao run_ed")
        populacao = ed_step(dim, populacao)
        best_fitness = min([sphere(x) for x in populacao])
        steps += 1

        # Menor numero do fitness // min(s)

    return best_fitness, steps

    # Loop de todos os vetores da populacao. // Impressao do vetor populacao 1, 2, 3 // O enumerate ira retornar alguns valores.

def ed_step(dim, populacao):

    for idx, x in enumerate(populacao):
        # print(f'populacao[{idx}] = {x}') # F = Formatar uma string
        sem_x = populacao[:idx] + populacao[idx+1:]
        # print(sem_x)
        abc = random.sample(sem_x, 3) # abc cria uma lista abc = {a, b, c}
        # print(abc)

        # Sorteio com random.sample
        # X nao pode sair nos resultados
        # get_y criar um vetor novo de y novo, usando a formula.
        y = get_y(dim, x, abc[0], abc[1], abc[2]) # x nao precisa de um compenente pois ele ja foi dado

        # Impressao da vetor populacao 0
        # Compara x e y e imprime o melhor resultado.
        fitness_y = sphere(y)
        fitness_x = sphere(x) # O parametro foi escolhido pois comparamos com um elemento da populacao.

        if fitness_y < fitness_x:
            populacao[idx] = y

        #print(y)
        #print(f'{fitness_x=} {fitness_y=}')
        #print(populacao)
    return populacao

# Funcao principal do codigo, onde puxa as funcoes acima para gerar seu resultado.
def main():
    goal = 0.000001
    for dim in range(5, 30, 5): # Dimensoes da populacao
        for pop_size in range(100, 1000, 100): # Numero de populacao
            best_fitness_list = []
            steps_list = []
            for statistics in range(20):
                populacao = populate(pop_size, dim, -10, 10)
                best_fitness, steps = run_ed(dim, populacao, goal)
                best_fitness_list.append(best_fitness)
                steps_list.append(steps)

            bf = np.array([best_fitness_list])
            st = np.array([steps_list])
            #Media e Desvio Padrao do pop_size + best_fitness + steps
            print(f'{pop_size} {dim} {np.mean(bf)} {np.std(bf)} {np.mean(st)} {np.std(st)}')
            whit open('estatistica.dat', 'a') as outfile:
                print(f'{pop_size} {dim} {np.mean(bf)} {np.std(bf)} {np.mean(st)} {np.std(st)}', file=outfile)

if __name__ == '__main__':
    main()
