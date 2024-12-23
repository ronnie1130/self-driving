import os
import glob
import time

def convert_kitti_to_yolo(kitti_label_path, image_width, image_height, output_path):
    print(f"\n處理標籤檔案: {os.path.basename(kitti_label_path)}")
    print(f"圖片尺寸: {image_width}x{image_height}")
    
    class_mapping = {
         "pedestrian": 1,
        "rider": 2,
        "car": 3,
        "truck": 4,
        "bus": 5,
        "train": 6,
        "motorcycle": 7,
        "bicycle": 8,
        "traffic light": 9,
        "traffic sign": 10
    }
    
    with open(kitti_label_path, 'r') as f:
        lines = f.readlines()
    
    print(f"找到 {len(lines)} 個物件")
    
    yolo_labels = []
    skipped_objects = 0
    for i, line in enumerate(lines, 1):
        parts = line.strip().split(' ')
        
        # 獲取類別和邊界框資訊
        class_name = parts[0]
        if class_name not in class_mapping:
            print(f"警告: 未知類別 '{class_name}'，跳過")
            skipped_objects += 1
            continue
            
        class_id = class_mapping[class_name]
        
        try:
            # 獲取邊界框座標 (KITTI format: left, top, right, bottom)
            left = float(parts[4])
            top = float(parts[5])
            right = float(parts[6])
            bottom = float(parts[7])
            
            # 計算 YOLO 格式的值
            center_x = ((left + right) / 2) / image_width
            center_y = ((top + bottom) / 2) / image_height
            width = (right - left) / image_width
            height = (bottom - top) / image_height
            
            # 確保值在 0-1 範圍內
            center_x = min(max(center_x, 0.0), 1.0)
            center_y = min(max(center_y, 0.0), 1.0)
            width = min(max(width, 0.0), 1.0)
            height = min(max(height, 0.0), 1.0)
            
            yolo_labels.append(f"{class_id} {center_x:.6f} {center_y:.6f} {width:.6f} {height:.6f}")
            print(f"轉換物件 {i}/{len(lines)}: {class_name} -> class_id={class_id}")
            
        except (IndexError, ValueError) as e:
            print(f"錯誤: 處理第 {i} 行時發生錯誤: {str(e)}")
            print(f"問題行內容: {line.strip()}")
            continue
    
    # 寫入 YOLO 格式的標籤檔
    with open(output_path, 'w') as f:
        f.write('\n'.join(yolo_labels))
    
    print(f"\n轉換完成:")
    print(f"- 成功轉換: {len(yolo_labels)} 個物件")
    print(f"- 跳過: {skipped_objects} 個物件")
    print(f"- 輸出檔案: {output_path}")

def process_dataset(kitti_base_path, output_base_path):
    """處理整個資料集"""
    
    print(f"\n開始處理資料集")
    print(f"輸入路徑: {kitti_base_path}")
    print(f"輸出路徑: {output_base_path}")
    
    # 創建輸出目錄
    os.makedirs(output_base_path, exist_ok=True)
    
    # 處理所有標籤檔
    label_files = glob.glob(os.path.join(kitti_base_path, '*.txt'))
    total_files = len(label_files)
    
    print(f"\n找到 {total_files} 個標籤檔案")
    
    start_time = time.time()
    processed_files = 0
    failed_files = 0
    
    for label_file in label_files:
        try:
            # 獲取對應的圖片檔名
            base_name = os.path.basename(label_file)
            image_file = os.path.join(os.path.dirname(kitti_base_path), 'images', base_name.replace('.txt', '.png'))
            
            # 檢查圖片是否存在
            if not os.path.exists(image_file):
                print(f"\n警告: 找不到圖片: {image_file}")
                failed_files += 1
                continue
            
            # 讀取圖片尺寸
            from PIL import Image
            with Image.open(image_file) as img:
                width, height = img.size
            
            # 轉換標籤
            output_label = os.path.join(output_base_path, base_name)
            convert_kitti_to_yolo(label_file, width, height, output_label)
            
            processed_files += 1
            
            # 顯示進度
            elapsed_time = time.time() - start_time
            avg_time = elapsed_time / processed_files
            remaining_files = total_files - processed_files
            estimated_time = avg_time * remaining_files
            
            print(f"\n進度: {processed_files}/{total_files} ({processed_files/total_files*100:.1f}%)")
            print(f"預估剩餘時間: {estimated_time/60:.1f} 分鐘")
            
        except Exception as e:
            print(f"\n錯誤: 處理檔案 {label_file} 時發生錯誤:")
            print(str(e))
            failed_files += 1
            continue
    
    # 顯示最終統計
    total_time = time.time() - start_time
    print(f"\n處理完成!")
    print(f"總處理時間: {total_time/60:.1f} 分鐘")
    print(f"成功處理: {processed_files} 個檔案")
    print(f"失敗: {failed_files} 個檔案")

if __name__ == "__main__":
    # 設定路徑
    kitti_path = "C:/Users/Veronica/Desktop/CV-FinalProject/data/training/label"  # KITTI 資料集路徑
    yolo_path = "C:/Users/Veronica/Desktop/CV-FinalProject/data/training/yolo_label"     # 輸出的 YOLO 標籤路徑
    
    try:
        process_dataset(kitti_path, yolo_path)
    except Exception as e:
        print(f"\n程式執行時發生錯誤:")
        print(str(e)) 