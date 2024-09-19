from pathlib import Path
import os
import random
import shutil

base_path = Path(__file__).parent.resolve()
print(base_path)

def split_dataset(base_path,dataset_path,split_data_path,train_ratio=0.6,val_ratio=0.2,test_ratio=0.2):
    """
       split the dataset into train test val folder
    Args:
        base_path (string): absolute path of the specific folder
        dataset_path (string): orginal dataset under the specific folder 
        split_data_path (string): splited dataset under the specific folder
        train_ratio(float): train ratio
        val_ratio(float):val_ratio
        test_ratio(float):test_ratio
    """
 
    dataset_path = base_path/dataset_path
    images_path = dataset_path/"images"
    labels_path = dataset_path/"labels"

    splited_data_path = base_path/split_data_path
    
    for folder in ["train","val","test"]:
        (splited_data_path/"images"/folder).mkdir(parents=True,exist_ok=True)
        (splited_data_path/"labels"/folder).mkdir(parents=True,exist_ok=True)

    # 获取所有图片文件名
    image_files = list(images_path.glob('*.png'))
    random.shuffle(image_files)

    train_size = int(len(image_files)*train_ratio)
    val_size = int(len(image_files)*val_ratio)
    test_size = int(len(image_files)*test_ratio)

    train_files = image_files[:train_size]
    val_files = image_files[train_size:train_size+val_size]
    test_files = image_files[train_size+val_size:]
    
    copy_file(train_files,labels_path,splited_data_path,"train")
    copy_file(val_files,labels_path,splited_data_path,"val")
    copy_file(test_files,labels_path,splited_data_path,"test")

 

    


def copy_file(file_list,labels_path,dest_data_path:Path,data_type:str):
    for file in file_list:
        des_image_path = dest_data_path/"images"/data_type/file.name
        shutil.copy(str(file),str(des_image_path))
        label_file = labels_path/file.with_suffix(".txt").name
        dest_label_path = dest_data_path/"labels"/data_type/label_file.name
        shutil.copy(str(label_file),str(dest_label_path))




if __name__ == "__main__":
    split_dataset(base_path,"car_data_v2","splited_dataset")
