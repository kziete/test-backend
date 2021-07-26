# Talana Test (buscar nombre más llamativo)

Una pequeña historia, bla, bla, bla

## Requisitos

- docker
- docker-compose

## Iniciar

`docker-compose up`

### Swagger

http://localhost:8000/api/schema/swagger-ui/


### Mailhog

http://localhost:1025

## Test
`docker-compose run --rm web pytest`

## Tareas
pas

### Terminar tests skipeados

Desarrollar el código necesario propuesto por los test skipeados (debes remover el marcador `@pytest.mark.skip` para habilitar el test)

### Refactorizar código legacy

Si ves que ciertos modulos están desorneados o no respetan una arquitectura limpia, puedes refactorizar el código
recuerda que los test deben pasar el refactor

