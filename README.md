# Currency Converter

This Python application creates a user-friendly interface for converting currencies. Users can select a currency from a dropdown menu, enter an amount, and choose whether to convert to Rial. The application fetches the exchange rate from a specified website and displays the converted amount.

## Features

- Convert between multiple currencies
- Convert to Rial (optional)
- User-friendly PyQt5 GUI

![Currency Converter GUI](https://mega.nz/file/14IkQDiJ#MGuAtoVpnul0wxWrCm6DKStBqNHWDuNZrKbhIbK4mog)

## Requirements

- Python 3
- PyQt5
- requests

## Installation

1. Clone this repository.
2. Install the required libraries:

    ```bash
    pip install PyQt5 requests
    ```

## Running the Application

1. Open a terminal in the project directory.
2. Run the following command:

    ```bash
    python currency_converter.py
    ```

## Explanation

The code for this application is in the `currency_converter.py` file. It uses the PyQt5 library to create the graphical user interface (GUI). The GUI consists of a dropdown menu for selecting the currency, a text box for entering the amount, a checkbox for converting to Rial, and a button for converting the currency.

When the user selects a currency and enters an amount, the application fetches the exchange rate from a website using the `requests` library. The application then converts the amount to the selected currency (or Rial, if checked) and displays the converted amount in the result label.

## How to Contribute

1. Fork the repository.
2. Make changes to the code.
3. Create a pull request.

## License

This project is licensed under the MIT License.

---

**Note:** The current implementation uses a placeholder function `gheymat` for currency conversion. You'll need to replace it with your actual logic that considers the fetched exchange rate and the `convert_to_rial` checkbox state.

This README file provides a clear overview of your application, its features, requirements, installation instructions, explanation of functionality, contribution guidelines, and a licensing statement.
