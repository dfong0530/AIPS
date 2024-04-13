from ebay_rest import API, Error
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


application = {
    "app_id": os.getenv('CLIENT_ID'),
    "cert_id": os.getenv('CLIENT_SECRET'),
    "dev_id": os.getenv('DEV_ID'),
    "redirect_uri": "https://google.com/"
}

user = {
    "email_or_username": "<production-username>",
    "password": "<production-user-password>",
    "scopes": [
        "https://api.ebay.com/oauth/api_scope",
        "https://api.ebay.com/oauth/api_scope/sell.inventory",

        "https://api.ebay.com/oauth/api_scope/sell.marketing",
        "https://api.ebay.com/oauth/api_scope/sell.account",
        "https://api.ebay.com/oauth/api_scope/sell.fulfillment"
    ],
    "refresh_token": "production-refresh_token",
    "refresh_token_expiry": "production-token_expiry"
}

header = {
    "accept_language": "en-US",
    "affiliate_campaign_id": "",
    "affiliate_reference_id": "",
    "content_language": "en-US",
    "country": "US",
    "currency": "USD",
    "device_id": "",
    "marketplace_id": "EBAY_US",
    "zip": "20500"
}


def get_my_listings(api, limit=10, offset=0):

    try:

        response = api.sell.inventory.getInventoryItems(limit=limit, offset=offset)
        listings = []
        
        if 'inventoryItems' in response:
            for item in response['inventoryItems']:
                listings.append({
                    'sku': item['sku'],
                    'offerId': item['offerId'],
                    'title': item['title'],
                    'price': item['price'],
                    'quantity': item['quantity'],
                    'status': item['status']
                })
        return listings
    except Error as e:
        return f"Failed to fetch own listings: {e.detail}"



def get_current_listings(api, search_query, sort_order='price', limit=5):
    try:
        search_results = api.buy.browse_search(q=search_query, sort=sort_order, limit=limit)
        listings = []
        for record in search_results:
            if 'item' in record:
                item = record['item']
                listings.append({
                    'item_id': item['itemId'],
                    'title': item['title'],
                    'price': item.get('price', {}).get('value', 'N/A'),
                    'currency': item.get('price', {}).get('currency', 'N/A'),
                    'item_url': item['itemWebUrl']
                })
        return listings
    except Error as e:
        return f"Failed to fetch current listings: {e.detail}"

def main():
    try:
        api = API(application=application, user=user, header=header)
        listings = get_current_listings(api, 'iPhone')
        if isinstance(listings, str): 
            print(listings)
        else:
            print("The five least expensive iPhone listings on eBay:")
            for listing in listings:
                print(f"Item ID: {listing['item_id']}, Title: {listing['title']}, Price: {listing['price']} {listing['currency']}, URL: {listing['item_url']}")
    except Error as error:
        print(f'Error: {error.number} - {error.reason} - {error.detail}.\n')

if __name__ == "__main__":
    main()
