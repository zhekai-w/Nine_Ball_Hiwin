import cv2
import torch
import numpy as np
from models.experimental import attempt_load
from utils.general import check_img_size, non_max_suppression, scale_coords
from utils.plots import plot_one_box
from utils.datasets import letterbox

# 初始化模型
device = 'cuda' if torch.cuda.is_available() else 'cpu'
weights = 'first_best.pt'  # 指定權重文件的路徑
model = attempt_load(weights, map_location=device)  # 加載模型
stride = int(model.stride.max())  # 模型步幅
img_size = 640  # 輸入圖像尺寸
img_size = check_img_size(img_size, s=stride)  # 檢查圖像尺寸

# 設定相機
cap = cv2.VideoCapture(0)  # 更改0至您的相機ID或視頻文件路徑

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # 圖像預處理
    img = letterbox(frame, img_size, stride=stride)[0]
    img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR到RGB
    img = np.ascontiguousarray(img)
    img = torch.from_numpy(img).to(device).float() / 255.0
    if len(img.shape) == 3:
        img = img[None]  # 增加批次維度
    
    # 推論
    pred = model(img)[0]

    # 非最大抑制
    pred = non_max_suppression(pred)

    # 繪製檢測框
    for det in pred:  # 檢測到的物件列表
        if len(det):
            det[:, :4] = scale_coords(img.shape[2:], det[:, :4], frame.shape).round()
            for *xyxy, conf, cls in det:
                label = f'{model.names[int(cls)]} {conf:.2f}'
                plot_one_box(xyxy, frame, label=label, color=[255, 0, 0], line_thickness=3)
    
    # 顯示結果
    cv2.imshow('YOLOv7 Object Detection', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
