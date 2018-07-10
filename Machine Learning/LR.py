import numpy as np
import pandas as pd
import sys
import csv
import matplotlib.pyplot as plt

#t0 - intercept
#t1 - slope (computed as a 2-d matrix)

#Compute cost function to fit to Gradient descent
def cost_func(n, t0, t1, x, y):
    return 1/2/n * sum([(t0 + t1[0]*np.asarray([x.iloc[0][i]]) + t1[1]*np.asarray([x.iloc[0][i]]) - y[i])**2 for i in range(n)])


#Finding the gradient descent
def gradient_descent(alpha, x, y, ep=0.0001, max_iter=1500):
    isconverged = False
    iter = 0
    n = x.shape[0]  #number of samples

    #initial values of theta
    t0 = 0
    t1 = [0,0]

    #total error, B(theta)
    B = cost_func(n, t0, t1, x, y)
    # print('B=',B);

    while not isconverged:
        #Compute the gradient descent for each training sample (x1 and x2)

        graddesc0 = 1.0/n * sum([(t0 + t1[0]*np.asarray([x.iloc[0][i]]) + t1[1]*np.asarray([x.iloc[0][i]]) - y[i]) for i in range(n)])
        graddesc1 = 1.0/n * sum([(t0 + t1[0]*np.asarray([x.iloc[0][i]]) + t1[1]*np.asarray([x.iloc[0][i]]) - y[i])*np.asarray([x.iloc[0][i]]) for i in range(n)])

        #Update theta
        temp0 = t0 - alpha * graddesc0
        temp1 = t1 - alpha * graddesc1

        t0 = temp0
        t1 = temp1

        #Mean squared error
        e = cost_func(n, t0, t1, x, y)
        print('B = ', e)
        B = e
        iter += 1

        if iter == max_iter:
            print('Max iteration exceeded')
            isconverged = True

    return t0,t1


if __name__ == '__main__':
    input_data = sys.argv[1]
    output_data = sys.argv[2]

    inputFile = open(input_data, 'rb')
    outputFile = open(output_data, 'wb')
    writer = csv.writer(outputFile)
    writer.header()

    iter = 0
    # Load input2.csv dataset as a DataFrame using pandas
    df = pd.read_csv('input2.csv', names=['age', 'weight', 'height'])

    # Scale the dataset
    mean_age = df[['age']].mean()
    stdev_age = df[['age']].std()
    mean_weight = df[['weight']].mean()
    stdev_weight = df[['weight']].std()

    scaled_age = (df[['age']] - mean_age) / stdev_age
    scaled_weight = (df[['weight']] - mean_weight) / stdev_weight
    # print(scaled_weight.describe())
    # print(scaled_age.describe())

    df['age'] = scaled_age
    df['weight'] = scaled_weight
    # print(df)

    #2-d matrix of features 1 and 2
    x = scaled_age
    x.columns = ["age"]
    x['weight'] = scaled_weight
    # print(x)

    y = df['height']

    # Values for alpha
    alpha_values = [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 1.5, 10]

    #Run Linear Regression for all values of alpha
    for iter in alpha_values:
        alpha = iter  # learning rate
        ep = 0.01  # criteria for convergence

        #Call gradient descent function to get intercept(=theta0) and slope(=theta1)
        theta0, theta1 = gradient_descent(alpha, x, y, ep, max_iter=100)

        #Get predicted value of height now
        for i in range(x.shape[0]):
            y_predict = theta0 + theta1 * x

        #Finally print the value of predicted height (write into output2.csv)
        print(y_predict)
