

#use ZINC API TO BUY FROM AMAZON USING API -- CHANGE SOME CREDS TO MATCH CUSTOMERS'
import requests
import product_search
import json
from amazon.api import AmazonAPI
#python request http request
#to https://api.zinc.io/v0/order
#curl https://api.zinc.io/v0/order -d
import ssl

#add valid credit card info etc


def buy(asin, first_name, surname, address_line1, address_line2, zip_code, city, state, customer, ):
	url = "https://api.zinc.io/v0/order"
	info = {"client_token": "597348b9c4452620817acf4a", "retailer": "amazon", "products": [{"product_id": asin, "quantity": 1}],"max_price": 0, "shipping_address": {  "first_name": first_name,  "last_name": surname,   "address_line1": address_line1,  "address_line2": address_line2,  "zip_code": zip_code,"city": city,   "state": state,  "country": "US",  "phone_number": customer}, "is_gift": True, "gift_message": "Heres your package, Enjoy!", "shipping_method": "cheapest", "payment_method": {  "name_on_card": "Zinc credit card",  "number": "zinc number",  "security_code": "xxxx",  "expiration_month": x,  "expiration_year": xxxx,  "use_gift": False },"billing_address": {  "first_name": "William",    "last_name": "Rogers",  "address_line1": "84 Massachusetts Ave",   "address_line2": "",  "zip_code": "02139",  "city": "Cambridge",   "state": "MA",  "country": "US",  "phone_number": "5551234567"}, "retailer_credentials": {  "email": "moezinia.r@gmail.com",  "password": "q2wq2wq2w"},"webhooks": {  "order_placed": "http://mywebsite.com/zinc/order_placed",  "order_failed": "http://mywebsite.com/zinc/order_failed",  "tracking_obtained": "http://mywebsite.com/zinc/tracking_obtained" },"client_notes": {  "our_internal_order_id": "abc123"}}
	print requests.post(url, data = json.dumps(info)).status_code

	if requests.post(url, data = json.dumps(info)).status_code == 200:
		post_api_request = requests.post(url, data = json.dumps(info))
		post_api_request.json()
		#print post_api_request
		#print post_api_request.text
		return 'Your order has been processed and is on its way! Thanks so much for using trickyricky tm'
	else:
		print post_api_request.raise_for_status()
		return 'Sorry, your order has not processed, please try again by texting us your desired item'
		raise Exception("Order not processed")




