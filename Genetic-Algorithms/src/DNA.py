import math
import random
from src.fitness import get_fitness

class DNA:

    def __init__(self, model_len, preprocessing_len):
        self.fitness = .0
        self.probability = .0
        self.prob = .0
        self.model_len = model_len
        self.preprocessing_len = preprocessing_len
        self.model_genes = [random.randint(0, 1) for i in range(model_len)]
        self.preprocessing_genes = [random.randint(0, 1) for i in range(preprocessing_len)]


    def calcFitness(self):
        if self.model_genes == [0]*self.model_len:
                self.model_genes[random.randint(0, self.model_len-1)] = 1

        self.fitness, self.probability = get_fitness(self.model_genes, self.preprocessing_genes)


    def crossover(self, Y):
        XY = DNA(self.model_len, self.preprocessing_len)
        mid_model, mid_preprocessing = round(self.model_len/2), round(self.preprocessing_len/2)

        XY.model_genes[0:mid_model] = self.model_genes[0:mid_model]
        XY.model_genes[mid_model:] = Y.model_genes[mid_model:]
        XY.preprocessing_genes[0:mid_preprocessing] = self.preprocessing_genes[0:mid_preprocessing]
        XY.preprocessing_genes[mid_preprocessing:] = Y.preprocessing_genes[mid_preprocessing:]

        return XY


    def mutate(self, mutationRate):
        for i in range(self.model_len):
            if random.random() < mutationRate:
                self.model_genes[i] = int(not(self.model_genes[i]))

        for i in range(self.preprocessing_len):
            if random.random() < mutationRate:
                self.preprocessing_genes[i] = int(not(self.preprocessing_genes[i]))


    def __len__(self):
        return self.model_len + self.preprocessing_len


    def __str__(self):
        to_print = []
        to_print.extend(self.model_genes)
        to_print.extend(self.preprocessing_genes)
        string =  "".join([str(x) for x in to_print])
        string += " -> "
        string += str(round(self.probability*100, 2))

        return string
