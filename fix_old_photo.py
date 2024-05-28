from PIL import Image, ImageFilter

# Open the image file
name = input("Ingresa el nombre de.la imagen o copia y pega:  ")
img = Image.open(name)

# Apply the sharpen filter
optimis = img.filter(ImageFilter.SHARPEN)

# Save the restored image
name_img = input("Nuevo nombre de la imagen: ")
optimis.save(f"{name_img}.jpg")