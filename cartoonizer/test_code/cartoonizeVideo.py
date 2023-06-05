import cv2
import os
import os
import cv2
import numpy as np
# import tensorflow as tf 
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import network
import guided_filter
from tqdm import tqdm

def extract_frames(video_path, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Read the video file
    cap = cv2.VideoCapture(video_path)

    # Get the total number of frames
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Iterate over each frame and save it as an image file
    for frame_index in range(total_frames):
        # Read the frame
        ret, frame = cap.read()

        # Save the frame as an image file
        frame_path = os.path.join(output_folder, f"frame_{frame_index:05d}.jpg")
        cv2.imwrite(frame_path, frame)

    # Release the video capture object
    cap.release()

def resize_crop(image):
    h, w, c = np.shape(image)
    if min(h, w) > 720:
        if h > w:
            h, w = int(720*h/w), 720
        else:
            h, w = 720, int(720*w/h)
    image = cv2.resize(image, (w, h),
                       interpolation=cv2.INTER_AREA)
    h, w = (h//8)*8, (w//8)*8
    image = image[:h, :w, :]
    return image
    
def cartoonize(load_folder, save_folder, model_path):
    input_photo = tf.placeholder(tf.float32, [1, None, None, 3])
    network_out = network.unet_generator(input_photo)
    final_out = guided_filter.guided_filter(input_photo, network_out, r=1, eps=5e-3)

    all_vars = tf.trainable_variables()
    gene_vars = [var for var in all_vars if 'generator' in var.name]
    saver = tf.train.Saver(var_list=gene_vars)
    
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    sess = tf.Session(config=config)

    sess.run(tf.global_variables_initializer())
    saver.restore(sess, tf.train.latest_checkpoint(model_path))
    name_list = os.listdir(load_folder)
    for name in tqdm(name_list):
        try:
            load_path = os.path.join(load_folder, name)
            save_path = os.path.join(save_folder, name)
            image = cv2.imread(load_path)
            image = resize_crop(image)
            batch_image = image.astype(np.float32)/127.5 - 1
            batch_image = np.expand_dims(batch_image, axis=0)
            output = sess.run(final_out, feed_dict={input_photo: batch_image})
            output = (np.squeeze(output)+1)*127.5
            output = np.clip(output, 0, 255).astype(np.uint8)
            cv2.imwrite(save_path, output)
        except:
            print('cartoonize {} failed'.format(load_path))

def combine_frames(input_folder, output_path, output_fps):
    # Get the list of frame filenames in the input folder
    frame_filenames = sorted(os.listdir(input_folder))

    # Get the width and height of the first frame
    frame_path = os.path.join(input_folder, frame_filenames[0])
    frame = cv2.imread(frame_path)
    height, width, channels = frame.shape

    # Initialize the video writer
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_path, fourcc, output_fps, (width, height))

    # Iterate over each frame and write it to the video file
    for frame_filename in frame_filenames:
        frame_path = os.path.join(input_folder, frame_filename)
        frame = cv2.imread(frame_path)
        out.write(frame)

    # Release the video writer
    out.release()

if __name__ == '__main__':
    model_path = 'cartoonizer\\test_code\\saved_models'
    load_folder = 'cartoonizer\\test_code\\test_images'
    save_folder = 'cartoonizer\\test_code\\cartoonized_images'
    video_path = "cartoonizer\\test_code\\video.mp4"
    input_folder = "cartoonizer\\test_code\\cartoonized_images"
    output_video_path = "cartoonizer\\test_code\\output_video.mp4"

    # Extract frames from the video
    extract_frames(video_path, load_folder)

    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
    cartoonize(load_folder, save_folder, model_path)
    
    output_fps = 34  # Adjust the frame rate as per your requirements

    # Combine frames into a video
    combine_frames(input_folder, output_video_path, output_fps)