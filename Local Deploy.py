import tensorflow as tf
import numpy as np
import gradio as gr

model = tf.keras.models.load_model('Model/model_A.h5')
class_name = ['Covid-19', 'Normal', 'Tuberculosis']

def predict_image(img):
  imgs = tf.keras.preprocessing.image.img_to_array(img)/255
  x = np.expand_dims(imgs, axis=0)
  predict = model.predict(x)
  predict = np.array(predict)
  list_predict = predict.tolist()[0]
  return {class_name[i]: list_predict[i] for i in range(3)}

image = gr.inputs.Image(shape=(150,150))
label = gr.outputs.Label(num_top_classes=3)

description = "Let's check your condition using your chest X-Ray image!"
title = "Tuberculosis (TB) Detection Using Chest X-Ray"
example = ["Images/normal.png",
           "Images/tb.png",
           "Images/covid.png",
           "Images/tb(1).png",
           "Images/covid(1).png",
           "Images/normal(1).png",
           "Images/tb(3).png"]

interface = gr.Interface(
    fn=predict_image,
    inputs=image,
    outputs=label,
    allow_flagging='auto',
    description=description,
    title=title,
    examples=example)

interface.launch(debug='True')
