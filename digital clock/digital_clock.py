import time
from datetime import datetime
import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%A, %B %d, %Y")

    print("=" * 40)
    print(" " * 10 + "🕒 DIGITAL CLOCK")
    print("=" * 40)
    print(f"Time: {current_time}")
    print(f"Date: {current_date}")
    print("=" * 40)

    time.sleep(1)