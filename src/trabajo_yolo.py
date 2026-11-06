from ultralytics import YOLO

# 1. Carga del modelo (usamos 'm' para balance óptimo de precisión)
model = YOLO("yolov8m.pt")

# 2. Inferencia con mayor resolución
ruta_imagen = "ml-dog-cat-detection-yolo/data/imagen_de_animales.png"
resultados = model(ruta_imagen, imgsz=1280)


# 3. Acceso al resultado de la primera imagen
resultado = resultados[0]

# Contadores y acumuladores para el informe
dogs = 0
cats = 0
otros = 0
detalles_detecciones = []

# 4. Iteración sobre cada caja detectada
for box in resultado.boxes:
    clase_id = int(box.cls[0])
    nombre_clase = model.names[clase_id]
    confianza = float(box.conf[0])
    coords = [round(c, 1) for c in box.xyxy[0].tolist()]

    if nombre_clase == "dog":
        dogs += 1
    elif nombre_clase == "cat":
        cats += 1
    else:
        otros += 1

    detalles_detecciones.append((nombre_clase, confianza, coords))

# 5. Generación del informe en consola
print("\n" + "=" * 55)
print("       INFORME DE RECONOCIMIENTO Y RECUENTO YOLO       ")
print("=" * 55)
print(f"Ruta analizada: {ruta_imagen}")
print(f"Dimensiones procesadas: {resultado.orig_shape[0]}x{resultado.orig_shape[1]} px")
print(f"Tiempo de inferencia: {resultado.speed['inference']:.2f} ms")
print("-" * 55)
print(f"{'Clase':<10} | {'Certeza':<10} | {'Coordenadas (x1, y1, x2, y2)'}")
print("-" * 55)

for clase, conf, coords in detalles_detecciones:
    print(f"{clase:<10} | {conf*100:>6.1f}%    | {coords}")

print("-" * 55)
print(f"TOTAL DETECTADO: Perros: {dogs} | Gatos: {cats} | Otros: {otros}")
print("=" * 55 + "\n")

# 6. Mostrar el resultado visual con las cajas delimitadoras
resultado.show()