import os
import cv2

def visualize_annotations(image_name):
    # Chemins des dossiers
    images_folder = "RectAdjust/UYLE/Sample/Images"
    labels_folder = "RectAdjust/UYLE/Sample/Labels"

    # Chemin complet de l'image et du fichier d'annotations
    image_path = os.path.join(images_folder, image_name)
    label_path = os.path.join(labels_folder, image_name.replace(".jpg", ".txt"))  # Adapte si tes images sont .png

    # Vérifie que les fichiers existent
    if not os.path.exists(image_path):
        print(f"L'image '{image_name}' est introuvable.")
        return
    if not os.path.exists(label_path):
        print(f"Le fichier d'annotations '{label_path}' est introuvable.")
        return

    # Charge l'image
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    # Lit les annotations et dessine les rectangles
    with open(label_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            # Découpe les données au format YOLO
            class_id, x_center, y_center, box_width, box_height = map(float, line.split())
            
            # Convertit les coordonnées normalisées en pixels
            x_center *= width
            y_center *= height
            box_width *= width
            box_height *= height

            # Calcule les coins du rectangle
            x_min = int(x_center - box_width / 2)
            y_min = int(y_center - box_height / 2)
            x_max = int(x_center + box_width / 2)
            y_max = int(y_center + box_height / 2)

            # Dessine le rectangle sur l'image
            cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

            # Ajoute l'étiquette (facultatif)
            cv2.putText(
                image,
                f"Class {int(class_id)}",
                (x_min, y_min - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2,
            )


    max_display_size = 800  # Limite de taille pour l'affichage
    scale_factor = min(1.0, max_display_size / max(width, height))  # Ajuste à l’écran
    resized_image = cv2.resize(image, (int(width * scale_factor), int(height * scale_factor)))

    # Affiche l'image avec les rectangles
    cv2.imshow("Annotated Image", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Exemple d'utilisation
visualize_annotations("IMG_7238.jpg")  # Remplace "example.jpg" par le nom de ton image
