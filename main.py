from flask import Flask,request,jsonify
import numpy as np
import pickle


model=pickle.load(open('model.pkl','rb'))


def main(arr):
    arr = np.array(arr).reshape(1, -1)
    pred=model.predict(arr)[0]
    return pred

