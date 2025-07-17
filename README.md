# SecureSpend

SecureSpend is a Flask-based web application designed to help users analyze and monitor their financial transactions with a focus on fraud detection and merchant categorization. The app provides an interactive dashboard to view recent transactions, identify potential fraud, and analyze spending patterns by merchant categories.

## Features

- Display recent transactions with details: transaction ID, amount, merchant category, and fraud status.
- Map Merchant Category Codes (MCC) to meaningful business descriptions.
- Fraud detection labeling integrated from a provided dataset.
- Summary analytics including total transactions, fraud rate, and average transaction amount.
- Searchable transactions table with filtering by merchant category.
- Responsive UI styled with Bootstrap for improved user experience.

## Technologies Used

- Python 3.x
- Flask (Web framework)
- Pandas (Data processing)
- HTML, CSS, Bootstrap (Frontend)
- JSON (Data interchange format)

## Dataset

This project uses publicly available transaction data from [Kaggle](https://www.kaggle.com/):

**Dataset Name: [Financial Transactions Dataset"]

You will need to download the dataset separately from Kaggle due to size and licensing restrictions. After downloading, place the following files in the project directory:

- `transactions_data.csv`
- `train_fraud_labels.json`

These files are **not included** in the repository.

For more details on the dataset, please visit the Kaggle page linked above.


## Getting Started

### Prerequisites

- Python 3.6 or later
- `pip` package manager

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Isha2004-coder/SecureSpend.git
   cd SecureSpend
