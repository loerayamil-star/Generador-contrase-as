# Generador de Contraseñas Seguras

Aplicación de escritorio en Python para generar y verificar contraseñas seguras, con interfaz gráfica construida con Tkinter.

## Funcionalidades

- **Generador de contraseñas**: crea contraseñas aleatorias con control sobre longitud, uso de mayúsculas, números y símbolos.
- **Verificador de fortaleza**: analiza cualquier contraseña y la clasifica en niveles: *Débil*, *Media*, *Fuerte* o *Muy fuerte*, con una barra visual de progreso.
- **Retroalimentación**: indica por qué una contraseña es débil (longitud insuficiente, falta de variedad de caracteres, etc.).
- **Copiar al portapapeles**: botón para copiar la contraseña generada con un clic.

## Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python 3 | Lenguaje base |
| Tkinter | Interfaz gráfica |
| `secrets` | Generación criptográficamente segura |
| `re` (regex) | Análisis de patrones en la contraseña |
| `pyperclip` | Copiar al portapapeles |

## Requisitos

Python 3.6 o superior y la librería externa `pyperclip`:

```bash
pip install pyperclip
```

## Cómo ejecutar

```bash
python interfaz.py
```

## Por qué `secrets` y no `random`

El módulo `random` de Python está diseñado para simulaciones y juegos, **no para seguridad**. Utiliza un generador pseudoaleatorio que puede ser predecible si se conoce la semilla.

El módulo `secrets` usa fuentes de entropía del sistema operativo (como `/dev/urandom` en Linux/macOS) para producir valores verdaderamente impredecibles. Esto es fundamental para contraseñas: si un atacante pudiera predecir la secuencia de números aleatorios, podría reproducir la contraseña generada.

**Regla práctica**: siempre que generes tokens, contraseñas o claves de seguridad, usa `secrets`.

## Nota educativa

Este proyecto fue desarrollado como ejercicio de aprendizaje, marcando el primer contacto con el módulo `secrets` y las expresiones regulares (`re`) en Python.
