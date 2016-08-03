#! /usr/bin/python3

import requests
import gi.repository
from bs4 import BeautifulSoup
gi.require_version('Notify','0.7')
from gi.repository import Notify,GdkPixbuf

res = requests.get('http://www.merriam-webster.com/word-of-the-day')
bs_obj = BeautifulSoup(res.text,'lxml')

#Finding the word of the day
word_of_the_day = bs_obj.h1.get_text()

#About the Word
word_type = bs_obj.find('span',{'class':'main-attr'}).get_text()

#Finding the meaning of the word or single meaning with example:
try:
    meaning = bs_obj.find('div',{'class':'wod-definition-container'}).select('p')[0].get_text()+'\n'+bs_obj.find('div',{'class':'wod-definition-container'}).select('p')[1].get_text()
#In case only single meaning given and no examples too:
except IndexError:
    meaning = bs_obj.find('div',{'class':'wod-definition-container'}).select('p')[0].get_text()

#Notification
Notify.init('Word_of_the_day')
nf = Notify.Notification.new(word_of_the_day.upper()+' ( '+word_type+' )',meaning)
#image = GdkPixbuf.Pixbuf.new_from_file('./Desktop/Python\ Stuff/Scraping/MW_logo.png')
#nf.set_image_from_pixbuf(image)
nf.show()

#Writing into a file
file = open('./Desktop/words/words_List.text','a')
file.write(word_of_the_day+':'+'\n'+meaning+'\n'+'\n')
file.close()