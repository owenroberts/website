#imaplib_connect.py

import imaplib
import ConfigParser
import os

def open_connection(u, p, verbose=False):
    # Read the config file
    config = ConfigParser.ConfigParser()
    config.read([os.path.expanduser('~/.pymotw')])

    # Connect to the server
    hostname = 'imap.gmail.com'
    if verbose: print 'Connecting to', hostname
    connection = imaplib.IMAP4_SSL(hostname, 993)

    # Login to our account
    username = u
    password = p
    if verbose: print 'Logging in as', username
    connection.login(username, password)
    return connection

if __name__ == '__main__':
    c = open_connection(verbose=True)
    try:
        print c
    finally:
        c.logout()