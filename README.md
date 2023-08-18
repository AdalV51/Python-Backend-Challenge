# Python Backend Challenge 🚀

¡Bienvenido al desafío de Python Backend!

En este emocionante reto, evaluaremos tu capacidad para aprender (pues utilizaremos un framework con el que quizás no estés muy familiarizado, como FastAPI) y tus conocimientos sobre las API REST. Este ejercicio tiene como objetivo conocer tus habilidades en Python. Tendrás dos días para completarlo y, si tienes alguna duda, ¡no dudes en preguntarnos!

## Para Empezar

¡Comencemos a trabajar en este emocionante proyecto!

1. Haz un fork de este repositorio en GitHub y luego clona el fork a tu máquina local para tener el código disponible y listo para trabajar.
2. Se requiere Docker Desktop y puede ser descargado e instalado desde [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)

Suponiendo que tienes Docker instalado y funcionando en tu máquina, simplemente ejecuta:

```
docker compose up
```

Luego podrás acceder a la aplicación en el puerto 8000 de la dirección IP de tu máquina Docker, posiblemente [http://localhost:8000/](http://localhost:8000/)

La documentación de FastAPI está disponible aquí: [http://localhost:8000/docs](http://localhost:8000/docs)

## Descripción del Problema

Este proyecto es una API que administra una lista de tareas (TODO list). Puedes crear TODOs y cada uno de ellos puede contener ITEMS. Cada TODO tiene la siguiente estructura:

```
{
    "title": "Tarea 35",
    "description": "Descripción para la Tarea 35",
    "due_date": "2023-08-22",
    "id": 36
}
```

Cada ITEM de TODO está vinculado a un TODO y tiene la siguiente estructura:

```
{
    "title": "Item 0 de la Tarea 35",
    "description": "Descripción para el Item 0 de la Tarea 35",
    "todo_id": 36,
    "id": 176
}
```

La base de datos ya está incluida en los archivos, así que deberías ser capaz de acceder a la siguiente URL para ver los registros existentes: [http://localhost:8000/todos/](http://localhost:8000/todos/)

Otra característica interesante es que la imagen de Docker que estás ejecutando (después de ejecutar ``` docker compose up ```) permite que realices cambios en la aplicación y esta se recargará automáticamente cuando guardes los cambios (recarga en caliente). En caso de que encuentres algún problema, simplemente detén el contenedor (Ctrl + C) y vuelve a ejecutar ``` docker compose up ```

## Tarea 1: Agrega Paginación

Agrega paginación al método GET ``` /todos/ ``` para que la siguiente URL funcione:

```
GET /todos/?page=1&page_size=10
```

TIP: Utiliza los parametros skip y limit que ya vienen definidos, despues de unos pequeños cambios podran ser utilizados como page y page_size.

## Tarea 2: Corrige el Método DELETE

Agrega el método necesario para que el endpoint ``` DELETE /todos/ ``` funcione correctamente.

## Tarea 3: Agrega un Nuevo Endpoint

Agrega un nuevo endpoint ``` GET /todos/ordered/ ``` que devuelva una lista completa de las tareas ordenadas por fecha (due_date) de la más próxima a la más lejana.

## Tarea 4: ¡BONO! Mejora la API

¡Agrega algo que haga que esta API sea aún mejor! Muéstranos tus habilidades y cómo puedes llevar esta aplicación al siguiente nivel.

## ¿Acabaste?

## ¿Acabaste?

Cuando hayas completado todas las tareas del desafío y estés listo para que revisemos tus respuestas, sigue estos pasos para enviar un Pull Request desde tu fork:

1. Asegúrate de haber guardado y confirmado todos los cambios que has realizado en tu repositorio local.
2. Accede a tu fork en GitHub. Debería estar en la URL `https://github.com/TU_NOMBRE_DE_USUARIO/fastapi-challenge` (reemplaza `TU_NOMBRE_DE_USUARIO` con tu nombre de usuario en GitHub).
3. Haz clic en el botón "Pull Request" en la parte superior de la página.
4. Selecciona el botón verde "New Pull Request".
5. Asegúrate de que las ramas "base" y "compare" estén configuradas correctamente. La rama "base" debería ser "main" o "master" en el repositorio original, y la rama "compare" debería ser la rama en la que has realizado tus cambios.
6. Proporciona un título descriptivo para tu Pull Request, como "Solución para el desafío de paginación".
7. En la descripción, puedes incluir cualquier información adicional que quieras compartir sobre tu enfoque, decisiones de diseño o cualquier otra cosa que consideres relevante.
8. Asegúrate de revisar tus cambios en la pestaña "Files Changed" para confirmar que todos los cambios que deseas enviar se incluyen en el Pull Request.
9. Una vez que estés satisfecho con la información proporcionada y los cambios mostrados, selecciona el botón verde "Create Pull Request".
10. ¡Listo! Tu Pull Request se enviará y nosotros nos encargaremos de revisar tus respuestas.

¡Buena suerte! Estamos emocionados de ver lo que puedes lograr en este desafío. ¡Diviértete programando! 😄🚀
