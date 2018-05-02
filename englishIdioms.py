from tkinter import *
from tkinter import messagebox
import bs4 as bs
import urllib.request
import random

root = Tk()
root.geometry('600x450')
root.title("English Idioms")

# download idioms from a website
sauce = urllib.request.urlopen('http://www.smart-words.org/quotes-sayings/idioms-meaning.html').read()
soup = bs.BeautifulSoup(sauce, 'lxml')
idioms = soup.find('dl')

# get random idiom
def getIdiom():
    global idioms
    idioms_list = []
    meaning_list = []

    idioms_rows = idioms.find_all('dt')
    for dt in idioms_rows:
        idioms_list.append(dt.text)

    meaning_rows = idioms.find_all('dd')
    for dd in meaning_rows:
        meaning_list.append(dd.text)

    dictionary = dict(zip(idioms_list, meaning_list))

    key, value = random.choice(list(dictionary.items()))
    idiomVar.set(key)
    meaningVar.set(value)


# create string variables
idiomVar = StringVar()
meaningVar = StringVar()

# create and position widgets in the window
top = Frame(root)
top.pack()
middle = Frame(root)
middle.pack()
bottom = Frame(root)
bottom.pack()
idiomLabel = Label(top, textvariable=idiomVar, fg="blue", font=("Arial", 30, "italic"), wraplength=500)
idiomLabel.grid(row=0, column=0, pady=(50,20))
meaningLabel = Label(middle, textvariable=meaningVar, fg="black", font=("Arial", 14), wraplength=500)
meaningLabel.grid(row=0, column=0, pady=(10,40))
butt = Button(bottom, text="Random idiom", command=getIdiom)
butt.grid(row=0, column=0)

root.mainloop()
