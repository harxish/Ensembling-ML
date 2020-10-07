import numpy as np

from data import get_data
from model import get_models

def get_fitness(model_genes, preprocessing_genes):

    fitness = 0
    predictions = []
    X_train, X_test, y_train, y_test = get_data(preprocessing_genes)
    models = get_models(model_genes)

    ## Training & Prediction
    for model in models:
        model.fit(X_train, y_train)
        predictions.append(model.predict_proba(X_test))

    predictions = np.array(predictions)
    predictions = np.mean(predictions, axis=0)
    y_hat = np.argmax(predictions, axis=1)

    for i in range(len(predictions)):
        fitness += predictions[i][y_test[i]]
    fitness = len(predictions) - fitness

    return fitness


if __name__ == "__main__":

    fitness = get_fitness([1, 1, 1], [0, 0, 1])
    print(fitness)
