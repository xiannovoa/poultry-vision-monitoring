# Análisis de datasets

Este documento recoge el proceso de inspección, organización y curación de las fuentes de imágenes utilizadas en la parte del proyecto dedicada a la **clasificación de enfermedades aviares a partir de imágenes de heces de gallina**.

El objetivo es construir un dataset útil, depurado y reutilizable que permita abordar una tarea principal:

1. Clasificación multiclase de imágenes de heces de gallina en cuatro categorías:
   - healthy
   - coccidiosis
   - newcastle
   - salmonella

---

# Descripción general del proyecto de dataset

La fase actual del proyecto se ha centrado en construir una **versión baseline limpia del dataset final**, a partir de varias fuentes públicas descargadas de internet y conservadas localmente sin modificar en la carpeta `01_raw/`. Durante este proceso se ha realizado la organización de fuentes, la unificación de etiquetas, la comprobación de archivos, la deduplicación exacta, la reducción de solapamiento fuerte entre fuentes, la asignación de identificadores únicos y la exportación de una versión final ya utilizable.

A día del estado actual del proyecto, el dataset final baseline ya existe, es usable, trazable y reutilizable. Sin embargo, todavía no incluye particiones `train/val/test` ni una revisión visual manual exhaustiva imagen por imagen.

---

# Fuentes utilizadas

Para construir el dataset final se trabajó con tres fuentes principales, cada una almacenada por separado dentro de `01_raw/`. Estas fuentes presentan estructuras diferentes, por lo que fue necesario normalizarlas antes de poder combinarlas dentro de un único inventario maestro.

Las referencias recopiladas de las fuentes utilizadas son las siguientes:

- `src01_main`: dataset principal de imágenes de heces y etiquetas asociadas
- `src02_poultry`: dataset complementario organizado por carpetas de clase
- `src03_extra`: fuente adicional usada para ampliar algunas clases

---

# Dataset 1 – Fuente principal (`src01_main`)

**Fuente del dataset**

Dataset público descargado localmente y almacenado en:

`01_raw/src01_main/`

---

## Descripción general

Esta fuente constituye el núcleo principal del proyecto. Contiene imágenes de heces de gallina organizadas en una carpeta `Train/`, mientras que las etiquetas se almacenan en un archivo `train_data.csv` que asocia cada nombre de imagen con su clase original.

Durante la fase de inspección se comprobó que la estructura era consistente: el número de imágenes presentes en `Train/` coincide exactamente con el número de filas del archivo `train_data.csv`. En total, esta fuente contiene **8067 imágenes** y **8067 filas de datos**, por lo que no se detectaron desajustes entre imágenes y etiquetas en esta fase inicial.

---

## Estructura del dataset

Tras la inspección de esta fuente se observa la siguiente organización:

`src01_main/`  
&nbsp;&nbsp;&nbsp;&nbsp;`Train/`  
&nbsp;&nbsp;&nbsp;&nbsp;`train_data.csv`

A diferencia de otras fuentes del proyecto, aquí las clases no están separadas en carpetas, sino que la correspondencia entre imagen y etiqueta depende del archivo CSV de anotaciones. Esto hizo necesaria una fase específica de lectura del CSV y construcción de índice para poder integrar esta fuente con el resto.

---

## Observaciones durante la inspección

Durante la inspección estructural de `src01_main` se observó que la fuente ya era internamente consistente y que podía utilizarse como base fiable para el inventario maestro. La comprobación entre contenido real de la carpeta e información del CSV dio resultado correcto, sin archivos faltantes en esta etapa.

Además, esta fuente fue posteriormente priorizada frente a otra fuente parcialmente solapada durante la fase de reducción de redundancia multifuente, lo que indica que se consideró la referencia principal para conservar ejemplos equivalentes cuando aparecían en varias colecciones.

---

## Papel en el proyecto

`src01_main` actúa como la **fuente principal** para la construcción del dataset final. Por su tamaño, consistencia interna y papel dentro de las decisiones de limpieza, constituye la base más importante del conjunto final utilizado para clasificación multiclase de enfermedades.

---

# Dataset 2 – Fuente complementaria (`src02_poultry`)

**Fuente del dataset**

Dataset público descargado localmente y almacenado en:

`01_raw/src02_poultry/`

---

## Descripción general

Esta segunda fuente contiene imágenes organizadas directamente en carpetas por clase. En concreto, se identifican las carpetas `cocci`, `healthy`, `ncd` y `salmo`, que posteriormente se mapearon a las cuatro etiquetas oficiales del proyecto.

Durante la inspección inicial se contabilizaron **6812 imágenes** en total, repartidas entre las diferentes clases. Esta fuente aportó una cantidad importante de ejemplos, pero también mostró un fuerte solapamiento con la fuente principal en fases posteriores del análisis.

---

## Estructura del dataset

La estructura observada en esta fuente es la siguiente:

`src02_poultry/`  
&nbsp;&nbsp;&nbsp;&nbsp;`cocci/`  
&nbsp;&nbsp;&nbsp;&nbsp;`healthy/`  
&nbsp;&nbsp;&nbsp;&nbsp;`ncd/`  
&nbsp;&nbsp;&nbsp;&nbsp;`salmo/`

