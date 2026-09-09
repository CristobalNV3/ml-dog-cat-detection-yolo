# ML Dog & Cat Detection with YOLO

Trabajo de Machine Learning para detectar y contar perros y gatos en una imagen utilizando Python y YOLO.

## Integrantes

- Cristóbal Navarrete
- Miguel Morales

## Objetivo

Reconocer perros y gatos presentes en una imagen y contar cuántos hay de cada uno.

## Tecnologías

- Python
- Ultralytics YOLO
- YOLOv8m

## Instalación

Instalar las dependencias:

```powershell
pip install -r requirements.txt
```

## Ejecución

```powershell
python src/trabajo_yolo.py
```

## Resultado

En la imagen utilizada se detectaron:

- 4 perros
- 4 gatos

Se utilizó un nivel mínimo de confianza de 0.50 para evitar detecciones de baja confianza.