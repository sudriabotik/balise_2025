if __name__ == "__main__":
    from ultralytics import YOLO # type: ignore
    import os

    print("__________________________",os.path.exists("C:/Users/PAUL/OneDrive - ESME/Documents/Pusan_cour/ia programming/final_project/"))


    # Load a model
    model = YOLO("yolov8n.yaml")  

    # Use the model
    results = model.train(
    data="config.yaml",
    epochs=50,         # 100 epoch would be perfect but it takes too much time. 
    batch=4,          # impossible to have a larger batch size due to my gpu is too weak. 
    imgsz=416,        # resize image to 416x416 enable to have a faster training.  
    lr0=0.001,         
    optimizer="AdamW", 
    mosaic=1.0,        # Augmentation of the dataset
    mixup=0.2           #means that 20% of the training samples will use the mixup augmentation, while the rest will remain as standard images.
    )


