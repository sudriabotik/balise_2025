import os

image_dir = "data_set_training/images/test"
label_dir = "data_set_training/labels/test"

image_exts = ['.jpg', '.jpeg', '.png']
missing_labels = []

for img_file in os.listdir(image_dir):
    if not any(img_file.endswith(ext) for ext in image_exts):
        continue
    label_file = os.path.splitext(img_file)[0] + '.txt'
    if not os.path.exists(os.path.join(label_dir, label_file)):
        missing_labels.append(img_file)

print("=== Vérification des images sans .txt ===")
print(f"Total images scannées : {len(os.listdir(image_dir))}")
print(f"❌ Images sans fichier label : {len(missing_labels)}")
for f in missing_labels:
    print("   -", f)
