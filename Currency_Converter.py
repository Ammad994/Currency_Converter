# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk, messagebox

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        self.base_currency = "USD"  # Default base currency
        self.target_currency = "EUR"  # Default target currency
        self.amount = tk.DoubleVar()  # Variable to store the amount to be converted

        # Local dictionary to mimic the exchange rate API data
        self.exchange_rates = {
            "USD": {"EUR": 0.85, "GBP": 0.72, "JPY": 109.33},
            "EUR": {"USD": 1.18, "GBP": 0.85, "JPY": 128.53},
            "GBP": {"USD": 1.39, "EUR": 1.18, "JPY": 151.30},
            "JPY": {"USD": 0.0092, "EUR": 0.0078, "GBP": 0.0066}
        }

        # List to store the conversion history
        self.conversion_history = []

        # Create widgets for the GUI
        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.pack(pady=5)

        self.amount_entry = tk.Entry(root, textvariable=self.amount, font=("Arial", 14))
        self.amount_entry.pack(pady=5)

        self.from_currency_label = tk.Label(root, text="From Currency:")
        self.from_currency_label.pack(pady=5)

        # Create a dropdown menu for selecting the base currency
        self.from_currency_combobox = ttk.Combobox(root, values=list(self.exchange_rates.keys()), font=("Arial", 14))
        self.from_currency_combobox.set(self.base_currency)
        self.from_currency_combobox.pack(pady=5)

        self.to_currency_label = tk.Label(root, text="To Currency:")
        self.to_currency_label.pack(pady=5)

        # Create a dropdown menu for selecting the target currency
        self.to_currency_combobox = ttk.Combobox(root, values=list(self.exchange_rates.keys()), font=("Arial", 14))
        self.to_currency_combobox.set(self.target_currency)
        self.to_currency_combobox.pack(pady=5)

        self.convert_button = tk.Button(root, text="Convert", command=self.convert)
        self.convert_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 16, "bold"))
        self.result_label.pack(pady=10)

    def convert(self):
        amount = self.amount.get()
        from_currency = self.from_currency_combobox.get().upper()
        to_currency = self.to_currency_combobox.get().upper()

        if from_currency == "" or to_currency == "":
            self.result_label.config(text="Please enter both currencies.")
            return

        if from_currency == to_currency:
            self.result_label.config(text="Both currencies are the same.")
            return

        # Check if exchange rate data is available locally
        if from_currency in self.exchange_rates and to_currency in self.exchange_rates[from_currency]:
            rate = self.exchange_rates[from_currency][to_currency]
            converted_amount = amount * rate
            self.result_label.config(text=f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
            self.save_conversion_to_history(from_currency, to_currency, amount, converted_amount)
        else:
            self.result_label.config(text="Currency not found.")

    def save_conversion_to_history(self, from_currency, to_currency, amount, converted_amount):
        # Save the conversion history to the list
        conversion_data = {
            "from_currency": from_currency,
            "to_currency": to_currency,
            "amount": amount,
            "converted_amount": converted_amount
        }

        self.conversion_history.append(conversion_data)

def main():
    root = tk.Tk()
    currency_converter = CurrencyConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
