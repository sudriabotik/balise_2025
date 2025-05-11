import os

# === À adapter ===
base_dir = "data_set_training/labels"  # racine des labels (contenant /train, /val, etc.)
valid_classes = [0, 1]

def is_valid_line(line):
    parts = line.strip().split()
    if len(parts) != 5:
        return False
    try:
        class_id = int(parts[0])
        if class_id not in valid_classes:
            return False
        coords = list(map(float, parts[1:]))
        return all(0.0 <= v <= 1.0 for v in coords)
    except:
        return False

def scan_all_txt(base_dir):
    invalid_files = []
    empty_files = []
    total = 0

    for root, _, files in os.walk(base_dir):
        for file in files:
            if not file.endswith(".txt"):
                continue
            total += 1
            path = os.path.join(root, file)
            with open(path, "r") as f:
                lines = f.readlines()
            if not lines:
                empty_files.append(path)
                continue
            if not all(is_valid_line(line) for line in lines):
                invalid_files.append(path)

    print("=== Résultat global ===")
    print(f"📁 Total fichiers .txt scannés : {total}")
    print(f"❌ Fichiers vides : {len(empty_files)}")
    for f in empty_files:
        print("   -", f)
    print(f"⚠️ Fichiers avec lignes incorrectes : {len(invalid_files)}")
    for f in invalid_files:
        print("   -", f)
    print("✅ Terminé.")

    return empty_files + invalid_files

if __name__ == "__main__":
    fautifs = scan_all_txt(base_dir)
    # === Optionnel : suppression automatique
    # for path in fautifs:
    #     os.remove(path)
    #     print(f"🗑️ Supprimé : {path}")
