from ultralytics import YOLO
import cv2
import os
from PIL import Image

# 載入訓練好的模型
model = YOLO('/mnt/sdb/home/veronica/cv/runs/detect/train5/weights/best.pt')  # 確保這裡的 'best.pt' 是您訓練後的模型權重檔案

# 測試圖片的資料夾路徑
image_folder = '/mnt/sdb/home/veronica/cv/data/test/images'  # 替換為您的資料夾路徑

# from PIL
test_images = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

for img_path in test_images:
    # 讀取圖片
    img = Image.open(img_path)
    
    # 使用模型進行推論
    results = model.predict(source=img, save=True)
# test_images = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

# for img_path in test_images:
#     # 讀取圖片
#     img = cv2.imread(img_path)
    
#     # 使用模型進行推論
#     results = model(img)
    
#     # 繪製結果
#     for result in results:
#         annotated_img = result.plot()  # 使用 plot() 方法來繪製預測結果
#         cv2.imshow('Result', annotated_img)
#         cv2.waitKey(0)  # 按任意鍵關閉圖片視窗

# cv2.destroyAllWindows()