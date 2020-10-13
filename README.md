[![forthebadge](https://forthebadge.com/images/badges/powered-by-coffee.svg)](https://forthebadge.com)

# Genetic-Algorithms-Ensembling
Ensembling Machine learning algorithms using Genetic Algorithms.

Using Genetic algorithms figure out the best combination of pre-processing functions and models so that the best accuracy is obtained. The gene is bit array of length #models + #pre-processing functions. The first half is the model gene where 1 means the model is taken into considerations 0 means not. The same holds for preprocessing gene, 1 means the pre processing function is performed and 0 means not.

> 101100 -> model gene : 101 && preprocessing gene : 100

The genes undergo crossover and mutation during natural selection. The fitness is calculated with the help of accuracy, the higher the accuracy better the gene fitness, so, the more fit genes have high probability to be choosen so they are used to create genes for the next generation.

**Models** : SVM, KNN, Logistic Regression.

**Preprocessing** : Polynomial Features, Scaling, Normalisation.

---

## Code organization

- `src.DNA.py` : Gene coding and performing corssover between genes and mutation.
- `src.data.py` : Loading WBCD Dataset and pre-processing functions for preprocessing genes.
- `src.model.py` : Loading models from Sklearn and giving it for model genes.
- `src.fitness.py` : Predict test labels and measure accuracy.
- `src.population.py` : Population class which does natural selection on different generation.

---

## How to Run

```
python3 main.py --generations 100 --pop_max 50 --mutation_rate 0.01 
                --model_len 3 --preprocessing_len 3
```
---
 
## Output

| Generation | Best Gene | Accuracy |
| ----------- | ----------- | ----------- |
| 1 | 101010 | 95.52 |
| 2 | 110110 | 96.15 |
| 3 | 010100 | 96.34 |
| 4 | 010100 | 95.54 |
| 5 | 110111 | 96.24 |
| 6 | 010100 | 95.54 |
| 7 | 010100 | 96.57 |
| 8 | 010100 | 95.66 |
| 9 | 010000 | 96.57 |
