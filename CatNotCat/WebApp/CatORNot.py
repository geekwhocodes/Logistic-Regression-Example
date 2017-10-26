# coding: utf-8
import os
import numpy as np
import scipy
from PIL import Image
import pickle

# In[106]:

def sigmoid(x):
    return 1/(1+ np.exp(-x))
# In[122]:

def predict(W,b,X):
    """ Predicts output """

    m = X.shape[1]

    predictions = np.zeros((1,m))
    W = W.reshape(X.shape[0], 1)
    yHat = sigmoid(np.dot(W.T, X) + b)
    
    for i in range(yHat.shape[1]):
        if yHat[0,i] <= 0.5 :
            predictions[0,i] = 0
        else:
            predictions[0,i] = 1
    
    return predictions

model_dir = "models"
if not os.path.exists(model_dir):
    os.makedirs(model_dir)
    
def saveModel(params, name):
    f = open( model_dir + '/' + name + ".model", "wb" )
    pickle.dump( params,f )
    f.close()


def loadModel(name):
    f = open(model_dir + '/' + name + ".model", "rb")
    model = pickle.load(f)
    f.close()
    return model

def get_predction(data):
    size = 64
    channel = 3
    model = loadModel('cat__lr0_01__iter_1000')

    ## resize img
    new_img = data.resize((size,size), Image.ANTIALIAS)
    img_norm = np.array(new_img)/255
    img_input = img_norm.reshape(size*size*channel,1)
    yhat = np.squeeze(predict(model["W"], model["b"],img_input))
    return 1 if yhat == 1 else 0


