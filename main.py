import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Création de la fenêtre principale
root = tk.Tk()

# Demande à l'utilisateur de sélectionner une image
filename = filedialog.askopenfilename()

# Chargement de l'image
image = Image.open(filename)

# Création d'un widget Canvas pour afficher l'image
canvas = tk.Canvas(root, width=image.width, height=image.height)
canvas.pack()

# Affichage de l'image dans le Canvas
image_tk = ImageTk.PhotoImage(image)
canvas.create_image(0, 0, anchor='nw', image=image_tk)

def selection_changed(event):
    # Récupération des coordonnées de début et de fin de la sélection
    x1, y1 = event.x, event.y
    x2, y2 = event.x_root, event.y_root

    # Calcul de la largeur et de la hauteur de la sélection
    width = abs(x1 - x2)
    height = abs(y1 - y2)

    # Calcul de la position de la sélection (coin supérieur gauche)
    left = min(x1, x2)
    top = min(y1, y2)

    # Affichage des résultats
    print(f"Width: {width} pixels")
    print(f"Height: {height} pixels")
    print(f"Top: {top} pixels")
    print(f"Left: {left} pixels")

# Ajout de la fonction de callback au widget Canvas
canvas.bind("<B1-Motion>", selection_changed)

root.mainloop()
