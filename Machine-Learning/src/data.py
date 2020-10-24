import pandas as pd
import numpy as np

from sklearn.preprocessing import scale
from sklearn.preprocessing import normalize
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import QuantileTransformer
from sklearn.model_selection import train_test_split

PREPROCESSINGS = ['poly', 'scale', 'normal']


def fetch_dataset():

    wbcd_data = pd.read_csv('datasets/breast-cancer-wisconsin.data', header=None)
    wbcd_data.columns = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
                         'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli',
                         'Mitoses', 'Class']

    wbcd_data.drop(['Sample code number'], axis=1, inplace=True)
    wbcd_data['Bare Nuclei'] = wbcd_data['Bare Nuclei'].apply(lambda x: 0 if x == '?' else int(x))
    wbcd_data['Class'] = wbcd_data['Class'].map({4: 1, 2: 0})
    wbcd_data = wbcd_data.sample(frac = 1)

    X_train, X_test, y_train, y_test = train_test_split(wbcd_data.drop(['Class'], axis=1).values,
                                                        wbcd_data['Class'].values, random_state=0)

    return X_train, X_test, y_train, y_test


def get_preprocessing(genes):

    preprocessings = []
    for i in range(len(genes)):
        if genes[i] == 1:
            preprocessings.append(PREPROCESSINGS[i])
    return preprocessings


def get_data(genes):

    X_train, X_test, y_train, y_test = fetch_dataset()
    preprocessing_functions = get_preprocessing(genes)

    for i in preprocessing_functions:

         if i == 'poly':
             poly = PolynomialFeatures(2)
             X_train = poly.fit_transform(X_train)
             X_test  = poly.transform(X_test)

         elif i == 'scale':
             X_train = scale(X_train)
             X_test  = scale(X_test)

         elif i == 'normal':
             X_train = normalize(X_train, norm='l2')
             X_test  = normalize(X_test, norm='l2')

    return X_train, X_test, y_train, y_test


if __name__ == "__main__":

    genes = [1, 1, 1]
    X_train, X_test, y_train, y_test = get_data(genes)
    print(X_train)