El recuento por carpetas obtenido durante la inspección fue:

- **cocci:** 2103 imágenes
- **healthy:** 2057 imágenes
- **ncd:** 376 imágenes
- **salmo:** 2276 imágenes

lo que suma un total de **6812 imágenes**.

---

## Observaciones durante la inspección

A diferencia de `src01_main`, esta fuente no utiliza un CSV de etiquetas, sino que la clase viene determinada por el nombre de la carpeta. Esto simplifica su lectura inicial, aunque obliga a estandarizar los nombres de clase para integrarlos con el resto del proyecto.

Durante el análisis de similitud multifuente se detectó un solapamiento fuerte entre `src02_poultry` y `src01_main`. En concreto, se cuantificaron **4670 casos de solapamiento fuerte** entre ambas fuentes, por lo que se decidió conservar los ejemplos de `src01_main` y descartar las copias equivalentes de `src02_poultry` dentro del inventario final.

---

## Papel en el proyecto

Esta fuente se utilizó como **dataset complementario** para ampliar el número total de ejemplos disponibles por clase. No obstante, debido al solapamiento detectado con la fuente principal, fue necesario aplicar reglas de limpieza para evitar inflar artificialmente el tamaño del dataset mediante imágenes redundantes.

---

# Dataset 3 – Fuente adicional (`src03_extra`)

**Fuente del dataset**

Dataset público descargado localmente y almacenado en:

`01_raw/src03_extra/`

---

## Descripción general

La tercera fuente del proyecto se utilizó como conjunto adicional para ampliar clases concretas. Está organizada por carpetas y contiene únicamente ejemplos de `Coccidiosis` y `Healthy`, que posteriormente se mapearon a las etiquetas finales `coccidiosis` y `healthy`.

Durante la inspección inicial se contabilizaron **390 imágenes** en total, repartidas de forma equilibrada entre ambas clases.

---

## Estructura del dataset

La estructura observada es la siguiente:

`src03_extra/`  
&nbsp;&nbsp;&nbsp;&nbsp;`Coccidiosis/`  
&nbsp;&nbsp;&nbsp;&nbsp;`Healthy/`

El recuento por carpetas fue:

- **Coccidiosis:** 195 imágenes
- **Healthy:** 195 imágenes

Total: **390 imágenes**.

---

## Observaciones durante la inspección

Esta fuente presenta una estructura simple y homogénea. Al aportar solo dos clases, no cubre por sí sola el problema completo de clasificación multiclase, pero sí resulta útil como refuerzo parcial del inventario global. Además, sus etiquetas originales usan mayúsculas y nombres distintos a otras fuentes, por lo que también fue necesario integrarlas mediante el mapeo general de clases del proyecto.

---

## Papel en el proyecto

`src03_extra` se utilizó como **fuente auxiliar** para complementar el dataset global. Su función principal fue aportar ejemplos adicionales en clases concretas dentro del proceso de agregación multifuente.

---

# Unificación de etiquetas

Dado que las distintas fuentes utilizaban nombres de clase diferentes, fue necesario definir un conjunto único de etiquetas oficiales para todo el proyecto. Las únicas etiquetas finales válidas quedaron fijadas como:

- **healthy**
- **coccidiosis**
- **newcastle**
- **salmonella**

Los mapeos aplicados durante la normalización fueron los siguientes:

- `Healthy -> healthy`
- `Coccidiosis -> coccidiosis`
- `Salmonella -> salmonella`
- `New Castle Disease -> newcastle`
- `cocci -> coccidiosis`
- `healthy -> healthy`
- `ncd -> newcastle`
- `salmo -> salmonella`

Este paso fue esencial para poder combinar todas las fuentes dentro de un único índice maestro coherente y utilizar después el dataset de forma homogénea en tareas de aprendizaje automático.

---

# Recuento inicial unificado antes de la limpieza

Una vez integradas las tres fuentes y unificadas sus etiquetas, se obtuvo un inventario bruto conjunto con **15269 imágenes**. La distribución inicial por clase fue la siguiente:

- **coccidiosis:** 4774
- **healthy:** 4656
- **newcastle:** 938
- **salmonella:** 4901

Este recuento inicial representa la suma de todas las imágenes disponibles antes de aplicar los procesos de limpieza, deduplicación exacta y reducción de solapamiento fuerte entre fuentes.

---

# Proceso de curación del dataset

La construcción del dataset final no consistió únicamente en unir carpetas, sino en un proceso de curación progresiva automatizado mediante varios scripts.

Entre las tareas realizadas se incluyen:

- separación de fuentes originales
- creación de inventario maestro
- verificación de existencia de archivos
- comprobación de etiquetas finales
- detección y eliminación de duplicados exactos
- reducción de solapamiento fuerte entre fuentes
- asignación de IDs únicos
- renombrado final de archivos
- exportación de `labels.csv` y `sources.csv`

---

# Detección de duplicados exactos

Una parte importante del proceso fue la detección y eliminación de duplicados exactos. Para ello se desarrolló una serie de scripts específicos de hashing y conteo de duplicados, con el fin de evitar que el dataset final quedara inflado artificialmente por imágenes repetidas.

