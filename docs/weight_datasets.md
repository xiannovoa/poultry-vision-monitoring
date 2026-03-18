# Análisis de datasets

Este documento recoge el proceso de inspección y selección de datasets abiertos utilizados en el proyecto **Sistema de visión por computador para monitorización avícola inteligente**.

El objetivo es identificar datasets que permitan abordar dos tareas principales:

1. Detección / segmentación de pollos
2. Estimación del peso del animal a partir de imágenes

---

# Dataset 1 – Broiler weights of Cobb Avian (Mendeley)

**Fuente del dataset**

https://data.mendeley.com/datasets/zrs8kk9dvr/1

---

## Descripción general

Este dataset contiene imágenes de pollos broiler de la línea Cobb Avian acompañadas de mediciones reales de peso obtenidas mediante una báscula digital.  

El dataset contiene aproximadamente 1772 imágenes de pollos broiler tomadas durante su crecimiento.

Las imágenes están organizadas en carpetas cuyo nombre corresponde al peso del animal en gramos en el momento de la medición.

Un mismo individuo puede aparecer en múltiples imágenes a lo largo del tiempo, ya que los pollos fueron fotografiados repetidamente durante el periodo experimental.

---

## Estructura del dataset

Tras descargar e inspeccionar el dataset se observa que las imágenes están organizadas en carpetas cuyo nombre corresponde al **peso del pollo en gramos**.

---

Cada carpeta contiene varias imágenes del mismo animal tomadas desde diferentes perspectivas. Por tanto, todas las imágenes dentro de una misma carpeta comparten la misma etiqueta de peso.

---

## Observaciones durante la inspección

A partir de la inspección visual del dataset se observan varios aspectos relevantes:

- En muchas imágenes el pollo aparece **sobre una báscula digital**, lo que permite verificar el peso.
- En otras imágenes el animal aparece **fuera de la báscula**, pero pertenecen al mismo individuo y mantienen la misma etiqueta de peso.
- Las fotografías están tomadas en un **entorno relativamente controlado**, con fondo uniforme y un solo animal visible.

---

## Papel en el proyecto

Este dataset constituye la **principal fuente de datos para entrenar el modelo de estimación de peso**, ya que proporciona la información clave necesaria para este problema: la correspondencia directa entre imagen y peso real.

Sin embargo, dado que las imágenes suelen contener **un único animal y un entorno controlado**, será necesario complementarlo con otros datasets que incluyan escenas con múltiples pollos y entornos más cercanos a granjas reales.

---

## Análisis del dataset

Tras la preparación del dataset se obtuvieron **1714 imágenes etiquetadas con el peso del animal**.

Los pesos registrados van desde **116 g hasta 2093 g**, con un total de **165 valores de peso distintos**.

El análisis de la distribución muestra que la mayoría de las imágenes corresponden a pollos de bajo peso (aproximadamente entre 200 g y 600 g), mientras que existen muchos menos ejemplos en rangos de peso elevados. Esto indica que el dataset presenta una **distribución desbalanceada**, con una mayor densidad de muestras en las primeras fases del crecimiento del animal.

---

# Dataset 2 – Broiler detection dataset (Kaggle)

**Fuente del dataset**

https://www.kaggle.com/datasets/lucasheilbuthh/inferring-broiler-chicken-weight

---

## Descripción general

Este dataset contiene imágenes de pollos broiler capturadas desde una **vista superior en un entorno de granja**, donde aparecen múltiples animales simultáneamente dentro del mismo encuadre.

Las imágenes parecen proceder de **secuencias de vídeo**, lo que implica que muchas de ellas corresponden a fotogramas consecutivos de una misma escena.

El objetivo principal de este dataset es facilitar tareas de **detección o segmentación de pollos en imágenes con múltiples individuos**, en contraste con otros datasets más controlados en los que aparece un único animal.

---

## Estructura del dataset

Tras inspeccionar el dataset se observa que las imágenes se encuentran organizadas en tres subconjuntos:

