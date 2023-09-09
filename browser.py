import socket
import re

done = False

while done is False:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input('Socket is ready. What host do you want to connect to? (Use format like (without quotes) "www.reddit.com".): ')
    while re.search("^www\..*[a-z*]$", host) == None:
        host = input('Please enter a valid host: ')
    print('Thanks for the valid host! Now we will need to send a GET request to see a certain page\'s content.')
    url = input('Enter a valid URL for the page: ')
    validRegex = r"^https*://" + re.escape(host) + r"/"
    while re.search(validRegex, url) == None:
        url = input('Please enter a valid URL: ')
        
    print("Thanks for the valid URL!")
    print("We'll be connecting to", host, "\nand we will GET", url, ":")

    mysock.connect((host, 80))

    cmdString = 'GET ' + url + ' HTTP/1.0\n\n'
    cmd = 'GET http://www.reddit.com/r/gamedev HTTP/1.0\n\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if (len(data)  < 1):
            break
        print(data.decode())
        
    mysock.close()
    
    userInput = input("Connect to something else? Enter 0 to exit: ")
    if userInput == '0': done = True
