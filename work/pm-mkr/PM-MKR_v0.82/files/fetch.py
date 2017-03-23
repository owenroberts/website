# fetch.py

import imaplib
import email
import imaplib_connect
import re
import getpass

def get_msgs(e, p):
	
	em = e
	if re.search(r'.+@gmail[.]com', e):
		print "thanks!"
	else:
		e += "@gmail.com"
	pa = p
	print "Thanks!"
	
	
	c = imaplib_connect.open_connection(em, pa)
	print type(c)
	m = []
	
	counter = 1
	while counter > 0:
		print "Downloading msg " + str(counter)
#	for i in range(1, 2000):
		try:
			c.select('[Gmail]/Chats', readonly=True)
			typ, msg_data = c.fetch(counter, '(RFC822)')
			if msg_data[0] is None:
				counter = 0
				return 0
			else:
				counter += 1
				body = msg_data[0][1]
				for response_part in msg_data:
					if isinstance(response_part, tuple):
						msg = email.message_from_string(response_part[1])
						for part in msg.walk():
							if part.get_content_type() == 'text/html':
								m.append(part.get_payload(None, True))
					
		finally:
			try:
				c.close()
			except:
					pass
					c.logout()
	
	return m
				

if __name__ == '__main__':
	import sys
	args = sys.argv
	
	m = get_msgs('obroberts@gmail.com', '$dogwood1')
	print m