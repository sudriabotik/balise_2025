import os
import random
import cv2
import numpy as np
import torchvision.transforms as T
from PIL import Image
from tqdm import tqdm
import math

def augment_image(pil_img, augmentation_type):
    if augmentation_type == "flip_and_noise":
        transform = T.Compose([
            T.RandomHorizontalFlip(p=1.0),  # Force horizontal flip
            T.RandomVerticalFlip(p=1.0),    # Force vertical flip
            T.Lambda(lambda x: add_noise(x)),
        ])
    elif augmentation_type == "contrast_brightness":
        transform = T.Compose([
            T.ColorJitter(brightness=0.4, contrast=0.4, saturation=0.3, hue=0.02),
        ])
    else:
        transform = T.Compose([])  # No augmentation

    return transform(pil_img)

def add_noise(pil_img):
    img = np.array(pil_img).astype(np.float32) / 255.0
    noise = np.random.normal(0, 0.02, img.shape)
    img += noise
    img = np.clip(img, 0, 1)
    return Image.fromarray((img * 255).astype(np.uint8))

def augment_dataset(input_dir, output_dir, augmentations_per_image=5):
    os.makedirs(output_dir, exist_ok=True)
    img_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    for filename in tqdm(img_files, desc="Augmenting images"):
        path = os.path.join(input_dir, filename)
        base_img = Image.open(path).convert("RGB")

        # Generate specific augmentations
        augmentations = ["flip_and_noise", "contrast_brightness"]
        for i, augmentation_type in enumerate(augmentations):
            aug_img = augment_image(base_img, augmentation_type)
            output_filename = f"{os.path.splitext(filename)[0]}_aug{i}.jpg"
            aug_img.save(os.path.join(output_dir, output_filename))

def verify_directory_path(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Le chemin spécifié n'existe pas : {path}")
    if not os.path.isdir(path):
        raise NotADirectoryError(f"Le chemin spécifié n'est pas un répertoire : {path}")
    print(f"Le chemin est valide et pointe vers un répertoire : {path}")

def transform_bounding_boxes(bboxes, img_width, img_height, flip_horizontal, flip_vertical):
    transformed_bboxes = []
    for bbox in bboxes:
        class_id, x_center, y_center, width, height = bbox

        if flip_horizontal:
            x_center = 1.0 - x_center

        if flip_vertical:
            y_center = 1.0 - y_center

        transformed_bboxes.append((class_id, x_center, y_center, width, height))

    return transformed_bboxes

def read_bounding_boxes(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    bboxes = []
    for line in lines:
        parts = line.strip().split()
        class_id = int(parts[0])
        coords = tuple(map(float, parts[1:]))
        bboxes.append((class_id, *coords))  # ✅ on garde la classe ici
    return bboxes


def write_bounding_boxes(file_path, bboxes):
    with open(file_path, 'w') as f:
        for bbox in bboxes:
            class_id, x, y, w, h = bbox
            f.write(f"{class_id} {x} {y} {w} {h}\n")

if __name__ == "__main__":
    import argparse
    import sys

    print("Arguments reçus :", sys.argv)  # Ajout pour débogage
    verify_directory_path("gros_data_set/augmente_data_set/original_image")
    print("__________\n")
    
    # Définir les chemins directement dans le script
    input_dir = "gros_data_set/augmente_data_set/original_image"
    output_dir = "gros_data_set/augmente_data_set/augmented_image"
    augmentations_per_image = 3  # Nombre d'augmentations par image

    # Nouvelle variable pour les fichiers d'annotations
    input_labels_dir = "gros_data_set/augmente_data_set/original_label"
    output_labels_dir = "gros_data_set/augmente_data_set/augmented_label"

    os.makedirs(output_labels_dir, exist_ok=True)

    # Appeler la fonction avec les variables définies
    augment_dataset(input_dir, output_dir, augmentations_per_image)

    # Récupérer la liste des fichiers d'images après augmentation
    img_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    for filename in tqdm(img_files, desc="Processing bounding boxes"):
        path = os.path.join(input_dir, filename)
        base_img = Image.open(path).convert("RGB")

        # Lire les annotations associées
        label_file = os.path.join(input_labels_dir, f"{os.path.splitext(filename)[0]}.txt")
        if os.path.exists(label_file):
            bboxes = read_bounding_boxes(label_file)
        else:
            bboxes = []

        # Generate specific augmentations
        augmentations = ["flip_and_noise", "contrast_brightness"]
        for i, augmentation_type in enumerate(augmentations):
            aug_img = augment_image(base_img, augmentation_type)
            output_filename = f"{os.path.splitext(filename)[0]}_aug{i}.jpg"
            aug_img.save(os.path.join(output_dir, output_filename))

            # Transformer les bounding boxes
            img_width, img_height = base_img.size
            flip_horizontal = augmentation_type == "flip_and_noise"
            flip_vertical = augmentation_type == "flip_and_noise"
            transformed_bboxes = transform_bounding_boxes(bboxes, img_width, img_height, flip_horizontal, flip_vertical)

            # Sauvegarder les annotations modifiées
            output_label_file = os.path.join(output_labels_dir, f"{os.path.splitext(filename)[0]}_aug{i}.txt")
            write_bounding_boxes(output_label_file, transformed_bboxes)
