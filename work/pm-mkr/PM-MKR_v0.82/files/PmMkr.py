"""
Welcome to Pm-Mkr!
A window will open with the program.  
The program is still being tested and may take time to run.  
Thank you for your patience.

""" 

from processing.pdf import *
from controlP5 import ControlP5
from controlP5 import Textfield
import os
import sys
import amachine
import re
import f10
import imaplib
import email
import imaplib_connect
import make_txt

print __doc__


w = int(72*8.5)
h = 72*11

page = 0
lh = 16
nk = 0
xmargin = 30
ymargin = 60
boxw = w/4 - xmargin
boxh = h/4 - ymargin
space = 0
page = 0
frame = 0

txtlines = []
words = []
global font



def setup():
	size(w, h)
	global font, font2, font3
	global key_phrase
	global cp5, keyInput, eInput, pInput, p, e, pdfbutton, readmebutton
	global instructions, bimg
	global kinboolean, buttonboolean, openboolean, savedchats, totalmsgs, firsttry, imap
	global counter, msgcount
	
	sys.setrecursionlimit(1000)
	
	totalmsgs = 0
	msgcount = 1.0
		
	counter = 1.0
	savedchats = 0
	kinboolean = 0
	buttonboolean = 0
	openboolean = 0
	firsttry = 0
	imap = 0
	
	key_phrase = ""
	p = ""
	e = ""

	instructions = loadImage("img/instructions.jpg")
	bimg = loadImage("img/b.jpeg")
	
	font = loadFont("fonts/SansSerif-10.vlw")
	font2 = loadFont("fonts/SansSerif-20.vlw")
	font3 = loadFont("fonts/Helvetica-Bold-12.vlw")
	fill(0)
	textSize(10)
	textFont(font, 10)
	
	cp5 = ControlP5(this)
	
	eInput = cp5.addTextfield("einput", 10, 200, 200, 20).addListener(e_listener)
	eInput.setFocus(1)
	
	pInput = cp5.addTextfield("pinput", 10, 270, 200, 20).addListener(p_listener)
	#pInput.setPasswordMode(True)
	#pInput.setLabelVisible(0)
	
	keyInput = cp5.addTextfield("keyinput",10,220,170,20).addListener(key_listener)
	keyInput.hide()
	
	pdfbutton = cp5.addButton("OPEN POEM.PDF",100,14,170,80,19).addListener(b_listener)
	pdfbutton.hide()
	
	readmebutton = cp5.addButton("Read More",40,10,90,80,19).addListener(r_listener)
	
	background(255)
	
#readme button	
def r_listener(r):
	path = os.getcwd()
	os.system("open " + path + "/../readme.txt")
	
# listen for email input
def e_listener(em):
	global e
	e = em.stringValue()
	eInput.setFocus(0)
	pInput.setFocus(1)
	
# listen for password input	
def p_listener(pa):
	global p, eInput
	eInput.submit()
	p = pa.stringValue()
	
	
def keyPressed(): 
	if (key == TAB):
		eInput.setFocus(0)
		pInput.setFocus(1)
	
# listen for keyphrase input	
def key_listener(k):
	global key_phrase, keyInput
	key_phrase = k.stringValue()
	keyInput.remove()
	
def b_listener(b):
	path = os.getcwd()
	os.system("open " + path + "/poem.pdf")
	
	

def open_gchats(em, pa):
	global e, p, m, c, openboolean, firsttry, imap
	if firsttry == 0: firsttry = 1
	e = em
	p = pa
	
	try:
		c = imaplib_connect.open_connection(e, p)
		status, count = c.select('[Gmail]/Chats', readonly=True)
		if status == 'OK': 
			openboolean = 1
		elif status == 'NO':
			imap = 1
			eInput.setFocus(1)
			pInput.setFocus(0)
			e = ''
			p = ''		
		
	except:

		eInput.setFocus(1)
		pInput.setFocus(0)
		e = ''
		p = ''
	m = []
	
def save_gchats(chats):
	chat = chats
	
	filename = "gchats.txt"
	FILE = open(filename, 'w')
		
	for line in chat:
		try:
			FILE.writelines(line)
			FILE.writelines('\n')
		except TypeError:
			pass
		
	FILE.close()


	
	
