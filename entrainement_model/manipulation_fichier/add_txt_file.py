import os

def create_missing_labels(image_dir, label_dir, image_extensions=(".jpg", ".jpeg", ".png")):
    os.makedirs(label_dir, exist_ok=True)

    # Liste des noms d'images sans extension
    image_basenames = {os.path.splitext(f)[0] for f in os.listdir(image_dir) if f.lower().endswith(image_extensions)}

    # Liste des noms de fichiers txt sans extension
    label_basenames = {os.path.splitext(f)[0] for f in os.listdir(label_dir) if f.endswith(".txt")}

    created = 0
    for img_name in image_basenames:
        if img_name not in label_basenames:
            txt_path = os.path.join(label_dir, f"{img_name}.txt")
            with open(txt_path, "w") as f:
                pass  # fichier vide
            print(f"📝 Créé : {img_name}.txt")
            created += 1

    print(f"\n✅ Fichiers .txt créés : {created}")
    print("Complétion des labels terminée.")

# === Exemple d’utilisation ===
if __name__ == "__main__":
    image_dir = "gros_data_set/image"   # ⬅️ Remplace ici
    label_dir = "gros_data_set/label"   # ⬅️ Et ici

    create_missing_labels(image_dir, label_dir)
