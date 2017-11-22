from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC7d87703f71cd0b56fb3cb90a0e1b6b50"
# Your Auth Token from twilio.com/console
auth_token  = "95ffe9ffa3d105050658682e7c27dcce"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14076940004", 
    from_="+13212412439",
    body="Hello from Python!")

print(message.sid)
