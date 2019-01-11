import keras1
import numpy as np
import time
import argparse
import math
import keyboard
from osc import OscClient
from osc import OscServer
from keras1 import NeuralNetRegression

#parameters
inputdimension  = 2
outputdimension = 11025
nHidden = 10
nNodes = 100
epochs = 1000

trained = 0
nExamples = 0
x = np.array([0])
y = np.array([0])
oscserverxin = 0
oscclient = OscClient("127.0.0.1",12000,'/keras/Yout')
oscserver = OscServer("127.0.0.1",6448,'/keras/Xin','/keras/Yin')
print("\+q: quit")

while True:
    time.sleep(0.1)
    if trained == 1:
        xin = np.array([oscserver.xin])
        yout = nn.predict(xin)
        yout = yout.tolist()
        oscclient.sendMsg(yout)
        oscserverxin = oscserver.xin
    try: 
        if oscserver.addexample == 1:
            if(nExamples==0):
                x = oscserver.xin
                y = oscserver.yin
            else:
                x = np.vstack((x,oscserver.xin))
                y = np.vstack((y,oscserver.yin))
            print(x)
            print(y)
            nExamples += 1
            print("Added Example")
            print("Number of Examples:", nExamples)
            print("\+q: quit")
            oscserver.addexample = 0
            pass
        if oscserver.delexample == 1:
            nExamples -= 1
            x = x[:-1]
            y = y[:-1]
            print(x)
            print(y)
            if(nExamples<0):nExamples=0
            print("Removed Example")
            print("Number of Examples:", nExamples)
            print("\+q: quit")
            oscserver.delexample = 0
            pass
        if oscserver.delall == 1:
            nExamples = 0
            x = np.array([0])
            y = np.array([0])
            print("Removed All Example")
            print("Number of Examples:", nExamples)
            print("\+q: quit")
            oscserver.delall = 0
        if oscserver.train == 1:
            # train
            if(nExamples > 1):
                nn = NeuralNetRegression(x,y,nHidden,nNodes)
                nn.train(x,y,nExamples,epochs)
                trained = 1
                oscserver.train = 0
            else:
                print("no Examples found. Need atleast 2 Examples to Train")
                print("\+q: quit")
                oscserver.train = 0
            pass
        if keyboard.is_pressed('\+q'): 
            oscserver.server.shutdown()
            quit()
            break
        if oscserver.quit == 1:
            oscserver.server.shutdown()
            quit()
            break
        else:
            pass
    except:
        oscserver.server.shutdown()
        quit()
        break