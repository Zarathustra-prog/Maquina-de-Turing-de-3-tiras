# Máquina de Turing de 3 Cintas en Python

## Descripción

Este proyecto implementa una **Máquina de Turing de tres cintas** en Python. La clase `ThreeTapeTM` permite simular cualquier máquina de Turing que utilice tres cintas, configurando estados, transiciones y movimientos.  

El archivo incluye una **máquina base** de ejemplo que recorre una cinta hasta encontrar un símbolo `#` y luego termina en un estado de aceptación. Esta máquina sirve como punto de partida para implementar operaciones más complejas, como suma o multiplicación de números binarios.

---

## Contenido

- `ThreeTapeTM` – Clase principal que implementa la máquina de Turing de tres cintas.
- `config_example` – Configuración de la máquina.
- `tape_1` – Entrada de la máquina.
- `tm.run()` – Método para ejecutar la máquina.
- `final_tapes` – Estado final de las cintas tras la ejecución.

---

## Cómo funciona

1. **Inicialización:** La máquina empieza en el estado `init` y coloca la cinta de entrada en la cinta 1. Las cintas 2 y 3 comienzan en blanco (`_`).  
2. **Paso de transición:** En cada paso, la máquina lee el símbolo bajo cada cabeza de cinta, busca la transición correspondiente en `delta` y aplica los cambios:  
   - Escribe nuevos símbolos  
   - Mueve las cabezas (`>`, `<`, `-`)  
   - Cambia de estado  
3. **Aceptación:** La ejecución termina si la máquina llega a un estado de aceptación o si se excede `max_steps`.  

---

## Configuración de la máquina (`config`)

El diccionario `config` tiene tres claves:

- `init`: Estado inicial (string)  
- `accept`: Lista de estados de aceptación  
- `delta`: Diccionario que define las transiciones  

Cada transición se define como: 

```python
(current_state, symbol_tape1, symbol_tape2, symbol_tape3) : 
(new_state, [write_tape1, write_tape2, write_tape3], [move_tape1, move_tape2, move_tape3])
```

## Aplicaciones: operaciones con números binarios

La máquina base puede extenderse para realizar operaciones con binarios, usando las tres cintas de la siguiente forma:

```python

| Operación      | Cinta 1                               | Cinta 2                 | Cinta 3         |
| -------------- | --------------------------------------| ----------------------- | --------------- |
| Suma         | Número A + `#` + Número B               | Auxiliar                | Resultado       |
| Multiplicación | Número A + `#` + Número B / Resultado | Auxiliar                | Auxiliar        |
```
