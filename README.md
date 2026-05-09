# Proyecto de Clasificación de Ataques de Ciberseguridad para el curso Aprendizaje de Máquinas

Asignatura: Aprendizaje de máquinas (ACIF104)
Informe Fase 2
Integrantes:
 - Daniel Prado Correa
 - Ximena Cortes Rodriguez
 - Guillermo Correa Martinez


## 1.	Objetivo del proyecto.
El objetivo del proyecto es clasificar automáticamente los tipos de ataques y sus categorías utilizando descripciones técnicas y vulnerabilidades.\

Requisitos Funcionales: Clasificación, identificación de categorías, análisis de vulnerabilidades, visualización, filtrado y predicción.


## 2.	Requisitos de instalación.
```bash
python -m venv venv

# Activar entorno 
#Linux / Mac
source venv/bin/activate

# Windows
venv\Scripts\activate

pip install -r requirements.txt
python app.py || python3 app.py
```


## 3.	Pasos para ejecutar frontend y backend.
pip install -r requirements.txt
python app.py || python3 app.py


## 4.	Ejemplo de uso.

<img width="1426" height="509" alt="image" src="https://github.com/user-attachments/assets/fb73c242-7786-48a3-907a-0d5af5581980" />




## Estructura del repositorio
data/: dataset o instrucciones para obtenerlo.\
notebooks/: análisis exploratorio, experimentos y pruebas.\
src/: scripts de limpieza, entrenamiento y predicción.\
app/: frontend y backend del prototipo.\
models/: pipelines serializados.
