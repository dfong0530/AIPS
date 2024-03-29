from ebay_rest import API, Error
import datetime

application = {
    "app_id": "placeholder-placeholder-PRD-placeholder-placeholder",
    "cert_id": "PRD-placeholder-placeholder-placeholder-placeholder-placeholder",
    "dev_id": "placeholder-placeholder-placeholder-placeholder-placeholder",
    "redirect_uri": "placeholder-placeholder-placeholder-placeholder"
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

def refresh_authentication(api):
    now = datetime.datetime.now()
    token_expiry = datetime.datetime.strptime(user['refresh_token_expiry'], "%Y-%m-%d %H:%M:%S")
    
    if now >= token_expiry:
        try:
            new_access_token, new_expiry = api.refresh_access_token(user['refresh_token'])
            
            user['access_token'] = new_access_token
            user['refresh_token_expiry'] = new_expiry
            
            print("Authentication token refreshed successfully.")
        except Exception as e:
            print(f"Failed to refresh authentication token: {e}")
    else:
        print("Authentication token does not need to be refreshed yet.")

def main():
    try:
        api = API(application=application, user=user, header=header)
    except Error as error:
        print(f'Initialization Error {error.number}: {error.reason} - {error.detail}.')
        return
    
    refresh_authentication(api)

    # TEST CASE #1
    
    try:
        print("The five least expensive iPhone listings on eBay:")
        results = api.buy_browse_search(q='iPhone', sort='price', limit=5)
        for record in results:
            if 'record' not in record:
                continue
            else:
                item = record['record']
                print(f"Item ID: {item['item_id']}, URL: {item['item_web_url']}")
    except Error as error:
        print(f'Search Error {error.number}: {error.reason} - {error.detail}.')
    except Exception as e:
        print(f'An unexpected error occurred: {str(e)}')

if __name__ == "__main__":
    main()
