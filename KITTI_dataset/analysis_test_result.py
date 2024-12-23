import os
import cv2
import matplotlib.pyplot as plt

def draw_labels(image_path, labels):
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    for label in labels:
        class_id = int(label[0])
        x_center = int(label[1] * width)
        y_center = int(label[2] * height)
        bbox_width = int(label[3] * width)
        bbox_height = int(label[4] * height)

        # 計算邊界框的左上角和右下角坐標
        x1 = int(x_center - bbox_width / 2)
        y1 = int(y_center - bbox_height / 2)
        x2 = int(x_center + bbox_width / 2)
        y2 = int(y_center + bbox_height / 2)

        # 繪製邊界框
        cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(image, str(class_id), (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

def process_directory(image_dir, label_dir):
    for label_file in os.listdir(label_dir):
        if label_file.endswith('.txt'):
            # 獲取對應的圖片檔名
            image_file = label_file.replace('.txt', '.jpg')  # 假設圖片是 .jpg 格式
            image_path = os.path.join(image_dir, image_file)
            label_path = os.path.join(label_dir, label_file)

            # 讀取標籤
            with open(label_path, 'r') as f:
                content = f.readlines()
                labels = [list(map(float, line.strip().split())) for line in content]

            # 繪製標籤
            draw_labels(image_path, labels)

# 設定圖片和標籤的資料夾路徑
image_directory = 'runs/detect/predict2/images'  # 替換為實際圖片資料夾路徑
label_directory = 'runs/detect/predict2/labels'  # 替換為實際標籤資料夾路徑

# 處理整個資料夾
process_directory(image_directory, label_directory)