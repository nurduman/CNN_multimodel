import os
import numpy as np
import shutil

def split_to_3(train_div, valid_div, test_div):
    # # Creating Train / Val / Test folders (One time use)
    root_dir = '/home/olzhas_ubuntu/Downloads/main_dataset/main_dataset/folderthree'
    healthy = '/Healthy'
    sick = '/Sick'

    classes=[healthy,sick]
    if os.path.exists(root_dir +'/train'):
        shutil.rmtree(root_dir +'/train')
        print("Deleted folders. Creating new ones...")
    if os.path.exists(root_dir +'/test'):
        shutil.rmtree(root_dir +'/test')
        print("Deleted folders. Creating new ones...")
    if os.path.exists(root_dir +'/val'):
        shutil.rmtree(root_dir +'/val')
        print("Deleted folders. Creating new ones...")
        
    os.makedirs(root_dir +'/train' + healthy)
    os.makedirs(root_dir +'/train' + sick)
    os.makedirs(root_dir +'/val' + healthy)
    os.makedirs(root_dir +'/val' + sick)
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
                    [int(len(allFileNames)*train_div), 
                    int(len(allFileNames)*(train_div+valid_div))])


        train_FileNames = [src+'/'+ name for name in train_FileNames.tolist()]
        val_FileNames = [src+'/' + name for name in val_FileNames.tolist()]
        test_FileNames = [src+'/' + name for name in test_FileNames.tolist()]

        print('Total images: ', len(allFileNames))
        print('Training: ', len(train_FileNames))
        print('Validation: ', len(val_FileNames))
        print('Testing: ', len(test_FileNames))

        # Copy-pasting images
        for name in train_FileNames:
            shutil.copy(name, "/home/olzhas_ubuntu/Downloads/main_dataset/main_dataset/folderthree/train"+currentCls)

        for name in val_FileNames:
            shutil.copy(name, "/home/olzhas_ubuntu/Downloads/main_dataset/main_dataset/folderthree/val"+currentCls)

        for name in test_FileNames:
            shutil.copy(name, "/home/olzhas_ubuntu/Downloads/main_dataset/main_dataset/folderthree/test"+currentCls)
def split_to_2(train_div, test_div):
    # Creating Train / Test folders (One time use)
    root_dir = '/home/olzhas_ubuntu/Downloads/main_dataset/main_dataset/folder'
    healthy = '/Healthy'
    sick = '/Sick'

    classes=[healthy,sick]
    if os.path.exists(root_dir +'/train'):
        shutil.rmtree(root_dir +'/train')
        print("deleted folders")
    if os.path.exists(root_dir +'/test'):
        shutil.rmtree(root_dir +'/test')
        print("deleted folders")
    if os.path.exists(root_dir +'/val'):
        shutil.rmtree(root_dir +'/val')
        print("deleted folders")
        
    os.makedirs(root_dir +'/train' + healthy)
    os.makedirs(root_dir +'/train' + sick)
    os.makedirs(root_dir +'/test' + healthy)
    os.makedirs(root_dir +'/test' + sick)

    # Creating partitions of the data after shuffeling
    for each in classes:
        currentCls = each
        src = "/home/olzhas_ubuntu/Downloads/main_dataset/main_dataset"+currentCls # Folder to copy images from

        allFileNames = os.listdir(src)
        np.random.shuffle(allFileNames)
        train_FileNames, test_FileNames = np.split(
            np.array(allFileNames),
                    [int(len(allFileNames)*train_div)])


        train_FileNames = [src+'/'+ name for name in train_FileNames.tolist()]
        test_FileNames = [src+'/' + name for name in test_FileNames.tolist()]

        print('Total images: ', len(allFileNames))
        print('Training: ', len(train_FileNames))
        print('Testing: ', len(test_FileNames))

        # Copy-pasting images
        for name in train_FileNames:
            shutil.copy(name, "/home/olzhas_ubuntu/Downloads/main_dataset/main_dataset/folder/train"+currentCls)

        for name in test_FileNames:
            shutil.copy(name, "/home/olzhas_ubuntu/Downloads/main_dataset/main_dataset/folder/test"+currentCls)
