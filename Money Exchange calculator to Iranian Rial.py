from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QCheckBox
import requests
import re
class CurrencyConverter(QWidget):

  def __init__(self):
    super().__init__()
    self.init_ui()

  def init_ui(self):
    self.setWindowTitle("Currency Converter")

    # Define options dictionary
    self.options = {
        "D": "https://www.tgju.org/profile/price_dollar_rl",
        "C": "https://www.tgju.org/profile/price_cad",
        "E": "https://www.tgju.org/profile/price_eur",
    }

    # Layout
    self.layout = QVBoxLayout()
    self.setLayout(self.layout)

    # Currency selection
    self.currency_label = QLabel("Select Currency:")
    self.layout.addWidget(self.currency_label)
    self.currency_combo = QComboBox(self)
    self.currency_combo.addItems(self.options.keys())
    self.layout.addWidget(self.currency_combo)

    # Amount input
    self.amount_label = QLabel("Amount:")
    self.layout.addWidget(self.amount_label)
    self.amount_input = QLineEdit(self)
    self.layout.addWidget(self.amount_input)

    # Rial conversion checkbox
    self.rial_checkbox = QCheckBox("Convert to Rial?")
    self.layout.addWidget(self.rial_checkbox)

    # Convert button
    self.convert_button = QPushButton("Convert")
    self.convert_button.clicked.connect(self.convert_currency)
    self.layout.addWidget(self.convert_button)

    # Result label
    self.result_label = QLabel("")
    self.layout.addWidget(self.result_label)

    self.show()

  def convert_currency(self):
    # Get selected currency
    selected_currency = self.currency_combo.currentText()
    address = self.options[selected_currency]

    # Get amount and conversion type
    amount = float(self.amount_input.text())
    convert_to_rial = self.rial_checkbox.isChecked()

    # Fetch exchange rate (replace with actual logic)
    # Change_Rate = ... (logic to get rate from the URL)
    r = requests.get(address)
    html = r.text
    data_attribute = "info.last_trade.PDrCotVal"
    pattern = r'<span data-col="' + data_attribute + '">(\d+,\d+)</span>'
    number = re.findall(pattern, html)
    Change_Rate = float(number[0].replace(",", "")) / 10
    # Convert currency
    def gheymat(x, y):
      if y:
        rial = x * Change_Rate
        return int(rial)
      else:
        return x / Change_Rate
    result = gheymat(amount, convert_to_rial)

    # Update result label
    self.result_label.setText(f"Converted amount: {result:.2f}")

# Create application and window
app = QApplication([])
window = CurrencyConverter()
app.exec_()