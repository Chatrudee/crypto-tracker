import requests
import time
import schedule
from prefect import flow, task
from tracker.models import CryptoPrice

@task(retries=2, retry_delay_seconds=5)
def fetch_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    price = response.json()['bitcoin']['usd']
    return price

@task
def save_price_to_db(price):
    CryptoPrice.objects.create(name="Bitcoin", price=price)
    print(f"[{time.strftime('%H:%M:%S')}] Successfully saved Bitcoin price: ${price}")

@flow(name="Crypto Price Tracker")
def crypto_tracker_flow():
    price = fetch_bitcoin_price()
    save_price_to_db(price)

def run_bot():
    print(f"[{time.strftime('%H:%M:%S')}] Bot is waking up...")
    crypto_tracker_flow()

def start():
    print("🚀 Starting Crypto Bot... (Running every 1 minute)")
    run_bot() # รันรอบแรกทันที
    
    schedule.every(1).minutes.do(run_bot) # ตั้งเวลา
    
    while True: # ลูปไม่มีวันจบ
        schedule.run_pending()
        time.sleep(1)