La eliminación de duplicados exactos se aplicó sobre el inventario maestro antes del análisis de solapamiento fuerte entre fuentes, formando parte de la limpieza base previa a la congelación de la baseline final.

---

# Análisis de similitud y solapamiento entre fuentes

Además de los duplicados exactos, se realizó un análisis de similitud para detectar grupos de imágenes con el mismo nombre, la misma clase y una apariencia muy parecida entre distintas fuentes. Para ello se utilizaron análisis por nombre y `pHash`, lo que permitió caracterizar el solapamiento multifuente.

Los resultados intermedios de este análisis fueron:

- **6494** grupos con mismo nombre y misma clase en varias fuentes
- de esos, **4670** grupos con mismo `pHash`
- de esos, **1824** grupos con `pHash` distinto

A partir de estos resultados se cuantificó específicamente el solapamiento fuerte entre:

- **`src01_main` <-> `src02_poultry`: 4670 casos**

---

# Decisión de limpieza multifuente

Para mantener un dataset más limpio y menos redundante, se aplicó una regla clara durante los casos fuertes de solapamiento multifuente:

- **conservar `src01_main`**
- **descartar la copia equivalente en `src02_poultry`**

Esta decisión no se implementó borrando archivos originales, sino marcando las decisiones sobre el inventario maestro. De este modo se mantuvo intacta la carpeta `01_raw/`, que actúa como copia original trazable y recuperable de las fuentes descargadas.

---

# Construcción de la baseline limpia final

Tras aplicar la eliminación de duplicados exactos y la reducción del solapamiento fuerte entre fuentes, se obtuvo el estado limpio actual del dataset. El resultado fue:

- **keep:** 9611
- **drop:** 5658
- **review:** 0

La distribución por clase dentro del conjunto `keep` quedó en:

- **coccidiosis:** 2958
- **healthy:** 2985
- **newcastle:** 659
- **salmonella:** 3009
- **total:** 9611

Esta versión limpia se congeló como baseline final y sirvió como base para la asignación de IDs, renombrado de archivos y exportación del dataset materializado.

---

# Asignación de IDs y exportación del dataset final

Una vez fijada la baseline limpia, se asignó a cada imagen conservada un identificador único estable con formato:

- `CFD_00001`
- `CFD_00002`
- etc.

A partir de estos identificadores se generaron los nombres finales de archivo, utilizando el `image_id` y manteniendo la extensión original. Posteriormente se exportaron los tres elementos principales del dataset final:

1. `images/`
2. `labels.csv`
3. `sources.csv`

El archivo `labels.csv` contiene:

- `image_id`
- `filename`
- `label`

mientras que `sources.csv` contiene:

- `image_id`
- `filename`
- `source_id`
- `original_filename`
- `original_label`
- `raw_path`

---

# Verificación de coherencia final

Una vez exportado el dataset final, se verificó la coherencia entre el contenido de la carpeta de imágenes y los archivos CSV generados. Los resultados fueron:

- **imágenes en carpeta:** 9611
- **filas en `labels.csv`:** 9611
- **filas en `sources.csv`:** 9611

Esto confirma que la versión final baseline está correctamente materializada y que cada imagen exportada dispone tanto de etiqueta final como de trazabilidad hacia su fuente de origen.

---

# Papel del dataset en el proyecto

El dataset final construido constituye la **base principal para entrenar y evaluar modelos de clasificación de enfermedades aviares a partir de imágenes de heces**. Su principal fortaleza no reside solo en el número de imágenes, sino en haber sido curado con una lógica clara de unificación, trazabilidad y reducción de redundancia.

Frente a una simple agregación de carpetas, el resultado actual es un dataset:

- usable
- trazable
- reutilizable
- documentado
- materializado en una estructura clara

---

# Limitaciones actuales

Aunque la baseline actual es plenamente utilizable, la documentación del proyecto indica varias tareas que todavía no se han realizado:

- revisión visual manual amplia
- detección y decisión manual fina sobre casi duplicados
- creación de particiones `train/val/test` o folds
- elaboración de una dataset card más formal o extensa

Estas limitaciones no impiden utilizar el dataset, pero sí indican que la versión actual debe entenderse como una **baseline limpia y práctica**, no como una versión curada manualmente al máximo nivel.

---

# Conclusión

El proyecto ya dispone de un **dataset final baseline útil, depurado y reutilizable** para clasificación multiclase de enfermedades aviares a partir de imágenes de heces. El conjunto final contiene **9611 imágenes** distribuidas en cuatro clases oficiales, con etiquetas unificadas, IDs únicos, archivos finales consistentes y trazabilidad por imagen hacia la fuente original.

No se trata únicamente de una colección de imágenes descargadas, sino de un dataset construido mediante un proceso explícito de curación que incluye inventario, verificación, deduplicación exacta, reducción de solapamiento fuerte entre fuentes y exportación final. Esto proporciona una base sólida para entrenar modelos más adelante, crear particiones en fases posteriores y seguir refinando el recurso sin perder la trazabilidad de lo ya hecho.