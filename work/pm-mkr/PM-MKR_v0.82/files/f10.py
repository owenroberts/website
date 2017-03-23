# this is supposed to do everything

class PmMkr(object):
	
	def __init__(self):
		self.poem = []

	def print_poem(self):
		print self.poem
	
	def get_poem(self):
		return self.poem

	def make_poem(self, key, chat, check):		
		import re
		import random
	
		debug = 1

		if debug is 0: print "NEW"

		k = key
		c = chat
		h = check
		b = 0
		newvar = 0
		
		new_line = ""
		punc = re.compile(r'[-.?!,\'":;()|0-9]')

		rchat = list()

		for line in c:
			line = line.strip()
			rchat.append(line)
		random.shuffle(rchat)

		for line in rchat:

			line = line.strip()
			r1 = '\\b' + k

			if re.search(r1, line):
				if line != h:
					#if b is 0: print line
					if b is 0: 
						self.poem.append(line + '\n')
					new_line = line

					r = k + '\W*\s\S+\\b'				
					if re.search(r, line):
						new_line = line
						#if b is 1: print line
						if b is 1: 
							self.poem.append(line + '\n')
							
						b = 0
						n = re.search(r, line)

						nk = n.group(0)
						nk = punc.sub("",nk)
						newvar = self.make_poem(nk, c, line)

					else:
						b = 1
				else:
					new_line = line
					b = 1

		if b is 1:
			b = 0
			h = h.strip()
			words = h.split(" ")
			nk = words[-1]
			nk = punc.sub("",nk)

			if nk != k and nk != "" and new_line != "":
				newvar = self.make_poem(nk, c, new_line)

			else:
				#print "SHOULD BE OVER"
				return 1 
				#sys.exit(0)
					
				


	
if __name__ == '__main__':
	import sys
	import get_chats
	import amachine
	import re
	
	sys.setrecursionlimit(1000)
		
	args = sys.argv
	
	try:
	   chat = open('gchats.txt', 'r')
	except IOError:
		chat = get_chats.get_chats("obroberts@gmail.com", "$dogwood1")
	  	print 'Getting chats.  This may take a while.'
	
	key_phrase = raw_input("Please enter keywords, I suggest 3 or more: ")
	key_phrase = re.sub(r'[,.-]', '', key_phrase)
	file_phrase = re.sub(r'\s','-', key_phrase)
	key_words = key_phrase.split(" ")

	filename = file_phrase + ".txt"
	open(filename, 'w').close()
	FILE = open(filename, 'a')	
	poemmaker = PmMkr()
	for key in key_words:
		poemmaker.make_poem(key, chat, "")
		p = poemmaker.get_poem()
		poem = amachine.amachine(p, key)
		print poem
		FILE.writelines(poem)	
	FILE.close()
