import numpy as np
import warnings

from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

MODELS = ['svm', 'knn', 'logistic']

def warn(*args, **kwargs):
    pass
warnings.warn = warn


def get_models(genes):

    model = find_models(genes)
    models = []
    for i in model:

        if i == 'svm':
            models.append(SVC(gamma='auto', probability=True))

        elif i == 'knn':
            models.append(KNeighborsClassifier(n_neighbors=5))

        elif i == 'logistic':
            models.append(LogisticRegression(random_state=0, max_iter=1000))

    return models


def find_models(genes):

    models = []
    for i in range(len(genes)):
        if genes[i]:
            models.append(MODELS[i])
    return models


if __name__ == "__main__":

    genes = [1, 0, 1]
    models = get_models(genes)
    for i in models:
        print(i)
