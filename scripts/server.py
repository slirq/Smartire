from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
import argparse
import json,os,cv2
from typing import Tuple, List
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# model = tf.keras.models.load_model('models/resnet50.h5',compile = False)
model = tf.keras.models.load_model('../models/model_tire_dense.h5',compile = False)
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])

app = Flask(__name__)  # creates a Flask application instance

@app.route('/', methods=['POST','GET'])
def predict():
    # Get the image file from the request
    img_file = request.files['image']  # gets the image file from the request
    
    print('Image recieved from client!')  # prints a message indicating that the image has been received from the client
    
    img_file.save(os.path.join(img_file.filename))  # saves the image file
    
    img = np.resize(cv2.imread('./image.jpg')/255.0,(1,256,256,3))
    op = np.argmax(model.predict(img))# recognizes the text in the image using the model

    # Return the text as a JSON response
    if op==1:
        text='Defective Tyre! Please get your Tyres changed!' # check for valid text
    else:
        text='The Tyre is in Good Shape!'
        
    print("output= ",op,"\ntext= ",text)    
    return jsonify({'text': text})  # returns the recognized text as a JSON response

if __name__ == '__main__':

    app.run(host="192.168.2.185", port=5000, debug=True) #run server