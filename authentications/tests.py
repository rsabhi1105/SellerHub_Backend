import vonage
client = vonage.Client(key="24684b17", secret="tsjevByQn2T26Jow")
sms = vonage.Sms(client)

responseData = sms.send_message(
    {
        "from": "Vonage APIs",
        "to": "916267732423",
        "text": "A text message sent using th65412242424e Nexmo SMS API",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
