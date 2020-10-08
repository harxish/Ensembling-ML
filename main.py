import argparse
from src.population import Population


def main(generations, pop_max, mutation_rate, model_len, preprocessing_len):

    generations, pop_max, model_len, preprocessing_len = map(int, [generations, pop_max, model_len, preprocessing_len])
    mutation_rate = float(mutation_rate)
    population = Population(model_len, preprocessing_len, pop_max, mutation_rate)
    population.calcFitness()

    while(generations):
        population.naturalSelection()
        population.calcFitness()
        population.updatePopulation()
        print(population.generation-1, " : ", population.best)
        generations -= 1



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--generations', default='100',
                        help="#preprocessing functions to be considered")
    parser.add_argument('--pop_max', default='20',
                        help="Maximum population for every generation")
    parser.add_argument('--mutation_rate', default='.01',
                        help="Mutation Rate while performing crossover")
    parser.add_argument('--model_len', default='3',
                        help="#models to be considered")
    parser.add_argument('--preprocessing_len', default='3',
                        help="#preprocessing functions to be considered")
    args = parser.parse_args()

    main(args.generations, args.pop_max, args.mutation_rate, args.model_len, args.preprocessing_len)
