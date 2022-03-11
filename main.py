
from flask import Flask, jsonify , redirect, render_template, request, session , url_for
import razorpay
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)
@app.route('/' , methods = ["GET" , "POST"] )
def home_page():
    if request.method == "POST":
        email = request.form["email"]
        name = request.form["name"]
        amount = request.form["amount"]
        order_amount = int(amount) * 100
        print(amount , " " , order_amount)
        data = {
            "amount" : order_amount , 
            "currency" : "INR",
            "payment_capture": "1"  
        }
        client = razorpay.Client(auth=("rzp_test_0wq6o3RvcfIKFu", "y3lPsnj1z6VmxsInjkkcqWzG"))
        create_order = client.order.create(data)
        print(name)

        session["name"] = name
        session["email"] = email
        session["amount"] = order_amount
        session["data"] = data
        session["create_order"] = create_order
        return redirect(url_for('check_out'))
    return render_template("homepage.html")

@app.route("/checkout" ,  methods = ["GET" , "POST"])
def check_out():
    print(session)
    return render_template("checkout.html"  )


@app.route("/success" ,  methods = ["GET" , "POST"])
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(port=5025 , debug=True )