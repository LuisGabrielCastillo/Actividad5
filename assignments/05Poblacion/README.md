![Tec de Monterrey](../../images/logotecmty.png)
# Crecimiento de población
Básicos-Crecimiento de población

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
    #escribe tu código abajo de esta línea
    pass

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

<br><b>Crecimiento de población</b>
<br>Escribe un programa que calcule la población de una especie en un determinado número de años. Utiliza la fórmula
 
<br> donde <a href="https://www.codecogs.com/eqnedit.php?latex=N_{i}e^{r&plus;t}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?N_{i}e^{r&plus;t}" title="N_{i}e^{r+t}" /></a> es la población inicial
<br>r es la tasa de crecimiento, la cual siempre es un número entre 0 y 1
<br>t es el tiempo en años y
<br>e la constante de Euler

<br><b>Entrada</b>
<br>Tres números recibidos uno en cada renglón, correspondientes a: población inicial (entero positivo), tiempo en años (entero positivo) y tasa de crecimiento (flotante entre 0 y 1), en ese orden.
<br><b>Salida</b>
<br>Un número entero, resultado del cálculo de la población final. IMPORTANTE: Trunca los decimales del número resultante, para que el resultado sea entero (¿Cuál es la función de la librería math de Python que te puede ayudar a truncar los decimales?).
<br>Ejemplo de ejecución del programa:
<br>>>> 100  
<br>>>> 1
<br>>>> 0.5
<br>164


**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
