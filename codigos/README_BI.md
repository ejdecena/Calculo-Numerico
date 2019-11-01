# Proyecto en Python sobre el Algoritmo de Bisección.

### Cada participante debe completar su módulo y luego solicitar el Pull-Request (PR).

A cada participante se le presenta un módulo en lenguaje *Python* con la siguiente estructura:

```python
import math


def biseccion(f, a, b, ER, N):
    """
    Implementa el Algoritmo de Biseccion y retorna la aproximación de la raíz.

    Parámetros:
    f: función de variable real f(x).
    a: límite inferior del intervalo.
    b: límite superior del intervalo.
    ER: cota mínima del error relativo.
    N: número máximo de iteraciones.
    """

    print("Iteración:", i, "Punto Medio:", pm_actual, "Error:", err)

    return pm_actual


if __name__ == "__main__":
    # Pruebe aquí su función.
    pass
```
## Requerimientos.

1. El participante deberá completar en su módulo la función `biseccion(f, a, b, ER, N)`, mostrando por pantalla mediante la instrucción `print()` el **contador de iteración**, el **punto medio** y el **error relativo** de la iteración, mediante `print("Iteración:", i, "Punto Medio:", pm_actual, "Error:", err)`.
2. La función `biseccion(f, a, b, ER, N)` **deberá retornar** la aproximación de la raíz o cero de la función `f` pasada por parámetro; es decir, deberá retornar el **último punto medio** calculado (`pm_actual`).
3. El participante deberá probar su función `biseccion(f, a, b, ER, N)` en la sección `main` del código, pudiendo implementar funciones adicionales para las pruebas. Las **funciones lambda** pueden ser de utilidad.

## Notas.

**NOTA 1**: Cualquier duda o pregunta sobre este proyecto, por favor abra un [**issue**](https://github.com/ejdecena/proyecto_biseccion/issues).

**NOTA 2**: Solo se recibirá UNA y solo una petición de PR por participante.

**NOTA 3**: Marque con **Watch** este repositorio para que reciba todas las notificaciones.

**NOTA 4**: Recuerde que hay un [**Tutorial Git**](https://github.com/ejdecena/tutorial_git) y un [**Tutorial Python**](https://github.com/ejdecena/tutorial_python) que pueden ser útiles en caso de cualquier duda.

**NOTA 5**: Se recibirán solicitudes de PR hasta el día **miércoles 30 de octubre de 2019, 11:59 pm**, SIN PRÓRROGA.