import os

def clean_unused_labels(image_dir, label_dir, image_extensions=(".jpg", ".jpeg", ".png")):
    # Récupère tous les noms d'images (sans extension)
    image_basenames = {os.path.splitext(f)[0] for f in os.listdir(image_dir) if f.lower().endswith(image_extensions)}

    # Récupère tous les fichiers .txt dans le dossier label
    label_files = [f for f in os.listdir(label_dir) if f.endswith(".txt")]

    removed = 0
    for label_file in label_files:
        label_name = os.path.splitext(label_file)[0]

        if label_name not in image_basenames:
            label_path = os.path.join(label_dir, label_file)
            os.remove(label_path)
            removed += 1
            print(f"🗑️ Supprimé : {label_file}")

    print(f"\n✅ Fichiers supprimés : {removed}")
    print("Nettoyage terminé.")

# === Exemple d’utilisation ===
if __name__ == "__main__":
    image_dir = "data_set_training_debug/images/train"   # ⬅️ Remplace ici
    label_dir = "data_set_training_debug/labels/train"   # ⬅️ Et ici

    clean_unused_labels(image_dir, label_dir)
