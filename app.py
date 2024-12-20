import os
from flask import Flask, render_template
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# MongoDB connection
mongo_uri = os.getenv('MONGO_URI', 'mongodb://db:27017/azure-pricing')
client = MongoClient(mongo_uri)
db = client.get_database()
prices_collection = db['prices']

@app.route('/')
def index():
    try:
        # Fetch only required fields from MongoDB
        prices = list(prices_collection.find({}, {'_id': 0, 'productName': 1, 'location': 1, 'currencyCode': 1, 'unitPrice': 1}))
        year = datetime.now().year
        return render_template('index.html', prices=prices, year=year)
    except Exception as e:
        return f"Error retrieving data: {e}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
