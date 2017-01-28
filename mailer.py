import sys
import time

import boto.ses


from config import *

# Get the email subject from command line
email_subject = sys.argv[1]

#creates connection to ses using boto
conn = boto.ses.connect_to_region(
                 BOTO_REGION,
                 aws_access_key_id=BOTO_ACCESS_KEY,
                 aws_secret_access_key=BOTO_ACCESS_SECRET)


file_content = open(HTML_FILE_PATH, 'r').read()
print file_content

contacts = open(CSV_FILE_PATH, 'r')

for i, contact in enumerate(contacts.readlines()):
	contact = contact.strip()
 	print i, contact
	try:
		conn.send_email(FROM_EMAIL, email_subject, '', [contact], html_body=file_content)
	except:
		print "error"
	# Sleep for some time to tackle max sending limit
	time.sleep(0.02)