Pictures/  
&nbsp;&nbsp;&nbsp;&nbsp;train/  
&nbsp;&nbsp;&nbsp;&nbsp;val/  
&nbsp;&nbsp;&nbsp;&nbsp;test/  

Cada una de estas carpetas contiene aproximadamente el mismo número de imágenes.

El número aproximado de imágenes en cada subconjunto es:

- **train:** ~549 imágenes  
- **val:** ~548 imágenes  
- **test:** ~548 imágenes  

Lo que da un total aproximado de **1645 imágenes**.

---

## Observaciones durante la inspección

A partir de la inspección visual del dataset se observan varios aspectos relevantes:

- Las imágenes están tomadas desde una **cámara fija situada sobre el área donde se encuentran los pollos**.
- Cada imagen contiene **varios animales simultáneamente**, lo que introduce oclusiones y solapamientos entre individuos.
- Las condiciones de iluminación y el fondo son relativamente consistentes, lo que sugiere que las imágenes fueron capturadas en un mismo entorno experimental.

Durante la inspección también se observa que la división entre los conjuntos **train, validation y test parece haberse realizado siguiendo un patrón secuencial en los nombres de archivo**, donde imágenes consecutivas se reparten entre los distintos subconjuntos.

Esto sugiere que el dataset podría estar construido a partir de **fotogramas consecutivos extraídos de vídeos**, lo que implica que imágenes muy similares pueden encontrarse en diferentes subconjuntos.

Este aspecto debe tenerse en cuenta durante el entrenamiento, ya que podría introducir **correlaciones entre los conjuntos de entrenamiento y evaluación**.

---

## Papel en el proyecto

Este dataset resulta especialmente útil para la **tarea de detección o segmentación de pollos en escenas con múltiples individuos**.

A diferencia del dataset de Mendeley, donde las imágenes muestran generalmente **un único animal en un entorno controlado**, este dataset representa situaciones más cercanas a un **entorno real de producción avícola**, donde múltiples pollos comparten el mismo espacio.

Por este motivo, este dataset puede utilizarse para entrenar o evaluar modelos encargados de **localizar automáticamente los pollos dentro de la imagen**, paso previo necesario para poder estimar posteriormente características individuales como el tamaño o el peso del animal.

---

## Análisis preliminar del dataset

El dataset contiene aproximadamente **1645 imágenes** distribuidas de forma equilibrada entre los conjuntos de entrenamiento, validación y prueba.

Las imágenes presentan **múltiples individuos por escena**, lo que introduce una mayor complejidad visual respecto a datasets donde aparece un único animal.

Esta característica lo convierte en un recurso especialmente útil para entrenar modelos de **detección o segmentación en entornos realistas**, que posteriormente podrían combinarse con modelos de estimación de peso a partir de regiones de interés correspondientes a cada animal.

---

## Formato de anotaciones

El dataset incluye archivos de anotación en formato JSON dentro de la carpeta `Json_Files`. Durante la inspección se identifican los siguientes archivos:

traincoco.json  
valcoco.json  
trainvgg.json  
valvgg.json  

Esto indica que las anotaciones están disponibles en **dos formatos distintos**.

Para el desarrollo del proyecto se considera más conveniente utilizar el **formato COCO**, ya que es compatible con numerosos frameworks modernos de deep learning para visión por computador.

Este formato permite describir para cada imagen:

- la localización de los objetos mediante **bounding boxes**
- posibles **segmentaciones**
- metadatos adicionales asociados a cada anotación

Estas anotaciones permiten entrenar modelos capaces de **detectar o segmentar automáticamente los pollos presentes en la imagen**, lo cual constituye un paso previo necesario para poder estimar características individuales de cada animal.

---

## Estructura del archivo de anotaciones

Tras inspeccionar el archivo `traincoco.json` se observa que las anotaciones siguen la estructura típica del **formato COCO**, ampliamente utilizado en tareas de visión por computador.

