## Índice
<summary>Tabla de contenido</summary>
  <ol>  
    <li><a href="#Introducción">Introducción</a></li>
    <li><a href="#Objetivos">Objetivos</a></li>
    <li><a href="#etapas-de-proyecto">Etapas de Proyecto</a></li>
    <li><a href="#ETL">ETL</a></li>
    <li><a href="#EDA">EDA</a></li>
    <li><a href="#funciones-api">Funciones API</a></li>
    <li><a href="#modelo-ML">Modelo ML</a></li>
    <li><a href="#Deployment">Deployment</a></li>
    <li><a href="#Video">Video</a></li>
  </ol>
</details>
</br>

## Introducción

¡Bienvenidos a Steam! Como Data Scientist, nuestro desafío es crear un sistema de recomendación de videojuegos para nuestros usuarios. Sin embargo, los datos se presentan en estado crudo y anidado, sin procesos automatizados y parte de nuestro trabajo será el alistamiento de los mismos con el fin de disponibilizarlos para las consultas y para la creación del modelo de recomendación.
</br>

## Objetivos

El objetivo central de este proyecto es desarrollar y desplegar un sistema de recomendación de videojuegos, aprovechando un conjunto de datos completo. El proyecto se enfoca en lograr los siguientes objetivos específicos:

- **Transformación y Limpieza de Datos:** Aplicar técnicas de Extracción, Transformación y Carga (ETL) para preprocesar y limpiar el conjunto de datos de juegos.

- **Análisis Exploratorio de Datos (EDA):** Realizar un análisis de los datos para obtener ideas sobre los atributos de los videojuegos, como características, género y plataforma. Identificar patrones clave que influyan significativamente en los precios y descubrir relaciones que puedan aprovecharse para una predicción precisa.

- **Desarrollo de API:** Diseñar e implementar un conjunto de funciones y una API que se integre perfectamente con el sistema de predicción de precios de juegos para realizar determinadas consultas.

- **Modelo ML:** Desarrollar un modelo de aprendizaje automático que utilice técnicas de regresión para predecir y recomendar algunos juegos a partir de los atributos de otros.

- **Despliegue de la API:** Implementar la API del sistema de predicción de videojuegos en un entorno de producción, garantizando su disponibilidad y accesibilidad para los usuarios.
</br>

## Etapas de Proyecto

