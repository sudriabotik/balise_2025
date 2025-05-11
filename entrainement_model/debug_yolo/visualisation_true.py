from ultralytics import YOLO
import os

# === Charger le modèle
model = YOLO("best_canette.pt")

# === Chemin vers ton image
img_path = "entrainement_model\data_set\Images\IMG_7238.jpg"  # ← à adapter

# === Lancer la prédiction avec visualisation complète des couches
results = model.predict(
    source=img_path,
    imgsz=640,
    visualize=True,       # ← active la sauvegarde des étapes internes
    save=True,            # ← enregistre l'image avec les prédictions
    save_txt=False,
    conf=0.25,
    verbose=True
)

# === Affichage du dossier où les images ont été sauvegardées
output_dir = results[0].save_dir
print(f"\n✅ Toutes les visualisations sont sauvegardées ici : {output_dir}")
