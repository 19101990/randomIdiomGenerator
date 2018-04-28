import bs4 as bs
import urllib.request
import random

sauce = urllib.request.urlopen('http://www.smart-words.org/quotes-sayings/idioms-meaning.html').read()
soup = bs.BeautifulSoup(sauce, 'lxml')
idioms = soup.find('dl')

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
print(key.upper() + "\n" + value)
