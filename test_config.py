import cv2
import numpy as np
print("--- Configuration Réussie ---")
print(f"OpenCV version: {cv2.__version__}")
print(f"NumPy version: {np.__version__}")
# Test de création d'une image simple (Matrice de zéros)
# Une image noire de 400x400 pixels
img = np.zeros((400, 400, 3), dtype=np.uint8)
cv2.putText(img, 'Config OK !', (100, 200),
cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.imshow('Vérification Computer Vision 1', img)
cv2.waitKey(0)
cv2.destroyAllWindows()