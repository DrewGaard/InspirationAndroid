from bs4 import BeautifulSoup as soup
from urllib import urlopen as uReq
import re
import threading
import tkMessageBox

def getQuotes():
    my_url_base = "https://www.goodreads.com/quotes?page="

    validPageNumbers = range(1,2)
    page_soup = []

    for n in range(len(validPageNumbers)):
        url = my_url_base + str(validPageNumbers[n])
        print(url)
        uClient = uReq(url)
        page_html = uClient.read()
        uClient.close()
        page_soup.append(soup(page_html, "html.parser"))

    ##uClient = uReq(my_url_base)
    ##page_html = uClient.read()

    ##uClient.close()


    #page_soup = soup(page_html, "html.parser")



    ##print(page_soup.h1)

    rawListClean = []

    for n in range(len(page_soup)): 
        quotesContainer = page_soup[n].findAll("div",{"class":"quote"})
        rawListMessy = []
        

        for singleQuoteContainer in quotesContainer:
            result = singleQuoteContainer.find("div", {"class":"quoteText"})
            rawListMessy.append(result.text)
            ##print(singleQuoteContainer.select('div.quoteText').text)




        for item in rawListMessy:
            #https://stackoverflow.com/questions/904746/how-to-remove-all-characters-after-a-specific-character-in-python
            clean = item.split("//<![CDATA[", 1)[0]
            print("-------------------------------------------------------")
            print(clean)
            clean = re.sub(r"[\n\t]*", "", clean)
            clean = clean.strip()
            if (len(clean)) < 110: #since twitter messages can't be over 140 chars
                rawListClean.append(clean)
            print("-------------------------------------------------------")


    with open('quotes.txt', 'w+') as f:
        for item in rawListClean:
            f.write("%s\n" % item.encode("ascii","ignore"))


def threadGetQuotes():
    threading.Thread(target=getQuotes).start()

        
##print(quotesContainer)


##singleQuoteContainer = quotesContainer[0]

##print(singleQuoteContainer)

##rawListMessy = []
##rawListClean = []
##
##for singleQuoteContainer in quotesContainer:
##    result = singleQuoteContainer.find("div", {"class":"quoteText"})
##    rawListMessy.append(result.text)
##    ##print(singleQuoteContainer.select('div.quoteText').text)
##
##
##
##
##for item in rawListMessy:
##    #https://stackoverflow.com/questions/904746/how-to-remove-all-characters-after-a-specific-character-in-python
##    clean = item.split("//<![CDATA[", 1)[0]
##    print("-------------------------------------------------------")
##    print(clean)
##    clean = re.sub(r"[\n\t]*", "", clean)
##    clean = clean.strip()
##    rawListClean.append(clean)
##    print("-------------------------------------------------------")
##
##with open('scraperquotes.txt', 'w+') as f:
##    for item in rawListClean:
##        f.write("%s\n" % item.encode('utf-8'))







