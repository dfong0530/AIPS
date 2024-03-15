import requests
import json

# eBay endpoint for creating a listing
url = "https://api.ebay.com/sell/inventory/v1/inventory_item"

# ADD YOUR TOKENS AND AUTH
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer",
}

item_data = {
    "sku": "sku-123",
    "offer": {
        "categoryId": "12345",
        "format": "FIXED_PRICE", 
        "listingDescription": "test",
        "marketplaceId": "EBAY_US", 
        "price": {
            "currency": "USD",
            "value": "25000.00"
        },
        "quantityLimitPerBuyer": 1
    },
    "product": {
        "title": "BLAH BLAH Item",
        "description": "VERY BLAH BLAH",
        "imageUrls": ["http://example.com/image1.jpg", "http://example.com/image2.jpg"],
    }
}

# POST IT!!!!!!!!!!!!
response = requests.post(url, headers=headers, data=json.dumps(item_data))

if response.ok:
    print("Listing created successfully.")
else:
    print(f"Failed to create listing. Response code: {response.status_code}, Detail: {response.text}")