El archivo contiene varias secciones principales:

- **info**: metadatos del dataset, incluyendo el año de creación y la herramienta utilizada para generar las anotaciones.
- **images**: lista de imágenes con su identificador, resolución y nombre de archivo.
- **annotations**: anotaciones asociadas a cada imagen.
- **categories**: lista de categorías presentes en el dataset.

Cada entrada en `images` incluye información como:

- identificador de la imagen
- resolución (1920×1080 píxeles)
- nombre del archivo

Ejemplo simplificado:

```
{
  "id": 0,
  "width": 1920,
  "height": 1080,
  "file_name": "000000000001.jpg"
}
```

---

## Información contenida en las anotaciones

Cada objeto anotado dentro de una imagen aparece descrito en la sección `annotations`.

Las anotaciones incluyen:

- **image_id**: identificador de la imagen a la que pertenece la anotación
- **category_id**: categoría del objeto
- **segmentation**: polígono que delimita el contorno del pollo
- **bbox**: bounding box que encierra el objeto
- **area**: área aproximada de la región segmentada
- **iscrowd**: indicador utilizado en el formato COCO para describir agrupaciones de objetos

Ejemplo simplificado de anotación:

```
{
  "image_id": 0,
  "category_id": 1,
  "segmentation": [...],
  "bbox": [x, y, width, height],
  "area": ...,
  "iscrowd": 0
}
```

Las anotaciones utilizan **segmentación poligonal**, lo que permite describir con mayor precisión la forma del animal en comparación con un simple bounding box.

---

## Categorías del dataset

En la sección `categories` se observa que el dataset incluye una única categoría:

- **chicken**

Esto indica que todas las anotaciones corresponden a **pollos presentes en la imagen**, por lo que el problema se plantea como una tarea de **detección de una sola clase de objeto**.

---

## Resolución y características de las imágenes

A partir de la inspección del JSON se observa que todas las imágenes del dataset tienen una resolución uniforme de:

**1920 × 1080 píxeles**

Esta resolución relativamente alta resulta adecuada para tareas de detección o segmentación, ya que permite conservar suficiente detalle visual para distinguir correctamente los contornos de los animales incluso cuando aparecen varios individuos dentro de la misma escena.

---

## Estadísticas de anotaciones

Se realizó un análisis adicional de los archivos de anotaciones en formato COCO para caracterizar la distribución de los objetos presentes en el dataset.

En el conjunto de entrenamiento (`train`) se obtienen las siguientes estadísticas:

- **Número de imágenes:** 549  
- **Número total de anotaciones (pollos):** 932  
- **Imágenes con al menos un pollo anotado:** 505  

Esto implica una media aproximada de **1.85 pollos por imagen**, con un mínimo de **1** y un máximo de **5** individuos en una misma escena.

En el conjunto de validación (`val`) se obtienen resultados muy similares:

- **Número de imágenes:** 548  
- **Número total de anotaciones:** 961  
- **Imágenes con anotaciones:** 504  

La media en este subconjunto es de **1.91 pollos por imagen**, con un máximo de **4** individuos en una misma imagen.

Estos resultados indican que, aunque el dataset incluye escenas con múltiples animales, la **densidad de pollos por imagen es relativamente baja**, lo que reduce el nivel de oclusión entre individuos.

---

## Tamaño de los objetos anotados

También se analizó el tamaño de las *bounding boxes* asociadas a cada anotación.

En el conjunto de entrenamiento:

- **Área media de las bounding boxes:** 79,418 píxeles  
- **Área mínima:** 49,786 píxeles  
- **Área máxima:** 108,830 píxeles  

En el conjunto de validación:

- **Área media:** 81,354 píxeles  
- **Área mínima:** 48,158 píxeles  
- **Área máxima:** 114,821 píxeles  

Estos valores indican que los pollos ocupan una **porción relativamente grande de la imagen**, lo que facilita su detección mediante modelos de visión por computador.

---

