# Proyecto de Clasificación de Ataques de Ciberseguridad para el curso Aprendizaje de Máquinas

Asignatura: Aprendizaje de máquinas (ACIF104)
Informe Fase 3
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

```bash
pip install -r requirements.txt
python app.py || python3 app.py
```

Una vez ejecutado los comandos anteriores, en navegador de preferencia tipear la siguiente url:
http://127.0.0.1:5000

Esto abrirá la aplicación para interactuar con el usuario.


## 4.	Ejemplo de uso.

Paso 1: Ingresar a la URL: http://127.0.0.1:5000

Abrirá la siguiente página:
<img width="1426" height="509" alt="image" src="https://github.com/user-attachments/assets/fb73c242-7786-48a3-907a-0d5af5581980" />

Paso 2: Escribir descriptor del incidente

Paso 3: Presionar botón "Analizar ataque"

Resultado: la aplicación mostrará la clasificación correspondiente al tipo de ataque descrito.

<img width="2852" height="1018" alt="image" src="https://github.com/user-attachments/assets/f5b34fe1-9802-4173-a6f8-2b434631a4b4" />



## Estructura del repositorio
data/: dataset o instrucciones para obtenerlo.\
notebooks/: análisis exploratorio, experimentos y pruebas.\
src/: scripts de limpieza, entrenamiento y predicción.\
app/: frontend y backend del prototipo.\
models/: pipelines serializados.
