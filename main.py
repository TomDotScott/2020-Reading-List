import requests
from bs4 import BeautifulSoup
import pandas

readinglist = pandas.DataFrame()

for year in range(2013, 2020):
    for month in range(1, 13):
        if month < 10:
            month = '0' + str(month)
        url = 'https://www.nytimes.com/books/best-sellers/{0}/{1}/01/combined-print-and-e-book-fiction/'.format(str(year), month)
        webpage = requests.get(url)

        print("NOW ON: ", month, year)

        soup = BeautifulSoup(webpage.text, 'html.parser')
        top10 = soup.findAll("ol", {"class": "css-12yzwg4"})[0].findAll("div", {"class": "css-xe4cfy"})

        for i in range(len(top10)):
            book = top10[i].contents[0]
            title = book.findAll("h3", {"class": "css-5pe77f"})[0].text
            author = book.findAll("p", {"class": "css-hjukut"})[0].text

            item = pandas.Series([title, author, i + 1, month, year], index=['Title', 'Author', 'Position', 'Month', 'Year'])
            readinglist = readinglist.append(item, ignore_index=True, sort=False)

print(readinglist)
readinglist.to_csv("readinglist.csv", index=False)



