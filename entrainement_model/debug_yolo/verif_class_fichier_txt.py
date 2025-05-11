import os

label_dirs = [
    "data_set_training/labels/train",
    "data_set_training/labels/val",
    "data_set_training/labels/test"
]
max_class = 1  # donc classes valides : 0 et 1

def scan_labels(label_dir):
    bad_files = []
    for f in os.listdir(label_dir):
        if not f.endswith(".txt"):
            continue
        with open(os.path.join(label_dir, f), 'r') as file:
            lines = file.readlines()
        for line in lines:
            parts = line.strip().split()
            if not parts: continue
            try:
                class_id = int(parts[0])
                if class_id > max_class:
                    bad_files.append((f, class_id))
                    break
            except:
                bad_files.append((f, "Invalid format"))
                break
    return bad_files

for label_dir in label_dirs:
    print(f"📂 Scanning {label_dir}")
    issues = scan_labels(label_dir)
    if issues:
        print(f"❌ Fichiers avec classes hors limite : {len(issues)}")
        for f, err in issues:
            print(f"   - {f} (classe : {err})")
    else:
        print("✅ Aucun problème détecté.\n")
