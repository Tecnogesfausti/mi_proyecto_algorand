import tkinter as tk
from tkinter import ttk
from core.algorand import AlgorandClient

class WalletApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Algorand Wallet (IES FaustiCoin)")
        self.client = AlgorandClient()

        # Etiqueta
        tk.Label(root, text="Elige una dirección Algorand").pack(pady=5)

        # Lista de direcciones (puedes leerlas desde un archivo)
        self.direcciones = [
            "34WES245TO2OGRXVXLD2OA7RLXMES4JZ5V6XL5DYJI27NV2272YNFANCOY",
            "DIRECCION2XXXXXXXXXXXXXXXXXXXX",
            "DIRECCION3XXXXXXXXXXXXXXXXXXXX"
        ]

        # Combobox
        self.address_var = tk.StringVar()
        self.combo = ttk.Combobox(root, textvariable=self.address_var, values=self.direcciones, state="readonly", width=60)
        self.combo.pack(pady=5)
        self.combo.bind("<<ComboboxSelected>>", self.on_select)

        # Botón
        tk.Button(root, text="Consultar saldo", command=self.check).pack(pady=10)

        # Resultado
        self.result = tk.StringVar()
        tk.Label(root, textvariable=self.result).pack()

    def on_select(self, event):
        # Este método se llama al elegir una dirección
        seleccion = self.combo.get()
        self.result.set(f"Dirección seleccionada: {seleccion}")

    def check(self):
        direccion = self.address_var.get()
        if not direccion:
            self.result.set("Selecciona una dirección primero")
            return
        try:
            balance = self.client.get_balance(direccion)
            self.result.set(f"Saldo: {balance} ALGO")
        except Exception as e:
            self.result.set(f"Error: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = WalletApp(root)
    root.mainloop()

