import smtplib

def mail(receiver,link):

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	username = os.environ.get('mail_user')
	password = os.environ.get('mail_pass')

	server.login(username,password)

	subject = ' PRICE DROP ALERT'
	body = 'Hey Buddy. The price has dropped for your product. Please check ' + link


	msg = f"Subject: {subject}\n\n{body}"

	server.sendmail (
		username,
		receiver,
		msg
	)

	server.quit()