import requests

class CryptoTracker:
    def __init__(self, api_url='https://api.coingecko.com/api/v3'):
        self.api_url = api_url

    def get_price(self, coin_id='bitcoin', currency='usd'):
        try:
            response = requests.get(f"{self.api_url}/simple/price", params={
                'ids': coin_id,
                'vs_currencies': currency
            })
            data = response.json()
            return data.get(coin_id, {}).get(currency, None)
        except Exception as e:
            print(f"Error fetching price: {e}")
            return None

    def get_market_cap(self, coin_id='bitcoin', currency='usd'):
        try:
            response = requests.get(f"{self.api_url}/coins/{coin_id}")
            data = response.json()
            return data.get('market_data', {}).get('market_cap', {}).get(currency, None)
        except Exception as e:
            print(f"Error fetching market cap: {e}")
            return None