# Dataset 4 – Broiler weight dataset (Roboflow)

**Fuente del dataset**

https://universe.roboflow.com/mohamed-f-abdelshafie-yxuwl/broiler-live-weight-by-semantic-segmentation

---

## Descripción general

Este dataset contiene imágenes de pollos broiler fotografiados sobre una báscula digital, de forma muy similar al dataset **Broiler weights of Cobb Avian (Mendeley)**.

Las imágenes muestran un único pollo y en al menos una foto por individuo el animal está situado sobre una báscula, lo que permite visualizar directamente el peso registrado en el momento de la captura.

Durante la inspección visual se observa que el estilo de las imágenes, el entorno y el tipo de captura parecen corresponder al mismo experimento utilizado en el dataset de Mendeley.

---

## Estructura del dataset

El dataset está dividido en tres subconjuntos:

train/  
valid/  
test/  

El peso del animal no aparece en el nombre de las carpetas, sino que está **codificado en el nombre del archivo de imagen**.

Ejemplo: 140_139-5....jpg

En este caso:

- **139** corresponde al peso del pollo en gramos.

---

## Observaciones durante la inspección

Durante la inspección del dataset se detectaron varios aspectos relevantes:

- Algunas imágenes parecen **duplicadas o muy similares**, posiblemente debido a exportaciones o aumentos de datos realizados en Roboflow.
- El estilo de las imágenes coincide con el dataset de **Mendeley**, lo que sugiere que ambos podrían proceder del mismo conjunto experimental.

Por este motivo será necesario verificar cuidadosamente la existencia de **duplicados entre ambos datasets** antes de combinarlos para el entrenamiento de modelos.

---

## Papel en el proyecto

Este dataset podría utilizarse como **complemento al dataset de Mendeley** para ampliar el número total de imágenes disponibles para la tarea de **estimación de peso del pollo a partir de imágenes**.

Sin embargo, antes de su uso será necesario realizar un proceso de **limpieza y verificación de duplicados**, especialmente si se pretende combinar ambos datasets.

---

## Preparación del dataset

A diferencia del dataset de Mendeley, en este caso las imágenes no están organizadas en carpetas cuyo nombre corresponda al peso del animal.  

En su lugar, como se ha mencionado antes, el **peso aparece codificado dentro del nombre del archivo**.

Para poder utilizar el dataset de forma consistente con el dataset de Mendeley, se desarrolló un script de preparación (`prepare_roboflow_broiler_weight.py`) que realiza las siguientes tareas:

- Recorre las carpetas `train`, `valid` y `test` del dataset original.
- Extrae el peso del animal a partir del nombre del archivo.
- Copia todas las imágenes a una única carpeta de trabajo.
- Genera un archivo `labels.csv` que contiene la correspondencia entre cada imagen y su peso.

De esta forma el dataset queda transformado a un formato homogéneo:

data/02_work/roboflow_broiler_weight_dataset/

images/  
labels.csv  

Este formato es equivalente al utilizado para el dataset de Mendeley y permite trabajar posteriormente con ambos datasets de forma conjunta.

---

## Análisis de duplicados entre datasets

Dado que este dataset fue publicado por el **mismo autor que el dataset de Mendeley**, surgió la posibilidad de que existieran **imágenes duplicadas entre ambos conjuntos de datos**.

Para comprobarlo se desarrolló un script de análisis (`check_duplicates_weight_datasets.py`) que calcula un **hash perceptual (pHash)** para cada imagen de ambos datasets y compara sus distancias.

Este tipo de hash permite detectar:

- imágenes idénticas
- imágenes muy similares
- imágenes con pequeñas variaciones (recortes, compresión, etc.)

El análisis comparó:

- **1714 imágenes del dataset de Mendeley**
- **4344 imágenes del dataset de Roboflow**

Los resultados obtenidos fueron:

- **545 posibles duplicados detectados**

Entre ellos se encuentran múltiples casos con **distancia de hash igual a 0**, lo que indica que las imágenes son **exactamente idénticas**.

