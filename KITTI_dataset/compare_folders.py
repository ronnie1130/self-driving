import os

def compare_folders(folder1, folder2):
    # 獲取兩個資料夾中的檔案名稱
    files1 = set(os.listdir(folder1))
    files2 = set(os.listdir(folder2))

    # 找出在 folder1 中但不在 folder2 中的檔案
    only_in_folder1 = files1 - files2
    # 找出在 folder2 中但不在 folder1 中的檔案
    only_in_folder2 = files2 - files1

    # 輸出結果
    if only_in_folder1:
        print(f"檔案只在 {folder1} 中:")
        for file in only_in_folder1:
            print(file)
    else:
        print(f"所有檔案在 {folder1} 中也存在於 {folder2} 中。")

    if only_in_folder2:
        print(f"檔案只在 {folder2} 中:")
        for file in only_in_folder2:
            print(file)
    else:
        print(f"所有檔案在 {folder2} 中也存在於 {folder1} 中。")

# 設定資料夾路徑
folder1 = 'C:/Users/Veronica/Desktop/CV-FinalProject/data/processed_train/images'  # 第一個資料夾
folder2 = 'C:/Users/Veronica/Desktop/CV-FinalProject/data/train_images'  # 第二個資料夾

# 執行比較
compare_folders(folder1, folder2) 