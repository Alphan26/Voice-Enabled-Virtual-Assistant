from twilio.rest import Client

twilio_phone_number = "+17622635102"
account_sid = "AC23b549490fab18878d60c4174013c3ac"
auth_token = "5a2254a68582c4d2e26f47b36f4f9c37"

client = Client(account_sid, auth_token)
call = client.calls.create(
  record = True,
  url="http://demo.twilio.com/docs/voice.xml",
  to="+905336977868",
  from_="+17622635102"
)
# record true diyor okey de bana konuşma bittikten sonra değil konuşma esnasında kayıt edip cevap verebilceğim bir sisteme ihtiyacım var.

print(call.sid)

# herhangi bir numarayı aramak için ödemeli hizmet yaplımasına ihtiyaç var, 15.50 $ free trial veriyo
