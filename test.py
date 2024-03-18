from ultralytics import YOLO

if __name__ == '__main__':
    # Load a model
    model = YOLO(r'runs/train/exp2/weights/best.pt')  # build a new model from YAML
    model.info()

