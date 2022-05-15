

import smtplib
from email.mime.text import MIMEText
from algo import encrypt_msg
#baseURL = 'https://api.thingspeak.com/update?api_key=09SMNBK4PFBB12A3&field3='
message = input("Enter message to send: ").strip()
encrypted_msg = encrypt_msg(message)
msg = MIMEText(encrypted_msg)
print("Message:\n", encrypted_msg)

print("----------------------------")
print("\nMessage sent ... ", u'\u2713')

