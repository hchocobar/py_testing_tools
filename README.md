# Python, Herramientas para Testing

## Descripción

El siguiente es un ejemplo cuyo objetivo es comprender y utilizar distintas herramientas de testing en un proyecto de Python.

El testing es una parte fundamental de cualquier aplicación, que permite validar automáticamente el correcto funcionamiento de la misma. 

## Herramientas de Testing utilizadas

- **Pytest** para **Unit Testing**.

  El testing unitario se encarga de validar el comportamiento aislado de los componentes de nuestro código.


- **Hypothesis** para **Property Based Testing**.

  Basado en la creación de tests válidos para cualquier combinación de parámetros que se le pueda pasar a la función de testing.


- **Schemathesis** para **Contract Testing**. 

  Se basa en la utilización de API contract para comprobar que la implementación del mismo se realiza de forma correcta.


- **Locust** para **Load Testing**.

  Basado en la creación de usuarios virtuales para generar carga sobre nuestra aplicación, y comprobar cómo se comporta.

## Instalación

Instalar dependencias utilizando pip:

    $ pip install fastapi
    $ pip install uvicorn
    $ pip install schemathesis
    $ pip install locus

## Ejecución de Hypothesis

Luego de ejecutar app/main, utilizar las siguientes urls en el browser.

    http://127.0.0.1:8000
    http://127.0.0.1:8000/docs
    http://127.0.0.1:8000/redoc

## Ejecución de Schemathesis

En la terminal ejecutar el siguiente comando:

    schemathesis run http://127.0.0.1:8000/openapi.json

## Ejecución de Pytest

En la terminal ejecutar el siguiente comando:

    pytest

## Ejecución de Locust

En la terminal ejecutar el siguiente comando:

    locust -f load_testing/calculator_user.py 

> **Importante** 
> >Con la versión 2.2.2 de Flask da un error; mientras que con la versión 2.1.3 de Flask funciona correctamente.
> > [Ver en Stackoverflow la solución al error con Flask 2.2.2](https://stackoverflow.com/questions/73337927/typeerror-init-got-an-unexpected-keyword-argument-unbound-message)


# Enlaces útiles

[Python](https://www.python.org) | 
[FastAPI](https://fastapi.tiangolo.com/) |
[uvicorn](https://www.uvicorn.org/) |
[pydantic](https://pydantic-docs.helpmanual.io/) |

[pytest](https://docs.pytest.org/en/stable/) |
[Hypothesis](https://hypothesis.readthedocs.io/en/latest/) |
[Schemathesis](https://schemathesis.readthedocs.io/en/stable/) |
[Locust](https://docs.locust.io/en/stable/)

# Muchas Gracias

[Héctor Chocobar Torrejón](http://chocobar.net)

![Avatar de Héctor](https://en.gravatar.com/userimage/146115819/41a333edd75fea5257a0a684c76cf977.png)
