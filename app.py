from flask import Flask, request, render_template
import africastalking

app = Flask(__name__)

username = "sandbox"
api_key = "cee5d955b0bd1d33a5ebbe2519f6ac1fe2bf43907924436b6f9b4f47ef9e86fe"

africastalking.initialize(username, api_key)

airtime = africastalking.Airtime

#recieve and send the SMS on the AT API

@app.route("/sms-sending", methods=["GET","POST"])
def sms_sending(): 
    
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        amount = "200"
        phone_number = request.form["phoneNumber"]
        currency_code = "KES"

        try:
            response = airtime.send(phone_number, amount, currency_code)
            print(response)
            return render_template("success.html")
        except Exception as e:
            print(f"Houston we have a problem {e}")
            return render_template("error.html")



#notify user on dashboard whether the SMS was sent or not

@app.route("/sending-notification", methods=["GET","POST"])
def sms_notification():
    pass


if __name__ == "__main__":
    app.run(debug=True)