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

### Nuevo Endpoint

Desarrollar un endpoint para finalizar un `Journey`


### Refactorizar código legacy

Si ves que ciertos modulos están desorneados o no respetan una arquitectura limpia, puedes refactorizar el código
recuerda que los test deben pasar el refactor