Ejemplo de coincidencias detectadas:

dist=0  
Mendeley : img_01093.jpg  
Roboflow : img_01639.jpg  

dist=0  
Mendeley : img_01159.jpg  
Roboflow : img_01018.jpg  

dist=2  
Mendeley : img_01159.jpg  
Roboflow : img_01111.jpg  

Estos resultados indican que el dataset de Roboflow **reutiliza parcialmente imágenes del dataset original de Mendeley**, o que ambos conjuntos de datos comparten una misma fuente de imágenes.

---

## Implicaciones para el proyecto

La presencia de duplicados entre datasets es un aspecto importante a tener en cuenta, ya que podría introducir **fugas de información entre conjuntos de entrenamiento y evaluación** si ambos datasets se utilizaran simultáneamente.

Por este motivo, antes de combinar ambos datasets será necesario considerar estrategias como:

- eliminar duplicados exactos
- eliminar imágenes muy similares
- mantener únicamente las imágenes únicas de cada dataset

Este análisis permite comprender mejor la relación entre ambos datasets y garantizar que los experimentos posteriores se realicen sobre datos **independientes y representativos**.

---

## Construcción del dataset final de pesos combinado

Con el objetivo de aumentar el número total de ejemplos disponibles para la tarea de estimación de peso, se procedió a combinar el dataset de **Mendeley** con el dataset de **Roboflow**.

Sin embargo, dado que ambos datasets comparten autor y presentan similitudes evidentes en las imágenes, era necesario verificar la existencia de **duplicados entre ambos conjuntos de datos**.

Para ello se desarrolló un script (`build_final_weight_dataset.py`) que realiza los siguientes pasos:

1. Lee las imágenes y etiquetas de ambos datasets preparados.
2. Calcula un **hash perceptual (pHash)** para cada imagen.
3. Detecta imágenes duplicadas o muy similares mediante la comparación de distancias entre hashes.
4. Elimina las imágenes redundantes.
5. Genera un **dataset final combinado libre de duplicados**.

El proceso se realizó sobre:

- **1714 imágenes del dataset de Mendeley**
- **4344 imágenes del dataset de Roboflow**

lo que da un total inicial de:

6058 imágenes.

Tras aplicar la detección de duplicados se identificaron:

- **1297 imágenes duplicadas o muy similares**

El dataset final resultante contiene:

- **4761 imágenes únicas con su correspondiente etiqueta de peso**

La estructura final del dataset generado es:

data/03_final/broiler_weight_dataset/

images/  
labels.csv  

Este dataset final constituye el **conjunto de datos principal para el entrenamiento de modelos de estimación de peso a partir de imágenes**, ya que combina información de ambos datasets manteniendo únicamente imágenes independientes.

---

## Distribución del dataset final de pesos

Una vez combinado el dataset de Mendeley con el dataset de Roboflow y eliminados los duplicados, se analizó la distribución de pesos del dataset final.

El dataset final contiene:

- **4761 imágenes**
- **pesos entre 116 g y 2093 g**
- **168 valores de peso distintos**

Las estadísticas descriptivas obtenidas son:

| Métrica | Valor |
|-------|------|
| Peso mínimo | 116 g |
| Peso máximo | 2093 g |
| Media | 471 g |
| Mediana | 371 g |
| Percentil 75 | 542 g |

El histograma de distribución muestra que la mayor parte de las muestras se concentran en el rango aproximado de:

**200 g – 600 g**

correspondiente a las primeras fases de crecimiento del pollo.

En cambio, existen relativamente pocas muestras en rangos de peso elevados (por encima de 1200 g).

Esto indica que el dataset presenta una **distribución desbalanceada**, con mayor representación de pollos jóvenes que de pollos cercanos a su peso final.

Aun así, el dataset cubre todo el rango de crecimiento del animal y proporciona una base adecuada para entrenar modelos de **estimación de peso a partir de imágenes**.