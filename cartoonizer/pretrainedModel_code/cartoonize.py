import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
# from tensorflow.keras.applications import vgg19
# import tensorflow.keras.applications.vgg19 as vgg19

def cartoonize(load_folder, save_folder, model_path):
    # Load the VGG19 model
    vgg19 = tf.keras.applications.vgg19.VGG19(include_top=True, weights=None)
    # vgg19_weights = np.load(model_path, allow_pickle=True, encoding='latin1').item()
    # vgg19_weights = np.load(model_path, allow_pickle=True).item()['conv5_4'][0]
    # vgg19.set_weights(vgg19_weights)
    vgg19.load_weights(r'cartoonizer\pretrainedModel_code\output_data.h5')

    # Load and preprocess the input image
    input_image = tf.keras.preprocessing.image.load_img(load_folder, target_size=(224, 224))
    input_image = tf.keras.preprocessing.image.img_to_array(input_image)
    input_image = vgg19.preprocess_input(input_image)
    input_image = tf.expand_dims(input_image, axis=0)

    # Make predictions with VGG19
    predictions = vgg19.predict(input_image)
    decoded_predictions = vgg19.decode_predictions(predictions, top=5)[0]

    # Print the top predicted labels
    for _, label, confidence in decoded_predictions:
        print(label, confidence)

    # Save the processed image
    processed_image = input_image[0]
    plt.imshow(processed_image)
    plt.axis('off')
    plt.savefig('processed_image.jpg', bbox_inches='tight')

if __name__ == '__main__':
    model_path = r'C:\Users\shash\Local\projects\cartoonizer\pretrainedModel_code\vgg19_no_fc.npy'
    # load_folder = r'C:\Users\shash\Local\projects\cartoonizer\pretrainedModel_code\test_images'
    load_folder = r'C:\Users\shash\Local\projects\cartoonizer\pretrainedModel_code\actress2.jpg'
    save_folder = r'C:\Users\shash\Local\projects\cartoonizer\pretrainedModel_code\cartoonized_images'
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
    cartoonize(load_folder, save_folder, model_path)