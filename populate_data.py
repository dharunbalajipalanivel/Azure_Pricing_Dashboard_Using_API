import os
import requests
from pymongo import MongoClient

# MongoDB connection
mongo_uri = os.getenv('MONGO_URI', 'mongodb://db:27017/azure-pricing')
client = MongoClient(mongo_uri)
db = client.get_database()
prices_collection = db['prices']

# Azure API endpoint
azure_api_url = "https://prices.azure.com/api/retail/prices?api-version=2023-01-01-preview"

def fetch_azure_data():
    response = requests.get(azure_api_url)
    data = response.json()

    if 'Items' in data:
        for item in data['Items']:
            # Insert or update data in MongoDB
            prices_collection.update_one(
                {"skuId": item["skuId"]},
                {"$set": item},
                upsert=True
            )
    print(f"Fetched {len(data['Items'])} items from Azure API.")

if __name__ == "__main__":
    fetch_azure_data()
