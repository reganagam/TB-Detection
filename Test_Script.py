import tensorflow as tf
import numpy as np
import gradio as gr

model = tf.keras.models.load_model('Model_H5/model.h5')

def predict_image(img):
  imgs = tf.keras.preprocessing.image.img_to_array(img)/255
  x = np.expand_dims(imgs, axis=0)
  prediction = model.predict(x)
  percentage = float(prediction)
  if percentage > 0.55:
    result = 'Tuberculosis'
  else:
    result = 'Normal'
  return {result: percentage}

image = gr.inputs.Image(shape=(224,224))
label = gr.outputs.Label(num_top_classes=2)

gr.Interface(fn=predict_image, inputs=image, outputs=label, allow_flagging='auto').launch(debug='True')
