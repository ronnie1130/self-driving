import os
import shutil
import random

def split_dataset(images_dir, labels_dir, base_dir, train_ratio=0.8):
    train_images_dir = os.path.join(base_dir, 'train_images')
    train_labels_dir = os.path.join(base_dir, 'train_labels')
    test_images_dir = os.path.join(base_dir, 'test_images')
    test_labels_dir = os.path.join(base_dir, 'test_labels')

    os.makedirs(train_images_dir, exist_ok=True)
    os.makedirs(train_labels_dir, exist_ok=True)
    os.makedirs(test_images_dir, exist_ok=True)
    os.makedirs(test_labels_dir, exist_ok=True)

    all_images = [f for f in os.listdir(images_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]
    random.shuffle(all_images)

    split_index = int(len(all_images) * train_ratio)

    train_images = all_images[:split_index]
    test_images = all_images[split_index:]

    for file in train_images:
        shutil.move(os.path.join(images_dir, file), os.path.join(train_images_dir, file))
        label_file = file.replace('.png', '.txt').replace('.jpg', '.txt').replace('.jpeg', '.txt')
        shutil.move(os.path.join(labels_dir, label_file), os.path.join(train_labels_dir, label_file))
    
    for file in test_images:
        shutil.move(os.path.join(images_dir, file), os.path.join(test_images_dir, file))
        label_file = file.replace('.png', '.txt').replace('.jpg', '.txt').replace('.jpeg', '.txt')
        shutil.move(os.path.join(labels_dir, label_file), os.path.join(test_labels_dir, label_file))

    print(f"訓練集圖片大小: {len(train_images)}")
    print(f"測試集圖片大小: {len(test_images)}")

images_directory = 'C:/Users/Veronica/Desktop/CV-FinalProject/data/training/images'
labels_directory = 'C:/Users/Veronica/Desktop/CV-FinalProject/data/training/labels'
base_directory = 'C:/Users/Veronica/Desktop/CV-FinalProject/data'

split_dataset(images_directory, labels_directory, base_directory) 