import africastalking

africastalking.initialize(username="sandbox", api_key="cee5d955b0bd1d33a5ebbe2519f6ac1fe2bf43907924436b6f9b4f47ef9e86fe")

airtime = africastalking.Airtime

try:
    response = airtime.send("+254727545805","200","KES")
    print(response)
except Exception as e:
    print(f"Houston we have problem: {e}")
    