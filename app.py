from flask import Flask,request
import flask
import numpy as np
import io, base64
from PIL import Image
import tensorflow as tf
import tensorflow
from PIL import Image
from tensorflow import keras
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.imagenet_utils import preprocess_input
import pickle
# Assuming base64_str is the string value without 'data:image/jpeg;base64,'

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['POST','GET','OPTIONS'])
def home():

    
    data=request.get_data()
    rawIO = io.BytesIO(data)
    byteImg = Image.open(rawIO)
    #sending image to frontend
    byteImg.save('test.png', 'PNG')
    n_model=tf.keras.models.load_model("my_model.h5")
    my_image= load_img('test.png',target_size=(160,160))
    print(my_image)
    my_image= img_to_array(my_image)
    # print(my_image)
    my_image=my_image.reshape(1,160,160,3)
    print(my_image)
    labels = ['Dog', 'Cat']
    def preds(probs):
      if probs > 0.5:
        return "This is a "+labels[1]
      else :
        return "This is a "+labels[0]
    myresult= n_model.predict(my_image)
    res = flask.Response([str(myresult[0][0]),preds(myresult[0][0])])
    res.headers["Access-Control-Allow-Origin"] = "*"
    print('....................',preds(myresult[0][0]),'...................')
    
    return res

app.run()