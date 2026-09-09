from pathlib import Path
from ultralytics import YOLO

# 1. Carga del modelo YOLOv8m preentrenado
model = YOLO("yolov8m.pt")

# 2. Definición de la ruta de la imagen e inferencia
raiz_proyecto = Path(__file__).resolve().parents[1]
ruta_imagen = raiz_proyecto / "data" / "imagen_de_animales.png"
ruta_outputs = raiz_proyecto / "outputs"
ruta_outputs.mkdir(parents=True, exist_ok=True)

if not ruta_imagen.exists():
    raise FileNotFoundError(f"No se encontró la imagen: {ruta_imagen}")

resultados = model(str(ruta_imagen), imgsz=1280, conf=0.50)

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

# 5. Generación del informe
lineas_informe = [
    "=" * 55,
    "       INFORME DE RECONOCIMIENTO Y RECUENTO YOLO       ",
    "=" * 55,
    f"Ruta analizada: {ruta_imagen}",
    f"Dimensiones procesadas: {resultado.orig_shape[0]}x{resultado.orig_shape[1]} px",
    f"Tiempo de inferencia: {resultado.speed['inference']:.2f} ms",
    "-" * 55,
    f"{'Clase':<10} | {'Certeza':<10} | {'Coordenadas (x1, y1, x2, y2)'}",
    "-" * 55,
]

for clase, conf, coords in detalles_detecciones:
    lineas_informe.append(
        f"{clase:<10} | {conf*100:>6.1f}%    | {coords}"
    )

lineas_informe.extend([
    "-" * 55,
    f"TOTAL DETECTADO: Perros: {dogs} | Gatos: {cats} | Otros: {otros}",
    "=" * 55,
])

informe = "\n".join(lineas_informe)

# Mostrar informe en consola
print("\n" + informe + "\n")

# Guardar informe como archivo de texto
ruta_informe = ruta_outputs / "resultados.txt"
ruta_informe.write_text(informe, encoding="utf-8")

# Guardar imagen procesada con bounding boxes
ruta_resultado = ruta_outputs / "animales_detectados.png"
resultado.save(filename=str(ruta_resultado))

print(f"Informe guardado en: {ruta_informe}")
print(f"Imagen procesada guardada en: {ruta_resultado}")


# 6. Mostrar el resultado visual con las cajas delimitadoras
resultado.show()