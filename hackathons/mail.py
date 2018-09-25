import sendgrid
import os
from sendgrid.helpers.mail import *
import pandas as pd


email_list = []
API_KEY = <get_api_key_from_sendgrid>

detail = pd.read_excel('hackathon.xlsx')
details = pd.DataFrame(detail)


def main_func(email_id):
	from_email = Email("rahulkumaran313@gmail.com", name="Rahul Arulkumaran")
	to_email = Email(email_id)
	subject = "Testing Merkalysis"
	content = Content("text/html", "<html><body><p>Test Email from Instalysis to figure out whether the API is functioning proper or not!</p></body></html>")
	mail = Mail(from_email, subject, to_email, content)
	response = sg.client.mail.send.post(request_body=mail.get())
	return response



if(__name__=="__main__"):
	sg = sendgrid.SendGridAPIClient(apikey=API_KEY)
	print(len(details))
	for hs in detail["email"]:
		email_list += [hs]
	print(email_list, len(email_list))
	i=0
	for email_id in email_list:
		i+=1
		response = main_func(email_id)
		print(i, response.status_code)
