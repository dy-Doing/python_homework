
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_file_path = 'ex1data1.txt'
# Reading a csv into Pandas
human_data = pd.read_csv(data_file_path, header=None, names=['Population', 'Profit'])
# print(human_data.head(6))
# print('lines:')
# print(len(human_data))
# human_data.describe()
# print(human_data.Profit)
human_data.plot(kind='scatter', x='Population', y='Profit', figsize=(12, 8))
# plt.show()

def computeCost(X, y, theta):
    inner = np.power(((X * theta.T) - y), 2)
    return np.sum(inner) / (2 * len(X))


human_data.insert(0, 'ones', 1)
print(human_data.head(20))
cols = human_data.shape[1]
X = human_data.iloc[:, 0:cols-1]

y = human_data.iloc[:, cols-1:cols]
X = np.matrix(X.values)
y = np.matrix(y.values)
theta = np.matrix(np.array([0, 0]))


def gradientDescent(X, y, theta, alpha, iters):
    temp = np.matrix(np.zeros(theta.shape))
    parameters = int(theta.ravel().shape[1])
    cost = np.zeros(iters)

    for i in range(iters):
        error = (X * theta.T) - y

        for j in range(parameters):
            term = np.multiply(error, X[:, j])
            temp[0, j] = theta[0, j] - ((alpha / len(X)) * np.sum(term))

        theta = temp
        cost[i] = computeCost(X, y, theta)

    return theta, cost


alpha = 0.01
iters = 800
g, cost = gradientDescent(X, y, theta, alpha, iters)
print(computeCost(X, y, g))
x = np.linspace(human_data.Population.min(), human_data.Population.max(), 100)
f = g[0, 0] + (g[0, 1] * x)

fig, ax = plt.subplots(figsize=(12,8))
ax.plot(x, f, 'r', label='Prediction')
ax.scatter(human_data.Population, human_data.Profit, label='Traning Data')
ax.legend(loc=2)
ax.set_xlabel('Population')
ax.set_ylabel('Profit')
ax.set_title('Predicted Profit vs. Population Size')
plt.show()

