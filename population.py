class Population:

    def __init__(self, model_len, preprocessing_len, popMax, mutationRate):

        self.popMax = popMax
        self.mutationRate = mutationRate
        self.sumFitness = 0
        self.generation = 1
        self.best = ""
        self.population = []
        self.newPopulation = []

        for _ in range(popMax):
            self.population.append(DNA(model_len, preprocessing_len))


    def __str__(self):

        res = ""
        for i in self.population:
            res += str(i) + "\n"
        print(res)


    def calcFitness(self):

        for i in self.population:
            i.calcFitness()


    def initFitness(self):

        self.sumFitness = 0
        for i in self.population:
            self.sumFitness += i.fitness


    def getWeightedRandom(self):

        rand = round(random.uniform(1, self.sumFitness+1))
        for i in self.population:
            rand -= i.fitness
            if rand < 1:
                return i
        return self.population[-1]


    def updatePopulation(self):

        self.generation += 1
        max = 0
        for i in self.population:
            if i.fitness > max:
                max = i.fitness
                self.best = "".join(i.genes)


    def naturalSelection(self):

        self.initFitness()
        self.newPopulation.clear()
        for _ in range(len(self.population)):
            X, Y = self.getWeightedRandom(), self.getWeightedRandom()
            XY, YX = X.crossover(Y), Y.crossover(X)
            XY.mutate(self.mutationRate), YX.mutate(self.mutationRate)
            self.newPopulation.append(XY if XY.fitness > YX.fitness else YX)

        self.population = [i for i in self.newPopulation]
