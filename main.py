import requests
import smtplib

endpoint = 'https://api.kanye.rest'
quotes_container = []

for _ in range(5):
    data = requests.get(endpoint)
    data_jason = data.json()
    kanye_quote = data_jason['quote']
    quotes_container.append(kanye_quote)

with open('kanye_quotes.txt', 'a') as file:
    for quote in quotes_container:
        data = file.write(f'{quote}\n')
        print(quote)

        # Email credentials
        sender_email = 'amadoubah12341@gmail.com'
        receiver_email = 'amadoubah12341@gmail.com'
        password = 'gtvbfcskuodoaibd'


def send_email():
    with open('kanye_quotes.txt', 'r') as file:
        data_content = file.read()
    subject = 'kanye west quotes from the kanye rest api | using python'
    body = f'{data_content}\n'
    message = f'Subject: {subject.title()}\n\n{body}'

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=sender_email, password=password)
            connection.sendmail(from_addr=sender_email, to_addrs=receiver_email, msg=message)
        print(f"Email sent successfully to {receiver_email}")
    except Exception as e:
        print(f"Error: {e}")

send_email()