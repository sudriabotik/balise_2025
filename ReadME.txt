Balise_2025

Ce repository, est constituer de submodule, il y a 2 autre repository : 
- balise_rasberry_2025
- UYLE

entrainement_model fait partie du repository balise_2025.

Pour pull tous les repository d'un coup, la commande : 

git clone --recurse-submodules https://github.com/sudriabotik/balise_2025.git


modif yolo : 
C:\Users\PAUL\anaconda3\Lib\site-packages\ultralytics\data\dataset.py 
else:  # read image
    im = cv2.imread(f)  # BGR
    print(f"[DEBUG] Lecture de l'image : {f}")  # ← AJOUT ICI