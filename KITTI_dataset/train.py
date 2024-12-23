from ultralytics import YOLO

# 載入模型
model = YOLO('yolov8n.pt')

# 開始訓練
model.train(
    data='data.yaml',  # 使用相對路徑
    epochs=100,
    device=0,        # 使用第一個 GPU
    batch=16,        # 可以根據 GPU 記憶體大小調整
    imgsz=640,       # 圖片大小
    workers=8,       # 資料載入的工作程序數
    verbose=True     # 顯示詳細訓練資訊
)

model.val()
