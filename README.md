# Talana Test (buscar nombre más llamativo)

Una pequeña historia, bla, bla, bla

## Requisitos

- docker
- docker-compose

## Ejecución

```bash
docker-compose run --rm web pytest
```

## Tareas

### Corregir Tests

Corregir todo el código necesario para que los tests previos pasen.

se recomienda proceder por el siguiente orden test_entities > test_usecases > test_controllers

pero si lo deseas, puedes hacerlo en cualquier orden

### Terminar tests skipeados

Diseñar el codigo necesario propuesto por los test skipeados, así como los tests mismos. Con el objetivo de desarrollar un api para finalizar un `Journey`

### Refactorizar código legacy

Si ves que ciertos modulos están desorneados o no respetan una arquitectura limpia, puedes refactorizar el código
recuerda que los test deben pasar el refactor

### Agregar capa de autenticacion

Nuestro dev no alcanzo a autenticar el api, hagalo pues
