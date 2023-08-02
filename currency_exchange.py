import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates

def convert_currency(amount_entry, converted_label):
    amount = float(amount_entry.get())

    currency_rates = CurrencyRates()
    converted_amount = currency_rates.convert("USD", "INR", amount)
    converted_label.config(text=f"Converted Amount: ₹ {converted_amount:.2f}")

def main():
    root = tk.Tk()
    root.title("Currency Converter")
    root.geometry("400x300")

    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 12))
    style.configure("TButton", font=("Arial", 12), background="blue", foreground="Black")

    title_label = ttk.Label(root, text="Currency Converter", font=("Arial", 16, "bold"), padding=(0, 10))
    title_label.pack()

    from_currency_label = ttk.Label(root, text="From Currency: $ USD", style="TLabel")
    from_currency_label.pack(pady=5)

    to_currency_label = ttk.Label(root, text="To Currency: ₹ INR", style="TLabel")
    to_currency_label.pack(pady=5)

    amount_label = ttk.Label(root, text="Amount:", style="TLabel")
    amount_label.pack(pady=5)

    amount_entry = ttk.Entry(root, font=("Arial", 12), width=40)
    amount_entry.pack(pady=5)

    convert_button = ttk.Button(root, text="Convert", command=lambda: convert_currency(amount_entry, converted_label), style="TButton")
    convert_button.pack(pady=10)

    converted_label = ttk.Label(root, text="", font=("Arial", 12), wraplength=350, justify="center")
    converted_label.pack()

    footer_label = ttk.Label(root, text="Made By Fahad", font=("Arial", 10, "italic"), padding=(0, 10))
    footer_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
