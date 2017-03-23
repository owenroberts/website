# hw-3 markov chain with a-machine

import sys
args = sys.argv
import re
from markov import MarkovGenerator

def amachine(txt, name):

	txt_lines = txt
	#print type(txt_lines)
#	print txt_lines
	name = re.sub(r'[aeiou]', '', name)

	key = ""
	tempKey = ""
	firstWord = 0
	keySet = 0
	tempKeySet = 0
	wordSet = 0
	notWord = 0
	lastWord = ""

	thePoem = ""

	# break through lines
	for line in txt_lines:
		#print line
		line.strip()
		#split words
		words = line.split(" ")
		#go through words
		#print words
		for word in words:

		#	if word == lastWord:
			if word != lastWord:
				#go through letters
				tempKeySet = keySet
				for letter in word:
					r = name + "lnkvt"
					if re.search(r'[%s]' % r, letter.lower()):				
						if notWord == 0:
							if keySet == 0:		
							# find the first vowel
								tempKey = letter.lower()
								keySet = 1
								wordSet = 1
							else:
								if letter.lower() == tempKey:
									keySet = 0
									wordSet = 1
								else: 
									wordSet = 0
									notWord = 1
									tempKey = key
									keySet = tempKeySet							
			

				if wordSet == 1 and notWord == 0:
					#print word
					key = tempKey
					#print key
					wordSet = 0
					thePoem += " " + word
					lastWord = word
					if firstWord == 0:
						firstWord = 1
				else:
					notWord = 0
					wordSet = 0
					if firstWord == 0:
						keySet = 0
						firstWord = 1
				
	#print "##" + thePoem 

	#that was the midterm
	#here's some markov

	generator = MarkovGenerator(n=1, max=500)

	line = thePoem.strip()
	line = re.sub(r'["\[\]()]', '', line)
	generator.feed(line)

	genpoem = generator.generate()
	#print genpoem
	return genpoem
	
	#return thePoem

if __name__ == '__main__':
	
	import sys
	import re
	
	args = sys.argv
	
	t = open(args[1], 'r')
	
		
	n = args[1]
	n = re.sub(r'.txt', '', n)
	n = re.sub(r'\w[/]', '', n)
	
	p = amachine(t, n)
	
	print p
	
	
	

