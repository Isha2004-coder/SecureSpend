from flask import Flask, render_template
import pandas as pd
import json

app = Flask(__name__)

# Load and preprocess data at startup
transactions = pd.read_csv('transactions_data.csv')
print("Sample merchant_ids BEFORE processing:")
print(transactions['merchant_id'].head(10))

with open('train_fraud_labels.json', 'r') as f:
    fraud_labels = json.load(f)
fraud_df = pd.DataFrame(list(fraud_labels.items()), columns=['id', 'is_fraud'])

# Convert 'id' columns to string and strip whitespace for merging
transactions['id'] = transactions['id'].astype(str).str.strip()
fraud_df['id'] = fraud_df['id'].astype(str).str.strip()

# Merge fraud info into transactions
transactions = transactions.merge(fraud_df, on='id', how='left')
transactions['is_fraud'] = transactions['is_fraud'].fillna(False)

# Load MCC codes JSON
with open('mcc_codes.json', 'r') as f:
    mcc_codes = json.load(f)

# Map MCC codes to merchant categories
transactions['mcc'] = transactions['mcc'].astype(str)
transactions['merchant_category'] = transactions['mcc'].map(mcc_codes).fillna('Unknown Merchant')

print(transactions[['mcc', 'merchant_category']].head(10))

# Select top 10 transactions for display
transactions_to_show = transactions[['id', 'amount', 'merchant_category', 'is_fraud']].head(10)

# Calculate analytics summary
total_transactions = len(transactions)
total_fraud = transactions['is_fraud'].sum()
fraud_rate = (total_fraud / total_transactions) * 100 if total_transactions > 0 else 0
average_amount = transactions['amount'].mean()

analytics = {
    "total_transactions": total_transactions,
    "total_fraud": total_fraud,
    "fraud_rate": f"{fraud_rate:.2f}%",
    "average_amount": f"${average_amount:.2f}",
}

@app.route('/')
def home():
    transactions_list = transactions_to_show.to_dict(orient='records')
    return render_template('index.html', transactions=transactions_list, analytics=analytics)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

