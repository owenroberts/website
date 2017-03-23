Hello.

This program will download a selection up to 2000 of all of the Gchats you have ever written (it will not download the Gchats written by your friends and correspondents) and then turn them into a poem, which you can print and make into a booklet or chapbook.  

The program uses an algorithm that takes key words that you input and a poetic style that I have programmed to generate a unique poem based on the words you have written.  Once the poem has been generated there will be instructions to print and make the book.  Once you download your Gchats it will be much faster to repeat the process.  Downloading the Gchats takes a while so it requires some patience.  The algorithm uses a recursive structure, meaning that each line of the poem uses the same function to generate a new line, until certain criteria are met.  This means that the poem generation time varies a lot, sometimes it takes two seconds, sometimes two minutes.  If it takes longer than two minutes, it may be stuck in a recursive loop, in which case, its best just to restart the program.  The Gchats will be saved, so the download time won't be required again.

In most cases you will be able to run the program in less than ten minutes.  If it seems to be taking too long to generate a poem, after the Gchats have been downloaded, it is a good idea to restart the program.  When entering key words for your poem, it helps to avoid common words like a, it, is, the etc and long or obscure words.  It also helps to pick words that you use regularly.  You can read more about the process and program here:

http://itp.nyu.edu/~obr208/blog/2012/05/09/rwet-final-documentation/

Double click the pmmkr file to run!

If you do print out your poem, it would be awesome if you sent a photo to me at obr208@nyu.edu.

If you have not already done so, be sure to activate IMAP in your Gmail account.  In settings, go to "Forwarding and POP/IMAP" and check "Enable IMAP" in the "IMAP Access panel".  Then go to "Labels" and check "Show in IMAP" for the Chats folder.  Be sure to change you settings.

PM MKR was written and designed by Owen Roberts for the class Reading and Writing Electronic Text, taught by Adam Parrish at ITP in Spring 2012.  Copyright (c) 2012 Owen Roberts

I used many resources including Processing.py, Beautiful Soup, ControlP5 and the imaplib for Python.

The code is all viewable in the files folder you have downloaded.  I don't know a whole lot about the rules of open source and everything like that, but I'm fairly certain all of the code I have used is open source or available for people, and my code is all right there if you actually want to use it for some reason.

Some notes on security and other conceptual issues:

I say it in the program, and my code is completely open for people to read so you can find out for sure, but there’s no way to really prove that I’m not doing anything with the Gmail emails and passwords that need to be entered for the program to run.  I haven’t come up with a satisfying solution to this problem and I’ve kind of resigned for now to the idea that people will either have to trust me or not care.  The imaplib uses SSL to login to Gmail, which I assume provides enough security for the average user, but I don’t know enough about those issues to guarantee that using the program is completely secure.  The only alternative I can suggest is just changing your Gmail password, either temporarily while you use the program, or changing it to something new after you use the program.  All I can say is that I've run it on my own Gmail hundreds of times at this point and have not changed my password and have never had a problem.

An important conceptual issue is the final step of printing a little chapbook.  It is obvious, and proven true through testing, that few people will actually make the final step of printing the book out, even though it was the original inspiration for the whole program (for me).  But, if you open the pdf and don’t print the poem, it is very difficult to read, because its laid out to be printed, so many of the page are upside down, because of the way the paper has to be folded.  I was convinced for a bit that I should make the option for users to just read a digital version, but I decided I wanted to push people to print it out as much as possible.  But as a bonus for people who use it a lot, I decided to save text copies of all the poems in a directory called “poems” in the “files” directory.  So that’s also a bonus for anyone who is still reading this readme. ; )
