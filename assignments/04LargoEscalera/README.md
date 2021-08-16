![Tec de Monterrey](../../images/logotecmty.png)
# Calcula Tiempo
Básicos-Calcula tiempo

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
    #escribe tu código abajo de esta línea
    pass

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

<br>Escribe un programa que determine el largo que debe tener una escalera, la cual se necesita para alcanzar una altura determinada, cuando se pone contra una casa. La altura que se desea alcanzar y el ángulo que deberá hacer la escalera contra la pared, son datos que te proporciona el usuario. Para calcular el largo de la escalera usa la siguiente ecuación: largo=altura/seno(ángulo). Recuerda que las funciones de Python que calculan seno y coseno, reciben los ángulos en radianes, pero tu programa va a recibir los ángulos en grados.

<br><b>Entrada</b>

<br>Un número que corresponde a la altura de la casa (flotante positivo) y el ángulo en grados (entero positivo), en ese orden.

<br><b>Salida</b>

<br>Un número, un número que representa el largo que debe tener la escalera. IMPORTANTE: Redondea el número para que el resultado sea entero. Utiliza la función adecuada que te provee Python para realizar un redondeo.

<br><b>Ejemplo:</b>

<br>>>> 2

<br>>>> 45

<br>3

**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
