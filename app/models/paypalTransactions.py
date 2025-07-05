import requests
from config import Config

def get_access_token():
    response = requests.post(
        f"{Config.PAYPAL_API_BASE}/v1/oauth2/token",
        data={"grant_type": "client_credentials"},
        auth=(Config.PAYPAL_CLIENT_ID, Config.PAYPAL_CLIENT_SECRET)
    )
    return response.json().get("access_token")

def create_order(amount, currency="USD"):
    access_token = get_access_token()
    payload = {
        "intent": "CAPTURE",
        "purchase_units": [{
            "amount": {
                "currency_code": currency,
                "value": amount
            }
        }]
    }
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(f"{Config.PAYPAL_API_BASE}/v2/checkout/orders", json=payload, headers=headers)
    return response.json(), response.status_code

def capture_order(order_id):
    access_token = get_access_token()
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(f"{Config.PAYPAL_API_BASE}/v2/checkout/orders/{order_id}/capture", headers=headers)
    return response.json(), response.status_code
