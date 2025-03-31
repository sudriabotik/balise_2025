import torch # type: ignore

#enable to see how much gpu are available to train the model. 

print("Nombre de GPUs disponibles :", torch.cuda.device_count())
for i in range(torch.cuda.device_count()):
    print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
