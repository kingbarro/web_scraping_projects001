#! I really like a multi-colored file (:-)

#Importing relevant modules
from asyncore import read
import webbrowser as wb
import requests, os
import pyttsx3 as pt
import bs4
#import sys
#import pyperclip



#def searching_place():
   # pt.speak('Please give me a location')
    #address = input()
    #pt.speak('You are looking for ')
    #pt.speak(address)
#print('some thing'+ address)

#Get address from clipboard
#address = pyperclip.paste()

#open browser and search address
    #wb.open('https://www.google.com/maps/place/' + address)

#searching_place()


def get_webpage():          #open web page and scraping function
    res = requests.get('http://nostarch.com/')
    type(res)
    
    #Error handling
    try:
        res.raise_for_status()

    except Exception as ex:
        print('DOWNLOAD FAILED %s' % (ex))
    
    #len(res.text)

    print(res.text[:])
    
    #Save the downloaded file to HardDisk (any format)
    saving_page = open('SavedHtml1.html', 'wb')
    for chunk in res.iter_content(100000):
        saving_page.write(chunk)
        print('Saving file ...')     
        print() 
        print('File save at '+ os.getcwd())
    saving_page.close()


    #Store the returned object to the variable 
    #parseTree
    #parseText = bs4.BeautifulSoup(res.text)
    #type(parseText)

    #Or we can load HTML from hard drive
    #saved_file = open('SavedHtml.html')
    #parse_it = bs4.BeautifulSoup(saved_file)
    #type(parse_it)


    
    


def main():
    get_webpage()

if __name__ == '__main__':
    main()
