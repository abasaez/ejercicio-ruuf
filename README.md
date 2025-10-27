# Tarea Dev Junior - Ruuf

## 🎯 Objetivo

El objetivo de este ejercicio es poder entender tus habilidades como programador/a, la forma en que planteas un problema, cómo los resuelves y finalmente cómo comunicas tu forma de razonar y resultados.

## 🛠️ Problema

El problema a resolver consiste en encontrar la máxima cantidad de rectángulos de dimensiones "a" y "b" (paneles solares) que caben dentro de un rectángulo de dimensiones "x" e "y" (techo).

## 🚀 Cómo Empezar

### Opción 1: Solución en TypeScript
```bash
cd typescript
npm install
npm start
```

### Opción 2: Solución en Python
```bash
cd python
python3 main.py
```

## ✅ Casos de Prueba

Tu solución debe pasar los siguientes casos de prueba:
- Paneles 1x2 y techo 2x4 ⇒ Caben 4
- Paneles 1x2 y techo 3x5 ⇒ Caben 7
- Paneles 2x2 y techo 1x10 ⇒ Caben 0

---

## 📝 Tu Solución

https://youtu.be/tCFEfc9E-Yg

Para mi solución, se colocan paneles contiguos en una orientación, calculando el espacio sobrante (remainder_width y remainder_height) y llenándolo con paneles rotados si es posible. Se lleva un contador de paneles (placed_panels) que almacena la cantidad colocada. En una segunda iteración, se rota la orientación de los paneles 90° para probar si se pueden colocar más.

Se elige la mejor respuesta entre ambas iteraciones y se retorna.

---

## 💰 Bonus (Opcional)

Si completaste alguno de los ejercicios bonus, explica tu solución aquí:

### Bonus Implementado
Bonus 1: Techo Triangular



### Explicación del Bonus
Para el bonus, se separa el techo triangular en una serie de rectángulos. Su altura se determina usando las medidas de los paneles, y su anchura se calcula usando propiedades geométricas de los triángulos.

A los rectángulos generados, se les aplica la función discutida anteriormente, y sumando los paneles colocados en cada piso, obtenemos los paneles totales que caben en el techo triangular.

Se hacen dos iteraciones, usando como altura de los rectángulos el ancho y el largo de los paneles, y se elige la mejor respuesta entre ambas.



---

## 🤔 Supuestos y Decisiones

El supuesto más importante fue que los paneles solo se podían colocar en su configuración inicial o rotados 90°, lo que simplifica mucho la solución.

Se optó por un algoritmo greedy, que en cada paso maximiza el número de paneles colocados en bloques de una sola orientación. Existen algoritmos más complejos que revisan permutaciones posibles, alternando orientaciones y dejando espacios vacíos, pero son mucho más costosos en tiempo de desarrollo y ejecución. Esta solución ofrece una buena aproximación, suficiente para la mayoría de los casos.