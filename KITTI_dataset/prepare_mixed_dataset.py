import os
import shutil
import random
from weather_augmentation import add_rain, add_fog
import cv2
import numpy as np

def prepare_mixed_dataset(
    original_dir,          # 原始資料目錄
    output_dir,           # 輸出目錄
    split_ratio={
        'original': 0.5,   # 原始資料
        'rain': 0.2,      # 一般雨天
        'heavy_rain': 0.15,# 大雨
        'fog': 0.15       # 霧天
    }
):
    # 創建輸出目錄結構
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'processed_image'), exist_ok=True)    

    # 獲取所有原始圖片
    image_files = [f for f in os.listdir(original_dir) if f.endswith(('.png'))]
    total_images = len(image_files)
    
    print(f"找到 {total_images} 張原始圖片")

    # 計算每種類型需要的圖片數量
    counts = {
        k: int(v * total_images) for k, v in split_ratio.items()
    }

    # 隨機選擇圖片進行處理
    random.shuffle(image_files)
    processed = 0

    # 1. 複製原始資料
    original_count = counts['original']
    original_images = image_files[:original_count]
    for img_file in original_images:
        # 複製圖片
        src_img = os.path.join(original_dir, img_file)
        dst_img = os.path.join(output_dir, 'processed_image', img_file)
        shutil.copy2(src_img, dst_img)
        
        processed += 1
        print(f"處理進度: {processed}/{total_images} - 複製原始圖片: {img_file}")

    # 2. 處理天氣效果
    weather_images = image_files[original_count:]
    current_idx = 0

    # 一般雨天
    rain_count = counts['rain']
    for i in range(rain_count):
        img_file = weather_images[current_idx + i]
        image = cv2.imread(os.path.join(original_dir, img_file))
        if image is None:
            continue
            
        # 添加雨天效果
        rain_image = add_rain(image.copy(), "drizzle")
        new_name = img_file
        cv2.imwrite(os.path.join(output_dir, 'processed_image', new_name), rain_image)
        
        processed += 1
        print(f"處理進度: {processed}/{total_images} - 添加雨天效果: {new_name}")
    
    current_idx += rain_count

    # 大雨
    heavy_rain_count = counts['heavy_rain']
    for i in range(heavy_rain_count):
        img_file = weather_images[current_idx + i]
        image = cv2.imread(os.path.join(original_dir, img_file))
        if image is None:
            continue
            
        # 添加大雨效果
        heavy_rain_image = add_rain(image.copy(), "heavy")
        new_name = img_file
        cv2.imwrite(os.path.join(output_dir, 'processed_image', new_name), heavy_rain_image)
      
        processed += 1
        print(f"處理進度: {processed}/{total_images} - 添加大雨效果: {new_name}")
    
    current_idx += heavy_rain_count

    # 霧天
    fog_count = counts['fog']
    for i in range(fog_count):
        img_file = weather_images[current_idx + i]
        image = cv2.imread(os.path.join(original_dir, img_file))
        if image is None:
            continue
            
        # 添加霧天效果
        fog_image = add_fog(image.copy())
        new_name = img_file
        cv2.imwrite(os.path.join(output_dir, 'processed_image', new_name), fog_image)
        
        processed += 1
        print(f"處理進度: {processed}/{total_images} - 添加霧天效果: {new_name}")

    print("\n資料集處理完成!")
    print(f"總圖片數: {processed}")
    print(f"原始圖片: {original_count}")
    print(f"雨天圖片: {rain_count}")
    print(f"大雨圖片: {heavy_rain_count}")
    print(f"霧天圖片: {fog_count}")

if __name__ == "__main__":
    # 設定路徑
    original_dir = "C:/Users/Veronica/Desktop/CV-FinalProject/data/training/images"  # 原始圖片目錄
    output_dir = "C:/Users/Veronica/Desktop/CV-FinalProject/data/training"     # 輸出目錄
    
    # 執行資料集準備
    prepare_mixed_dataset(original_dir, output_dir) 