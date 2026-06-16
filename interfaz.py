import tkinter as tk
from tkinter import ttk
import pyperclip

from generador import generar_contraseña, evaluar_contraseña


def construir_ventana():
    root = tk.Tk()
    root.title("Generador de Contraseñas Seguras")
    root.resizable(False, False)

    # estilos de colores para la barra segun el nivel ===========
    estilo = ttk.Style()
    estilo.configure("debil.Horizontal.TProgressbar", background="red")
    estilo.configure("media.Horizontal.TProgressbar", background="orange")
    estilo.configure("fuerte.Horizontal.TProgressbar", background="yellow")
    estilo.configure("muyFuerte.Horizontal.TProgressbar", background="green")

    longitud_var = tk.IntVar(value=16)

    def actualizar_longitud(valor):
        longitud_var.set(round(float(valor)))

    ttk.Scale(root, from_=8, to=64, variable=longitud_var,
          orient="horizontal", command=actualizar_longitud).pack()

    tk.Label(root, textvariable=longitud_var).pack()

    mayusculas_var = tk.BooleanVar(value=True)
    numeros_var = tk.BooleanVar(value=True)
    simbolos_var = tk.BooleanVar(value=True)

    tk.Checkbutton(root, text="Mayúsculas", variable=mayusculas_var).pack()
    tk.Checkbutton(root, text="Números", variable=numeros_var).pack()
    tk.Checkbutton(root, text="Símbolos", variable=simbolos_var).pack()

    contraseña_var = tk.StringVar()

    tk.Entry(root, textvariable=contraseña_var,
             state="readonly", width=30).pack()

    def generar():
        contraseña_var.set(generar_contraseña(
            longitud_var.get(),
            mayusculas_var.get(),
            numeros_var.get(),
            simbolos_var.get()
        ))

    tk.Button(root, text="Generar", command=generar).pack()

    # label de confirmacion al copiar ======================
    copiado_var = tk.StringVar(value="")
    tk.Label(root, textvariable=copiado_var, fg="green").pack()

    def copiar():
        contraseña = contraseña_var.get()
        if contraseña:
            pyperclip.copy(contraseña)
            copiado_var.set("Copiado")
            root.after(2000, lambda: copiado_var.set(""))

    tk.Button(root, text="Copiar", command=copiar).pack()

    # verificar contraseña ===================================
    tk.Label(root, text="Verificar contraseña:").pack()

    verificar_var = tk.StringVar()
    tk.Entry(root, textvariable=verificar_var, width=30).pack()

    barra = ttk.Progressbar(root, maximum=100, orient="horizontal", length=200)
    barra.pack()

    nivel_var = tk.StringVar(value="")
    tk.Label(root, textvariable=nivel_var).pack()

    razones_var = tk.StringVar(value="")
    tk.Label(root, textvariable=razones_var, wraplength=250, justify="left").pack()

    def actualizar_verificador(*args):
        texto = verificar_var.get()
        if not texto:
            barra["value"] = 0
            barra["style"] = ""
            nivel_var.set("")
            razones_var.set("")
            return

        resultado = evaluar_contraseña(texto)
        barra["value"] = resultado["puntuacion"]

        # cambia el color de la barra segun el nivel ============================
        colores = {
            "Débil": "debil.Horizontal.TProgressbar",
            "Media": "media.Horizontal.TProgressbar",
            "Fuerte": "fuerte.Horizontal.TProgressbar",
            "Muy fuerte": "muyFuerte.Horizontal.TProgressbar",
        }
        barra["style"] = colores[resultado["nivel"]]

        nivel_var.set(f"Nivel: {resultado['nivel']} ({resultado['puntuacion']}/100)")

        if resultado["razones"]:
            razones_var.set("\n".join(resultado["razones"]))
        else:
            razones_var.set("Contraseña segura")

    verificar_var.trace_add("write", actualizar_verificador)

    root.mainloop()


if __name__ == "__main__":
    construir_ventana()
