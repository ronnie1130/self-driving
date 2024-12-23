import os

images_dir = '/mnt/sdb/home/veronica/data/train_images'
images = [f for f in os.listdir(images_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]

print(f"Images count: {len(images)}")