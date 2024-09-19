from ultralytics import YOLO
from pathlib import Path
import time

base_path = Path(__file__).parent.resolve()

def valuate_model():
    model_path = base_path/"runs"/"detect"/"train2"/"weights"/"best.pt"
    model = YOLO(model_path)
    metrix = model.val(data="./car_data_v2.yaml")
    print(metrix)

def predict_model():
    model_path = base_path/"runs"/"detect"/"train3"/"weights"/"best.pt"
    data_path = base_path/"splited_dataset"/"images"/"test"
    print(data_path)
    model = YOLO(model_path)
    results = model.predict(source=data_path)
    for result in results:
        result.show()
        time.sleep(1)

    

if __name__ == "__main__":
    predict_model()
