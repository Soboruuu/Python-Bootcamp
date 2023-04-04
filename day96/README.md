# Day 96 - An Online Shop
## Concepts Practised
- Create a Web Server with Flask
- URL Building with Flask
- Flask URL Paths and the Flask Debugger
- Python Decorator Functions and the `@` Syntax
- Stripe API
- Create sample page with Stripe API DOCS (https://stripe.com/docs/checkout/quickstart)
- Go to [http://localhost:4242/checkout.html]
------
- Credit Card Numbers for TEST / Payment succeeds (4242 4242 4242 4242)
- Credit Card Numbers for TEST / Payment requires authentication (4000 0025 0000 3155)
- Credit Card Numbers for TEST / Payment is declined (4000 0000 0000 9995)
-----

## An Online Shop

![success](https://user-images.githubusercontent.com/116648895/229669878-a48457d3-2f72-44ef-8d02-df2f25d8ccba.gif)


# Accept a Payment with Stripe Checkout

Stripe Checkout is the fastest way to get started with payments. Included are some basic build and run scripts you can use to start up the application.

## Running the sample

1. Build the server

'''
pip3 install -r requirements.txt
'''

2. Run the server

'''
export FLASK_APP=server.py
python3 -m flask run --port=4242
'''

3. Go to [http://localhost:4242/checkout.html](http://localhost:4242/checkout.html)

https://blog.naver.com/soboruuu88/223064306754
