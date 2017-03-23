# modificed get_chats.py
# this just does the beautiful soup stuff (if i can get it to fucking work)
# need to get rid of special characters all of them 




def make_txt(msgs):
	
	import re
	
	txt = []
	is_it = 0
	
	m = msgs
			
	for part in m:
		part = re.sub(r'=[\n\r]*', '', part)
		part = re.sub(r'<div[^>]*>', '\n', part)
		part = re.sub(r'<[^<>]*>', '', part)
		part = re.sub(r'&nbsp;', ' ', part)
		part = re.sub(r'&[^;]*;', '', part)
		part = re.sub(r'\w\w?:\w\w\s[PA]M\s?', '', part)
		part = re.sub(r'\sme:', 'me:', part)
		part = part.strip()
		
		lines = part.split('\n')
		
		for line in lines:
			#print line
			if re.match(r'me:', line):
				#print line
				is_it = 1
				line = re.sub(r'me:', '', line)
				line = line.strip()
				txt.append(line)
			else:
				#if re.match(r'\w+:', line):
				if re.match(r'.+:\s', line):
					is_it = 0
				else:
					if is_it == 1:
						#print type(line)
						txt.append(line)

	return txt
		
if __name__ == '__main__':
	
	import sys
	import fetch
	
	args = sys.argv
	
	chat = open(args[1], 'r')
	
	txt = make_txt(chat)
	
	print txt
		
	
