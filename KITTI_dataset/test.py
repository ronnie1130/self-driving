from ultralytics import YOLO
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

# 載入模型
model = YOLO('runs/detect/train/weights/best.pt')

# 進行預測
results = model.val(data='data.yaml', save_json=True,save=True)

