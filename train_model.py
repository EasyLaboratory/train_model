from ultralytics import YOLO
import torch
from pathlib import Path
print(torch.cuda.is_available())

base_path = Path(__file__).parent.resolve()

model_path = base_path/"runs"/"detect"/"train2"/"weights"/"best.pt"
model = YOLO(model_path)
model.train(data="car_data_v2.yaml",device=0,batch=32)