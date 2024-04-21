import os
from typing import Final
from vonage import Client, Sms
from dotenv import load_dotenv

load_dotenv()

SECRET: Final[str] = os.getenv('SMS_SECRET')
SMS_KEY: Final[str] = os.getenv('SMS_KEY')
FROM_USER: Final[str] = "sms test"
TO_USER: Final[str] = "972528512751"

def main() -> None:
    client: Client = Client(key=SMS_KEY, secret=SECRET)
    sms: Sms = Sms(client)

    with open('message.txt', 'r', encoding='utf-8') as f:
        text: str = f.read()

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

if __name__ == "__main__":
    main()