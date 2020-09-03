import africastalking

africastalking.initialize(username="sandbox", api_key="cee5d955b0bd1d33a5ebbe2519f6ac1fe2bf43907924436b6f9b4f47ef9e86fe")

payment = africastalking.Payment

try:
    response = payment.mobile_checkout("DUKA","+254727545805","KES","200")
    print(response)
except Exception as e:
    print(f"Houston we have problem: {e}")
    