El proyecto se desarrolló siguiendo estos aspectos clave:
- ETL (Extract, Transform, Load): Proceso de extracción, transformación y Carga: [ETL link](https://github.com/idaroga/PI-MLOps-STEAM-IVAN/blob/main/pi01-ivan-etl.ipynb)
- EDA (Exploratory Data Analisys): Analisis exploratorio de datos: [EDA link](https://github.com/idaroga/PI-MLOps-STEAM-IVAN/blob/main/pi01-ivan-eda.ipynb)
- Funciones de consulta (endpoints) para la API: [Funciones link](https://github.com/idaroga/PI-MLOps-STEAM-IVAN/blob/main/pi01-ivan-funciones.ipynb)
- Modelos de aprendizaje automático: [Modelamiento link](https://github.com/idaroga/PI-MLOps-STEAM-IVAN/blob/main/pi01-ivan-modelado.ipynb)
- Implementación de API: [Deployed API link](https://pi-mlops-steam-ivan.onrender.com/docs)
</br>

## ETL (Extract, Transform, Load)

Durante la fase de transformación y limpieza de datos (ETL), se han aplicado una serie de pasos esenciales para garantizar la calidad y coherencia de los datos. Estas acciones buscan preparar el conjunto de datos de manera óptima para su análisis posterior y para ser consumido por la API que se está desarrollando.
</br>

### **1- Reconocimiento del origen de los datos:** 
  - Se encuentran 3 datasets en archivos diferentes cada uno en formato json pero se encuentran comprimidos así que se procede a descomprimirlos primero con "winrar" antes de importarlos.
  - Una vez descomprimirdos se revisa el formato de codificación de cada archivo y se evidencia lo siguiente:
    - australian_user_reviews.json = encoding MacRoman
    - australian_user_items.json = encoding MacRoman
    - output_steam_games.json = encoding ASCII
  - Después de leer cada archivo JSON en un dataframe y dado que toma bastante tiempo realizar este proceso se guarda cada dataframe en formato CSV como respaldo para poder cargarlo de manera más rápida en caso de ser necesario.
  <br>

  #### **1-1- Lectura de datos**

  #### **1-2- Estructura general de los datasets**

    **1-2-** csv_games.csv = output_steam_games.json:
      - Se revisa dimensiones, cantidad de columnas, estructura general y se encuentran 88310 filas (registros) completamente nulos así que se eliminan para reducir el tamaño del arhivo, mejorar el procesamiento y limpiar un poco más los datos.
      - El dataset queda listo para exportar a CSV para realizar el "Analisis Exploratorio de Datos" (EDA)
      <br>

    **1-2-** csv_reviews.csv = australian_user_reviews.json
      - Se revisa dimensiones, cantidad de columnas, estructura general y no se encuentran filas completamente nulas.
      - Dado que el dataset contiene una columna llamada "reviews" que contiene datos en formato lista compuestas a su vez de diccionarios de procede a desanidar y para dejar un dataset completo 
      - El dataset queda listo para exportar a CSV para realizar el "Analisis Exploratorio de Datos" (EDA)

    **1-2-** csv_items.csv = australian_user_items.json
      - Se revisa dimensiones, cantidad de columnas, estructura general y no se encuentran filas completamente nulas.
      - Dado que la columna "items" contiene una lista de diccionarios se procede a desanidar y dejar un dataset completo desanidado
      - El dataset queda listo para exportar a CSV para realizar el "Analisis Exploratorio de Datos" (EDA)
</br>

## **2- Exportar a CSV**
  Se exporta cada dataset a un archivo CSV independiente de la siguiente forma:
  - Archivo "output_steam_games.json" = etl_games.csv
  - Archivo "australian_user_reviews.json" = etl_reviews.csv
  - Archivo "australian_users_items.json" = etl_items.csv
</br>

*Todas estas etapas se llevaron a cabo de manera local en **Visual Studio Code (VSCODE)**, empleando **Jupyter Notebook** como nuestro entorno principal. Para la implementación de cada paso, contamos con la potencia de **Python** como lenguaje de programación, respaldado por las versátiles bibliotecas **numpy y pandas**, que fueron fundamentales para la manipulación y transformación eficiente de los datos. Estas herramientas esenciales se combinaron hábilmente para crear un flujo de trabajo fluido y eficaz, permitiendo que el proyecto tomara forma de manera coherente y organizada.*
</br>

## EDA (Exploratory Data Analysis)

Utilizando los datos resultantes del proceso ETL, se llevó a cabo un análisis exploratorio de datos (EDA).

A medida que se avanzaba en la exploración de datos se tomaron decisiones críticas que influyeron en la dirección del proyecto. La identificación de patrones y atributos relevantes se convirtió en un pilar esencial para construir la base de las funciones API y el sistema de recomendación que se desarrollaría posteriormente. La calidad del análisis realizado durante el EDA estableció el terreno para la creación de soluciones sólidas y eficientes que aprovecharían al máximo la información extraída de los datos procesados en la etapa de ETL.
</br>

### **1- COMPRENSIÓN DEL NEGOCIO**

  Steam es una plataforma digital de distribución de videojuegos desarrollada por la empresa Valve Corporation. Fue lanzada en 2003 y se ha convertido en una de las plataformas más populares para comprar, descargar y jugar videojuegos en computadoras personales.

  Steam ofrece una amplia variedad de funciones y servicios relacionados con los videojuegos:

  1. **Distribución Digital:** Steam permite a los usuarios comprar y descargar videojuegos directamente a sus computadoras. Los juegos se vinculan a las cuentas de los usuarios y se pueden descargar y jugar en cualquier momento.

  2. **Actualizaciones Automáticas:** Steam proporciona actualizaciones automáticas para los juegos comprados. Esto asegura que los juegos estén siempre actualizados con los últimos parches y mejoras.

  3. **Comunidad:** Steam cuenta con una comunidad en línea donde los jugadores pueden interactuar, unirse a grupos, chatear con amigos, compartir capturas de pantalla y logros, y más.

  4. **Tienda:** La tienda de Steam ofrece una amplia selección de juegos de diferentes géneros y desarrolladores. Los jugadores pueden buscar juegos, leer reseñas, ver trailers y comprar títulos directamente desde la plataforma.

  5. **Biblioteca de Juegos:** Los juegos adquiridos se almacenan en la biblioteca de juegos del usuario, lo que facilita la descarga y el acceso.

  6. **Steam Workshop:** Muchos juegos en Steam tienen soporte para el Steam Workshop, una plataforma que permite a los jugadores crear, compartir y descargar contenido adicional, como mods, mapas y elementos creados por la comunidad.

  7. **Steam Cloud:** Steam ofrece almacenamiento en la nube para guardar partidas y configuraciones de juego, lo que permite a los jugadores acceder a su progreso desde diferentes dispositivos.

  8. **Ofertas y Promociones:** Steam es conocido por sus ofertas regulares, ventas y promociones que permiten a los jugadores comprar juegos a precios reducidos.

  En resumen, Steam es una plataforma integral que facilita la adquisición, descarga y gestión de videojuegos en PC. Ha tenido un impacto significativo en la industria de los videojuegos y ha influido en cómo se distribuyen y consumen los juegos en la era digital.

  #### **1-1- Obtener datos provenientes de ETL**

  #### **1-2- Examinar estructura general**

    **1-2- df_games**
      - Corresponde a un dataset que indica los juegos disponibles en la plataforma de steam y sus respectivas características
      - A primera vista se van a descartar la siguientes columnas que se consideran innecesarias para las demandas del proyecto como son:
        - publisher
        - title
        - url
        - reviews_url
        - early_access
      
    **1-2- df_reviews**
      - Corresponde a un dataset que indica las reseñas que los jugadores hacen de los videojuegos y las características relacionadas con estas reseñas
      - A primera vista se van a descartar la siguientes columnas que se consideran innecesarias para las demandas del proyecto como son:
        - user_url
        - funny
        - helpful

    **1-2- df_items**
      - Corresponde a un dataset que indica las características de cada usuario con respecto a los videojuegos que posee
      - A primera vista se van a descartar la siguientes columnas que se consideran innecesarias para las demandas del proyecto como son:
        - steam_id
        - item_name
        - playtime_2weeks

  - Dadas las dimensiones y el peso de los datasets games, items y reviews se planea generar nuevos datasets que contenga cada uno la información específica para ejecutar las consultas que demanda el proyecto. De esta manera se trabajarán datasets de dimensiones más pequeñas con menor tamaño de almacenamiento para agilizar las consultas.
  - Por esta razón se seleccionarán únicamente las columnas necesarias de los datasets games, items y reviews con el fin de realizar las respectivas combianciones para obtener como resultado los datasets deseados
</br>

### **2- Limpieza de datos**
  - Se realizarán las transformaciones de cada una de las columnas de los datasets games, reviews e items de acuerdo al tipo de variable que corresponde
</br>

### **3- Creación de nuevos datasets**
  - df_userdata
  - df_countreviews
  - df_genre
  - df_userforgenre
  - df_developer
  - df_sentiment_analysis
  - df_modeloML
</br>

### **4- Exportar a CSV**
  - Se exporta a CSV cada dataset
</br>

*Todo este proceso fue desarrollado localmente en **Visual Studio Code (VSCODE)** utilizando **Jupyter Notebook** como nuestro entorno de trabajo principal. La combinación de herramientas tecnológicas que empleamos incluye **Python** como lenguaje de programación, junto con bibliotecas esenciales como **numpy y pandas** para la manipulación eficiente de datos. Además, utilizamos **matplotlib y seaborn** para la creación de visualizaciones gráficas impactantes, que nos permitieron revelar patrones y tendencias ocultas en los datos de manera efectiva.*
</br>

## Funciones API

En esta fase del proyecto, se llevaron a cabo el desarrollo de los puntos finales solicitados mediante funciones en Python, dentro de un archivo de Jupyter Notebook. Tras la instalación de FastAPI y uvicorn, se creó un archivo [main.py](https://github.com/idaroga/PI-MLOps-STEAM-IVAN/blob/main/main.py) con la estructura necesaria para desplegar los puntos finales.

Realicé pruebas de esta implementación a nivel local, utilizando el servicio uvicorn en el puerto 8000

Estas funciones se alimentan con datos del archivo CSV resultante del análisis exploratorio de datos (EDA) realizado anteriormente. 

*Todo este proceso de desarrollo se llevó a cabo de manera local en **Visual Studio Code (VSCODE)**, haciendo uso de **Jupyter Notebook**, **Python, numpy, pandas, FastAPI y uvicorn**. Esta amalgama de herramientas tecnológicas permitió dar vida a los puntos finales de la API, desplegando de manera exitosa el acceso a las funciones y capacidades desarrolladas en el proyecto.*
</br>


## Modelo ML
</br>


## Deployment

Luego de completar la implementación de **main.py** y demás archivos que componen el modelo y las funciones, el despliegue de la API se realizó de manera exitosa a través de Render, siguiendo un proceso meticuloso y organizado:

**1. Creación de Entorno Virtual:** El proceso de despliegue comenzó con la creación de un entorno virtual aislado, lo cual permitió gestionar y separar las dependencias específicas de la API, evitando conflictos y asegurando la coherencia en el entorno de producción.

**2. Configuración de Archivos Necesarios:** Se llevaron a cabo las configuraciones necesarias para el despliegue, asegurando que todos los archivos esenciales estuvieran presentes y correctamente configurados. Esto garantizó una base sólida para el funcionamiento de la API en el entorno de Render.

**3. Inicialización de Git y Realización de Instalaciones:** Se inició un repositorio de Git para el proyecto y se realizaron las instalaciones pertinentes de las bibliotecas y paquetes necesarios para el funcionamiento de la API. Esto aseguró que la infraestructura estuviera lista para el proceso de despliegue.

**4. Generación de Lista de Dependencias (Pip Freeze):** Se generó una lista de las dependencias y versiones específicas utilizadas en el entorno virtual. Esta lista proporcionó un registro claro y conciso de las bibliotecas que respaldaban la API, simplificando la gestión y el mantenimiento. [requierements.txt](https://github.com/idaroga/PI-MLOps-STEAM-IVAN/blob/main/requirements.txt)

**5. Experiencia Render:** A través de Render, se llevaron a cabo los pasos necesarios para desplegar la API. Render proporcionó una plataforma eficiente y confiable para implementar aplicaciones, asegurando una experiencia de usuario optimizada y accesible. Render implementa la aplicación y genera un enlace para acceder a la [API en ejecución](https://pi-mlops-steam-ivan.onrender.com). **(Puedes agregar "/docs" al final del enlace para acceder a la documentación automática creada por FastAPI. Esto te brindará una interfaz interactiva y detallada que describe todos los endpoints, métodos y parámetros disponibles en la API de manera clara y concisa.)**

*Con la culminación exitosa de estos pasos, la API que se había construido y desarrollado con dedicación y precisión ahora está completamente preparada y lista para ser consumida. La combinación de todas estas etapas ha permitido llevar el proyecto desde su fase inicial hasta un estado funcional y accesible, donde los usuarios pueden aprovechar plenamente las funciones y capacidades de la API de manera confiable y eficiente.*
</br>

## Video

Link al video donde proporciono una visión general de este proyecto:
  
[Google Drive](https://drive.google.com/drive/folders/1JcFrubYnCqzWCYygGrwtBN0N8MlOM7ts?usp=drive_link)
  
</div>

