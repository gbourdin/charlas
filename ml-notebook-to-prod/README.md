# Machine Learning: Del Notebook a Producción
En este repo esta todo el material de soporte de la charla que di en la PyConAr 2018 titulada "Machine Learning: Del Notebook a Producción".

Van a encontrar las slides, los ejemplos que use, los notebooks, los datos que use para entrenar y un par de cookiecutters que prepare para armar wrappers de predictores y apis que sirven proyectos de machine learning.

Contenido:

**cookiecutters**

Aca van a encontrar api-template y predictor-template que son los que use para crear todos los ejemplos de la charla

**examples**

Acá van a encontrar  housingExample y mnistExample:

**housingExample**:

- Implementa 2 predictores de precios de casas basados en las siguientes features:
    + Cantidad de habitaciones
    + Cantidad de baños
    + Superficie cubierta
    + Superficie del terreno
    + Año de construccion
- Hay modelos entrenados para cada uno de los predictores
- Hay una API REST configurada para servir el modelo basado en xgboost
- Hay un frontend web para usar el predictor

**mnistExample**

- Implementa un predictor basado en el ejemplo del tutorial de tensorflow que clasifica digitos escritos a mano
- Hay modelos entrenados con distinta cantidad de epochs para el modelo
- Hay una API REST configurada para servir el modelo
- Hay un frontend web para poder dibujar numeros y obtener predicciones


**input**

Acá está el dataset de kaggle que utilicé para entrenar los modelos de housingExample


**notebooks**

Hay un par de notebooks que no llegué a mostrar durante la charla donde juego un poco con los datos y voy probando distintos modelos que implementé luego


**slides**
El codigo fuente y las slides compiladas que utilice en la charla

German Bourdin
