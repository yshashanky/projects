import h5py

# Open the .h5 file
file = h5py.File(r'cartoonizer\pretrainedModel_code\output_data.h5', 'r')

# List the keys (dataset names) in the file
keys = list(file.keys())
print("Datasets in the .h5 file:", keys)

# Print the dataset names
for dataset_name in keys:
    dataset = file[dataset_name]  # Replace 'dataset_name' with the actual dataset name
    data = dataset[()]
    print(dataset_name)
    print("Shape of the data:", data.shape)

# Close the .h5 file
file.close()
