# Assignment 3: Machine Learning
# Problem 1 - Perceptron Algorithm
##############################################

import sys
from random import choice, seed, randrange
import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt

#Create the SIGMOID or activation function
sigmoid_func = lambda x: -1 if x < 0 else 1

def perceptron_sigmoid(X, Y):
    w = np.zeros(len(X[0]))
    eta = 1
    n = 30
    errors = []

    for t in range(n):
        total_err = 0
        for i, x in enumerate(X):
            if (np.dot(X[i], w)*Y[i]) <= 0:
                total_err += (np.dot(X[i], w)*Y[i])
                b = eta*X[i]*Y[i]
                w = w + b
        errors.append(total_err*-1)
        # print(w)
        writer.writerow([w, b])
        #Record each weight in the output file

    plt.plot(errors)
    plt.xlabel('Epoch')
    plt.ylabel('Total Loss')
    # plt.show()

    return w


if __name__ == '__main__':
    input_data = sys.argv[1]
    output_data = sys.argv[2]

    inputFile = open(input_data, 'rb')
    outputFile = open(output_data, 'wb')
    writer = csv.writer(outputFile)
    # writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #Creating dataframe of input1.csv
    df = pd.read_csv(inputFile,  names=['feature_1','feature_2','label'])
    # print(df)
    numpyMatrix = df.as_matrix()
    # print(numpyMatrix)

    labels = df['label']
    labels = labels.as_matrix()
    # print(labels)

    #Call PLA
    w = perceptron_sigmoid(numpyMatrix, labels)
    # print(w)
