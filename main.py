import os
import vonage
from dotenv import load_dotenv

load_dotenv()

SECRET = os.getenv('SMS_SECRET')
SMS_KEY = os.getenv('SMS_KEY')

FROM_USER = "sms test"
TO_USER = "972500000000"

client = vonage.Client(key=SMS_KEY, secret=SECRET)
sms = vonage.Sms(client)

with open('message.txt', 'r', encoding='utf-8') as f:
    text = f.read()

responseData = sms.send_message(
    {
        "from": FROM_USER,
        "to": TO_USER,
        "text": text,
        'type':'unicode'
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")