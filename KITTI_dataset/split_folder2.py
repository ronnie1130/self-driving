import os
import shutil

def split_folder2_based_on_folder1(folder1_train, folder1_test, folder2, output_train, output_test):
    # 確保輸出資料夾存在
    os.makedirs(output_train, exist_ok=True)
    os.makedirs(output_test, exist_ok=True)

    # 獲取資料夾1中的檔名
    train_files = os.listdir(folder1_train)
    test_files = os.listdir(folder1_test)

    # 將資料夾2中的檔案移動到相應的資料夾
    for file in train_files:
        if file in os.listdir(folder2):
            shutil.move(os.path.join(folder2, file), os.path.join(output_train, file))

    for file in test_files:
        if file in os.listdir(folder2):
            shutil.move(os.path.join(folder2, file), os.path.join(output_test, file))

# 設定資料夾路徑
folder1_train = 'C:/Users/Veronica/Desktop/CV-FinalProject/data/train_images'
folder1_test = 'C:/Users/Veronica/Desktop/CV-FinalProject/data/test_images'
folder2 = 'C:/Users/Veronica/Desktop/CV-FinalProject/data/training/processed_images'
output_train = 'C:/Users/Veronica/Desktop/CV-FinalProject/data/processed_train/images'
output_test = 'C:/Users/Veronica/Desktop/CV-FinalProject/data/processed_test/images'

# 執行分割
split_folder2_based_on_folder1(folder1_train, folder1_test, folder2, output_train, output_test) 