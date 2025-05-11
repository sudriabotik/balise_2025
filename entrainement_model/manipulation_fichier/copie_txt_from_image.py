import os
import shutil

def copy_matching_labels(image_subset_dir, label_full_dir, label_output_dir, image_extensions=(".jpg", ".jpeg", ".png")):
    os.makedirs(label_output_dir, exist_ok=True)

    image_files = [f for f in os.listdir(image_subset_dir) if f.lower().endswith(image_extensions)]
    image_basenames = {os.path.splitext(f)[0] for f in image_files}

    copied = 0
    for basename in image_basenames:
        label_filename = f"{basename}.txt"
        src_label_path = os.path.join(label_full_dir, label_filename)
        dst_label_path = os.path.join(label_output_dir, label_filename)

        if os.path.exists(src_label_path):
            shutil.copy2(src_label_path, dst_label_path)
            print(f"📄 Copié : {label_filename}")
            copied += 1
        else:
            print(f"⚠️ Label manquant pour : {basename}")

    print(f"\n✅ Fichiers .txt copiés : {copied}")
    print("Copie terminée.")

# === Exemple d'utilisation ===
if __name__ == "__main__":
    image_subset_dir = "gros_data_set/augmente_data_set/original_image"      # 🔁 images sélectionnées
    label_full_dir = "gros_data_set/label" # 🔁 annotations complètes
    label_output_dir = "gros_data_set/augmente_data_set/original_label"      # 🔁 nouvelle destination des labels

    copy_matching_labels(image_subset_dir, label_full_dir, label_output_dir)
