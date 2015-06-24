#this script responds to texts, and takes message body (prints to webpage)

#THIS SCRIPT CONTROLS EVERYTHING - MAIN FILE WHICH RESPONDS AND TEXTS TO CUSOTMERS
import test_sms
import request_amazon
import unicodedata
#can now use item classes from product search.
from product_search import Item
from flask import Flask, request, redirect
import twilio.twiml


#IMPORT APP_STRIPE, INDEX_STRIPE, CHARGE_STRIPE, LAYOUT_STRIPE




 
app = Flask(__name__)

#item needs to contain the product asin when it runs thorugh the clause
asin = None
# 3 states: suggestion, purchase, and confirmation
state = 'suggestion'
#customer is number as a string
customer = None
#whether they want to purchase or not
result = None



@app.route("/my_twilio_endpoint", methods=['GET', 'POST'])
def reply():

	
	global state
	global asin
	global customer
	global result
	global message_body

#unicode to string
	message_body = request.form['Body']
	message_body = message_body.encode("utf-8", "ignore")
	customer = request.form['From']
	customer = customer.encode("utf-8", "ignore")

	print '1'

	if state == 'suggestion':

	#print message_body
		item = Item(message_body)
		#can add image later
		txtresp = "We found this product : {0}. The price will be: {2} {1}. Respond 'Yes' if you would like to purchase this item, and 'No' if you dont quite fancy it!".format(item.prod_item(), item.prod_price()[0], item.prod_price()[1])
		resp = twilio.twiml.Response()
		resp.message(txtresp)
		asin = str(item.prod_asin())
		print '2'
		state = 'purchase'
		
		#this return statement is needed to send response text - and also returns on web app
		return str(resp)
		
		
	elif state == 'purchase':
		#FIX TO MAKE ALL YESES WITH LOWERCASE ETC
		if message_body == 'Yes' or message_body == 'yes' or message_body =='YES':
			#buy product
			print '3'
			print message_body
			result = 'Please text back your preferred shipping address and name in the format: [First name], [Last name], [Address line 1], [Address line 2(can leave empty)], [zip code], [city], [state]'
			test_sms.shipping_request(result, customer)
			state = 'confirmation'


		else:
			state = 'suggestion'
			print '4'
			result = 'We are sorry that you do not want to purchase this item. Please search for a different product!'
			test_sms.send(result, customer)
			customer = None
			result = None
			


			#IF SHIPPING ADDRESS MAKES SENSE (CAN USE EITHER PARSING (USING COMMAS), OR PYADDRESS MODULE LIBRARY)
	elif state == 'confirmation':		
		if shipping address ok, message body = full:
				#PUT INFORMATION INTO INFO IN REQUEST_AMAZON.PY (SHIPPING AND NAME)
				#CHECK USING MESSAGE_BODY - also store in mongo database, customer name, phone and shipping address
				txtresp = 'Please fill out your credit card info' + URL to flask web page with stripe credit card info + /endpoint? or just customer number already in a form box
				txtresp += 'you have 5 mins to fill this out as we store your request - your product might be unavailable if you take more than 5 mins'
				resp = twilio.twiml.Response()
				resp.message(txtresp)
				state = 'purchasing'
				return str(txtresp)

		else:
			result = 'sorry you have an invalid shipping address, please search for an item you would like to purchase.'
			
			test_sms(result, customer)
			state = 'suggestion'
			asin = None
			result = None


	elif state == 'purchasing':
		#ULTIMATUM OF 5 MINS -- WITHIN 5 MINS!!
		if stripe form filled out with credit card info and billing info, and token received, successfully:
			store stripe token (prob from flask web server stored into mongodb) #have to import those files

			#whether it went through or not is result
			#all shipping info should have been put in above conditional

			#PURCHASE ON OUR ACCOUNT
			result = request_amazon.buy(asin)
			
			#MUST RETURN SOMETING?
			#did all go well?
			test_sms.send(result,customer)
			print '5'
			asin = None
			result = None
			state = 'suggestion'
			#MUST RETURN SOMETING?		
			return None

			#THEN HOW ARE WE ACTUALLY GOING TO CHARGE THEM?
			#IMPORT FILE AND CHARGE.. using 
			use selenium?
			if result was successful, charge token by product.asin.price + rickys commision! (import stripe file)
		else:
			result = 'Sorry you took too long, please respond with a new choice of product.'
			test_sms.send(result, customer)
			state = 'suggestion'
			asin = None
			result = None




if __name__ == "__main__":
    app.run(debug = True, port=80, host = '0.0.0.0')

 #message_body is content. 