def draw():
  global frame
  frame += 1
  global space, txtlines, page, nk
  global font, font2, font3
  global p1img
  global key_phrase
  global instructions, bimg
  global key_phrase
  global cp5, keyInput, eInput, pInput, p, e, pdfbutton, buttonboolean, readmebutton
  global kinboolean, buttonboolean, openboolean, savedchats, totalmsgs

  global m, c, counter, msgcount
  

  
  linelength = 0
  q = 0
  butt = 0
  background(255)
  
  chat = ""

  if page == 0:
	text("welcome to POEM MKR", 10, 10, width, 100)
	fill(112, 104, 133)
	text("POEM MKR uses an algorithm to generate a poem about you using your Gchat logs.  For more on this process, click the Read More button below.", 10, 30, 200, 200)
	image(bimg, 310, 0)
	
	fill(207, 180, 255)
	text("The first work created with PM-MKR, Apple Cat Death.", 310, 360)
	fill(0)
	
	text("POEM MKR was written and designed by Owen Ribbit for the class Reading and Writing Electronic Text, taught by Adam Parrish at ITP in Spring 2012.  I used Processing.py, Beautiful Soup, ControlP5 and the imaplib for Python, all extremely helpful and awesome resources.  Copyright (c) 2012 Owen Roberts", 10, 680, width/2, 400)

	
	try:
		chat = open('gchats.txt', 'r')
	except IOError:
		if openboolean == 0: 
			text("To generate a poem, please type your Gmail address...", 10, 50+120, 200,200)
			text("... then type your password and press ENTER.", 10, 90+150, 200, 40)
		text("Your information will not be saved anywhere.", 10, 90+220, 200, 40)
	
	
	if chat != "":
		eInput.remove()
		pInput.remove()
		text("Got the corpus of Gchats!", 10, 150)
		if key_phrase == "": 
			text("Please enter keywords, separated by a space (ex: apple cat death). I suggest 3 or more: ", 10, 170, 200, 200)
		if kinboolean == 0: 
			keyInput.show()
			keyInput.setFocus(1)
			kinboolean = 1
	
	else: 
		if firsttry == 1 and e == "": 
			fill(255,0,0)
			if imap == 0: text("You may have entered your info incorrectly.  Please try again.", 10, 140, 200, 200)
			if imap == 1: text("You may need to enable IMAP in your Gmail settings.  See Read More for directions.", 10, 125, 200, 200)
			fill(0)
			
		if e != "" and p != "":			
			if openboolean == 0:
				open_gchats(e, p)				
		
			if openboolean == 1:
				text("You probably have thousands of chats to download.  This could take a while, consider checking back in 10 minutes.  Once you have downloaded your chats, you can run the program again without the downloading time.", 10, 210, 300, 60)
				eInput.remove()
				pInput.remove()	
				try:			
					if counter > 0:
						text("Downloading msg " + str(int(counter)) + " / " + str(totalmsgs), 10, 170)
						rect(10, 180, 2, 10)
						rect(216, 180, 2, 10)
						if int(totalmsgs) is not 0:
							rect(14,180,(float(counter)/float(totalmsgs))*200, 10)
						try:
							c.select('[Gmail]/Chats', readonly=True)
							status, count = c.select('[Gmail]/Chats', readonly=True)
							if totalmsgs is 0:
								totalmsgs = count[0] 
								msgcount = float(float(totalmsgs) / 2000)
								if msgcount < 1: msgcount = 1
								
							typ, msg_data = c.fetch(int(counter), '(RFC822)')
							if msg_data[0] is None:
								counter = 0
								savedchats = 1
								return 0
							else:
								body = msg_data[0][1]
								for response_part in msg_data:
									if isinstance(response_part, tuple):
										msg = email.message_from_string(response_part[1])
										for part in msg.walk():
											if part.get_content_type() == 'text/html':
												m.append(part.get_payload(None, True))
												counter += msgcount
						finally:
							try:
								c.close()
							except:
									pass
									c.logout()
				
				except IOError:
					text("There seems to be an error.  Try entering your information again.", 10, 50)
			
				if savedchats is 1:
					text("Formatting messages...", 10, 250) 
					chat = make_txt.make_txt(m)
					save_gchats(chat)
					savedchats = 0

	
	if key_phrase != "":
		key_phrase = re.sub(r'[,.-]', '', key_phrase)
		file_phrase = re.sub(r'\s', '-', key_phrase)
		key_words = key_phrase.split(" ")
	
		if key_phrase != "": text("Generating poem...", 10, 200)
		if key_phrase != "": text("If this takes longer than 2-3 minutes, try restarting the program.  You will not have to wait for downloading time.", 10, 220, 200, 200)
	
		print "writing file with key words"
		
		filename = "poems/" + file_phrase + ".txt"
		open(filename, 'w').close()
		FILE = open(filename, 'a')
		poemmaker = f10.PmMkr()
		for key in key_words:
			poemmaker.make_poem(key, chat, "")
			p = poemmaker.get_poem()
			poem = amachine.amachine(p, key)
			FILE.writelines(poem)
		FILE.close()
	
		txtlines = loadStrings(filename);
	
		for j in range(len(txtlines)):
			space += ceil(textWidth(txtlines[j])) / boxw
	
		space = space * lh
		space = space/32
		if (space > boxh):
			space = boxh - 10
	
		page += 1
		
		print "done loading file, setting up space"
	
	
	
	
  elif page == 1:
	
	keyInput.remove()
	readmebutton.remove()
	
	print "buidling first page"
	
	
	for k in range(len(txtlines)):
		if q < 15:	
			nk = k
        	nb = ceil(textWidth(txtlines[k])) / boxw
        	if (5+(butt+nb)*lh) > space:
          		q += 1
          		butt = 0
		elif q == 1:
          #THE TITLE
			kx = 20 + 5 + q%4*(w/4)
			ky = 80 + floor(q/4)*h/4 + butt*lh
			morey = ceil(textWidth(key_phrase)/boxw)
			text(str(key_phrase), kx, ky, boxw, boxh)
			text("by owen ribbit", kx, ky + morey*14, boxw, boxh)
			k -= 1
			q += 1
		else:
			if floor(q/4) == 1 or floor(q/4) == 3:
				kx = xmargin/2 + q%4*(w/4)
				ky = ymargin/2 + floor(q/4)*h/4 + butt*lh - h/4
				pushMatrix()
				translate(w, h)
				rotate(PI)
				text(txtlines[k], kx, ky, boxw, boxh)
				wordlines = 1
				words = split(txtlines[k], " ")
				for i in range(len(words)):
					linelength += textWidth(words[i])
					if (linelength > boxw):
						wordlines += 1
						linelength = int(textWidth(words[i]))
				butt += wordlines
				popMatrix()
			else:
				kx = xmargin/2 + q%4*(w/4)
				ky = ymargin/2 + floor(q/4)*h/4 + butt*lh
				text(txtlines[k], kx, ky, boxw, boxh)
				wordlines = 1
				words = split(txtlines[k], " ")
				for i in range(len(words)):
					linelength += textWidth(words[i])
					if (linelength > boxw):
						wordlines += 1
						linelength = int(textWidth(words[i]))
				butt += wordlines
	saveFrame("p1.png")
	p1img = loadImage("p1.png")
	background(255)
	text("Preparing the layout for printing...", 10, 20, 200, 20)
	page += 1
	
	print "done building first page"

  elif page == 2:
	
	print "building second page"
	
	for j in range(len(txtlines)):
		space += ceil(textWidth(txtlines[j])) / boxw
		space = space * lh
		space = space/16
	if (space > boxh):
		space = boxh - 10
	butt = 0
	q = 0
	for k in range(nk, len(txtlines)):		
		nb = ceil(textWidth(txtlines[k])) / boxw
		if (5+(butt+nb)*lh) > space:
			q += 1
			butt = 0
		if floor(q/4) == 1 or floor(q/4) == 3:
			kx = xmargin/2 + q%4*(w/4)
			ky = ymargin/2 + floor(q/4)*h/4 + butt*lh - h/4
			pushMatrix()
			translate(w, h)
			rotate(PI)
			text(txtlines[k], kx, ky, boxw, boxh)
			wordlines = 1
			words = split(txtlines[k], " ")
			for i in range(len(words)):
				linelength += textWidth(words[i])
				if (linelength > boxw):
					wordlines += 1
					linelength = int(textWidth(words[i]))
			butt += wordlines
			popMatrix()
		
		else:
			kx = xmargin/2 + q%4*(w/4)
			ky = ymargin/2 + floor(q/4)*h/4 + butt*lh
			text(txtlines[k], kx, ky, boxw, boxh)
			wordlines = 1
			words = split(txtlines[k], " ")
			for i in range(len(words)):
				linelength += textWidth(words[i])
				if (linelength > boxw):
					wordlines += 1
					linelength = int(textWidth(words[i]))
			butt += wordlines
	
	print "saving images "
			
	saveFrame("p2.png")
	p2img = loadImage("p2.png")
	print "making pdf"
	pdf = beginRecord(PDF, "poem.pdf")
	image(p1img, 0, 0)
	pdf.nextPage()
	image(p2img, 0, 0)
	endRecord()
	page += 1
	
	print "done with pdf"

  elif page == 3:
	
	
	if buttonboolean == 0:
		pdfbutton.show()
		buttonboolean = 1
	
	image(instructions, 0, 0)


run()