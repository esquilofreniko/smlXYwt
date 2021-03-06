import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from keras.models import Sequential
from keras.layers import Dense
from sklearn.datasets import make_regression
from sklearn.preprocessing import MinMaxScaler

class NeuralNetRegression:
    def __init__(self,x,y,nHidden,nNodes):
        # generate regression dataset
        self.x = x
        self.y = y
        self.inputdimension  = self.x.shape[1]
        self.outputdimension = self.y.shape[1]
        self.nHidden = nHidden
        self.nNodes = nNodes
        self.model = Sequential()
        self.model.add(Dense(self.nNodes, input_dim=self.inputdimension, activation='relu'))
        for i in range(nHidden-1):
            self.model.add(Dense(self.nNodes, activation='relu'))
        self.model.add(Dense(self.outputdimension, activation='linear'))

    def train(self,x,y,nExamples,epochs):
        # define and fit the final model
        self.nExamples = nExamples
        self.epochs = epochs
        self.model.compile(loss='mse', optimizer='adam')
        self.model.fit(x, y, epochs=epochs,batch_size=self.nExamples,verbose=1)

    def predict(self,xin):
        # make a prediction
        self.xin = xin
        self.yout = self.model.predict(self.xin)
        return self.yout