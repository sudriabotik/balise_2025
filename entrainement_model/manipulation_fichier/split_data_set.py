import os
import shutil
import random
from pathlib import Path

def split_yolo_dataset(image_dir, label_dir, output_dir, train_ratio=0.75, val_ratio=0.20, test_ratio=0.05):
    # Créer les dossiers nécessaires
    for split in ['train', 'val', 'test']:
        os.makedirs(os.path.join(output_dir, 'images', split), exist_ok=True)
        os.makedirs(os.path.join(output_dir, 'labels', split), exist_ok=True)

    # Liste des fichiers images
    image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    random.shuffle(image_files)

    total = len(image_files)
    n_train = int(total * train_ratio)
    n_val = int(total * val_ratio)
    n_test = total - n_train - n_val

    splits = {
        'train': image_files[:n_train],
        'val': image_files[n_train:n_train + n_val],
        'test': image_files[n_train + n_val:]
    }

    for split, files in splits.items():
        for img_file in files:
            base_name = Path(img_file).stem
            label_file = f"{base_name}.txt"

            src_img_path = os.path.join(image_dir, img_file)
            src_lbl_path = os.path.join(label_dir, label_file)

            dst_img_path = os.path.join(output_dir, 'images', split, img_file)
            dst_lbl_path = os.path.join(output_dir, 'labels', split, label_file)

            shutil.copy2(src_img_path, dst_img_path)

            if os.path.exists(src_lbl_path):
                shutil.copy2(src_lbl_path, dst_lbl_path)
            else:
                open(dst_lbl_path, 'w').close()  # fichier label vide si absent

        print(f"✅ {split.upper()} : {len(files)} images")

    print("\n🎉 Jeu de données divisé avec succès.")

# === Paramètres à modifier ===
image_dir = "gros_data_set/image"       # 🔁 ton dossier images
label_dir = "gros_data_set/label"       # 🔁 ton dossier labels
output_dir = "data_set_training"    # 🔁 dossier de sortie

split_yolo_dataset(image_dir, label_dir, output_dir)
