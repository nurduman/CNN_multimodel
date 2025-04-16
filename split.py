import os
import numpy as np
import shutil

# # Creating Train / Val / Test folders (One time use)
root_dir = '/home/olzhas_ubuntu/Downloads/main_dataset/main_dataset'
healthy = '/Healthy'
sick = '/Sick'

classes=[healthy,sick]

os.makedirs(root_dir +'/train' + healthy)
os.makedirs(root_dir +'/train' + sick)
os.makedirs(root_dir +'/val' + healthy)
os.makedirs(root_dir +'ffFF/val' + sick)
os.makedirs(root_dir +'/test' + healthy)
os.makedirs(root_dir +'/test' + sick)

# Creating partitions of the data after shuffeling
for each in classes:
    currentCls = each
    src = "/home/olzhas_ubuntu/Downloads/main_dataset/main_dataset"+currentCls # Folder to copy images from

    allFileNames = os.listdir(src)
    np.random.shuffle(allFileNames)
    train_FileNames, val_FileNames, test_FileNames = np.split(
        np.array(allFileNames),
                [int(len(allFileNames)*0.7), 
                int(len(allFileNames)*0.8)])


    train_FileNames = [src+'/'+ name for name in train_FileNames.tolist()]
    val_FileNames = [src+'/' + name for name in val_FileNames.tolist()]
    test_FileNames = [src+'/' + name for name in test_FileNames.tolist()]

    print('Total images: ', len(allFileNames))
    print('Training: ', len(train_FileNames))
    print('Validation: ', len(val_FileNames))
    print('Testing: ', len(test_FileNames))

    # Copy-pasting images
    for name in train_FileNames:
        shutil.copy(name, "/home/olzhas_ubuntu/Downloads/main_dataset/main_dataset/train"+currentCls)

    for name in val_FileNames:
        shutil.copy(name, "//home/olzhas_ubuntu/Downloads/main_dataset/main_dataset/val"+currentCls)

    for name in test_FileNames:
        shutil.copy(name, "/home/olzhas_ubuntu/Downloads/main_dataset/main_dataset/test"+currentCls)
