import cv2
import os

# 创建保存图片的文件夹
if not os.path.exists("frames"):
    os.makedirs("frames")

# 打开视频文件
cap = cv2.VideoCapture(r"C:\Users\zty\Downloads\VID_20250513_163702.mp4")
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # 每两帧提取一次
    if frame_count % 30 == 0:
        # 保存当前帧为图片
        cv2.imwrite(f"frames/frame_{frame_count:04d}.png", frame)

    frame_count += 1

cap.release()
cv2.destroyAllWindows()