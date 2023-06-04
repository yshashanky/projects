import h5py
import numpy as np

model_path = r'C:\Users\shash\Local\projects\cartoonizer\pretrainedModel_code\vgg19_no_fc.npy'

# Create a new .h5 file
output_file = h5py.File(r'cartoonizer\pretrainedModel_code\output_data.h5', 'w')

vgg19_weights = np.load(model_path, allow_pickle=True).item()['conv5_4'][0]

# Create a dataset in the .h5 file and write the array data
output_file.create_dataset('data', data=vgg19_weights)

# Close the .h5 file
output_file.close()
