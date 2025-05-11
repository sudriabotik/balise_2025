if __name__ == "__main__":
    from ultralytics import YOLO # type: ignore
    import os
    os.environ["CUDA_LAUNCH_BLOCKING"] = "1"


    # Load a model
    model = YOLO("yolov8n.pt") # pretrained model

    # Use the model
    results = model.train(
    data="entrainement_model/config.yaml",
    epochs=40,         # 100 epoch would be perfect but it takes too much time. 
    batch=8,          # impossible to have a larger batch size due to my gpu is too weak. 
    imgsz=640,        # resize image to 416x416 enable to have a faster training.  
    lr0=0.001,         
    optimizer="AdamW", 
    mosaic=1.0,        # Augmentation of the dataset
    mixup=0.1           #means that 20% of the training samples will use the mixup augmentation, while the rest will remain as standard images.
    )


