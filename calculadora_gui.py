import tkinter as tk

class CalculadoraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")

        # Variable para almacenar la expresión y mostrarla en pantalla
        self.expresion = ""

        # Frame para la pantalla
        self.frame_pantalla = tk.Frame(self.root, width=300, height=50)
        self.frame_pantalla.pack_propagate(False)
        self.frame_pantalla.pack(padx=10, pady=10)

        self.label_pantalla = tk.Label(self.frame_pantalla, text=self.expresion, anchor="e", font=("Arial", 20), bg="white", bd=5)
        self.label_pantalla.pack(fill=tk.BOTH, expand=True)

        # Frame para los botones
        self.frame_botones = tk.Frame(self.root)
        self.frame_botones.pack(padx=10, pady=10)

        # Botones de dígitos y operadores
        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (texto, fila, columna) in botones:
            tk.Button(self.frame_botones, text=texto, width=10, height=3, command=lambda t=texto: self.click_boton(t)).grid(row=fila, column=columna, padx=5, pady=5)

    def click_boton(self, valor):
        if valor == '=':
            try:
                resultado = str(eval(self.expresion))
                self.expresion = resultado
            except:
                self.expresion = "Error"
        else:
            self.expresion += valor
        
        self.actualizar_pantalla()

    def actualizar_pantalla(self):
        self.label_pantalla.config(text=self.expresion)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()
