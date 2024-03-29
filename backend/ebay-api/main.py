from ebay_rest import API, DateTime, Error, Reference
import os

from dotenv import load_dotenv

load_dotenv()

application = {
    "app_id": f"{os.getenv('CLIENT_ID')}",
    "cert_id": f"{os.getenv('CLIENT_SECRET')}",
    "dev_id": f"{os.getenv('DEV_ID')}",
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
        "https://api.ebay.com/oauth/api_scope/sell.fulfillment",
        "https://api.ebay.com/oauth/api_scope/sell.inventory",
        ""
    ],
    "refresh_token": "production-refresh_token",
    "refresh_token_expiry": "production-token_expiry"
}

header = {
    "accept_language": "en-US",
    "affiliate_campaign_id": "",
    "affiliate_reference_id": "",
    "content_language": "en-CA",
    "country": "CA",
    "currency": "CAD",
    "device_id": "",
    "marketplace_id": "EBAY_ENCA",
    "zip": ""
}

key_pair = {
    "private_key": "placeholder-placeholder-placeholder-placeholder-placeholder-plac",
    "signing_key_id": "placeholder-placeholder-placeholder-"
}


# def refresh_access_token(credentials):
#     oauth_client = OAuth2(**credentials)
#     new_token = oauth_client.refresh_access_token()
#     return new_token


# def create_inventory_item(api_client, item_data):
#     try:
#         response = api_client.create_inventory_item(item_data)
#         return response
#     except Error as e:
#         print(f"Failed to create inventory item: {e.detail}")
#         return None


# def create_and_publish_offer(api_client, offer_data):
#     try:
#         offer_id = api_client.create_offer(offer_data)
#         publish_response = api_client.publish_offer(offer_id)
#         return publish_response
#     except Error as e:
#         print(f"Failed to create or publish offer: {e.detail}")
#         return None


def main():

    # access_token = refresh_access_token(user_credentials)
    # user_credentials["access_token"] = access_token


    # api_client = Trading(**application, **user_credentials)

    # item_response = create_inventory_item(api_client)
    # if item_response:
    #     print("Inventory item created successfully.")


    # offer_response = create_and_publish_offer(api_client)
    # if offer_response:
    #     print("Offer created and published successfully.")
    try:
        api = API(application=application, user=user, header=header)
    except Error as error:
        print(f'Error {error.number} is {error.reason}  {error.detail}.\n')
    else:
        try:
            print("The five least expensive iPhone things now for sale on-eBay:")        
            for record in api.buy_browse_search(q='iPhone', sort='price', limit=5):
                if 'record' not in record:
                    pass    # TODO Refer to non-records, they contain optimization information.
                else:
                    item = record['record']
                    print(f"item id: {item['item_id']} {item['item_web_url']}")
        except Error as error:
            print(f'Error {error.number} is {error.reason} {error.detail}.\n')
        else:
            pass

if __name__ == "__main__":
    main()
