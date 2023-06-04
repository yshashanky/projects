import cv2
import tensorflow as tf
import numpy as np
# import logging

# Configuring the logs
# logging.basicConfig(filename=r'cartoonization\app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.basicConfig(filename=r'cartoonization\app.log', filemode='w', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# logging.debug('This is a debug log message')
# logging.info('This is an info log message')
# logging.warning('This is a warning log message')

# Image path
imagePath = r'C:\Users\shash\Downloads\dd.png'

# Load the input image
image = cv2.imread(imagePath)

# Get the size of the image
height, width, channels = image.shape
print("Image size:", width, "x", height)

# Resize the image
width, height = 256, 256
resized_image = cv2.resize(image, (width, height))
height, width, channels = resized_image.shape
print("Image size:", width, "x", height)


# Load the CartoonGAN model
model_path = 'saved_models'
model = tf.saved_model.load(model_path)

# Preprocess the resized image
preprocessed_image = np.expand_dims(resized_image.astype(np.float32) / 255.0, axis=0)

# Apply the CartoonGAN filter
output = model(preprocessed_image)['output'][0]

# Convert the output tensor to an image
output_image = (output * 255).numpy().astype(np.uint8)
# Perform post-processing if needed (e.g., adjusting colors, adding effects)

# Save the output image
output_path = 'output_image.jpg'
cv2.imwrite(output_path, output_image)
