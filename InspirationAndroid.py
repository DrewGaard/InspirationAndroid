import tweepy
import random
import threading
import os
import Tkinter
from Tkinter import Entry
from Tkinter import StringVar
from Tkinter import Label
import tkMessageBox
import sys
from webscraper import threadGetQuotes

##auth = tweepy.OAuthHandler("PufrdE08T8Zw20zXgaUZgKlOB", "LGi8jRaToWVHfVKGaPFkf7VNlTzok2UdgV6CtWNffcoWvu08mR")
##auth.set_access_token("1100180733006536704-V34XaV7utGKGAyFA8m9EvV50kHf9mC", "2N3Yr3TzrAy9L0aTNbzVMxQtHVWRqYOYsRNKHjNRHNQwN")
##
##api = tweepy.API(auth)

gui = Tkinter.Tk()
gui.geometry('450x450+500+300')
gui.title('Inspiration Android')


apiInfoEntered = False

consumerKeyVar = StringVar()
consumerSecretVar = StringVar()
accessTokenVar = StringVar()
accessTokenSecretVar = StringVar()

##if os.stat("apiinfo.txt").st_size == 0:
##    print("No file found.")
##else:

if os.path.exists("apiinfo.txt"):
    append_write = 'r+'
else:
    append_write = 'w+'

apiFile = "apiinfo.txt"
myApiInfoList = []
with open(apiFile, append_write) as apiFile:
    myApiInfoList = apiFile.read().splitlines()

if os.stat("apiinfo.txt").st_size == 0:
    print("No file found.")
else:
    consumerKeyVar.set(myApiInfoList[0])
    consumerSecretVar.set(myApiInfoList[1])
    accessTokenVar.set(myApiInfoList[2])
    accessTokenSecretVar.set(myApiInfoList[3])


getQuotesLabel = Label(gui, text = "Press the button below to get quotes:")
getQuotesLabel.pack()

getQuotesButton = Tkinter.Button(gui, text="Get Quotes", command = threadGetQuotes)
getQuotesButton.pack()


consumerKeyLabel = Label(gui, text = "Consumer Key:")
consumerKeyLabel.pack()
consumerKey = Entry(gui, textvariable=consumerKeyVar).pack()

consumerSecretLabel = Label(gui, text = "Consumer Secret:")
consumerSecretLabel.pack()
consumerSecret = Entry(gui, textvariable=consumerSecretVar).pack()

accessTokenLabel = Label(gui, text = "Access Token:")
accessTokenLabel.pack()
accessToken = Entry(gui, textvariable=accessTokenVar).pack()

accessTokenSecretLabel = Label(gui, text = "Access Token Secret:")
accessTokenSecretLabel.pack()
accessTokenSecret = Entry(gui, textvariable=accessTokenSecretVar).pack()



def tweetit():
    t = threading.Timer(3600.0, tweetit) #3600
    t.start()


    #Here I am checking to see if the program has been running before. If that is the case
    #Then the file that has delete the previous tweets should be used to eliminate duplicate tweets
    if os.stat("newquotes.txt").st_size == 0:
        f = "quotes.txt"
        print("getting first list")
    else:
        f = "newquotes.txt"


    with open(f, append_write_quotes) as f:
        mylist = f.read().splitlines()

    #print mylist

    listLength = len(mylist)

    if listLength == 0:
        t.cancel
        print("Empty List.")
        tkMessageBox.showinfo("Empty List Error", "Something went wrong. Please get quotes before starting the program!")
        startButton.pack_forget()
        return

    randNum = random.randint(0, listLength - 1)
    print(mylist[randNum] + " " + hashtags)

    try:
        api.update_status(mylist[randNum] + " " + hashtags)
    except Exception:
        tkMessageBox.showinfo("API Call Error", "Something went wrong. Please check the provided information for all the API text fields!")
        startButton.pack_forget()
        
    del mylist[randNum]

    with open("newquotes.txt", "w") as f:
        for item in mylist:
            f.write("%s\n" % item)


startButton = Tkinter.Button(gui, text="Start", command = tweetit)



def getValues():
    consumerKeyEntered = consumerKeyVar.get()
    print(consumerKeyEntered)
    consumerSecretEntered = consumerSecretVar.get()
    print(consumerSecretEntered)

    accessTokenEntered = accessTokenVar.get()
    print(accessTokenEntered)

    accessTokenSecretEntered = accessTokenSecretVar.get()
    print(accessTokenSecretEntered)

    #Unfortunatley I used global variables
    global auth
    global api
    global apiInfoEntered

    
    if consumerKeyEntered == "" or consumerSecretEntered == "" or accessTokenEntered == "" or accessTokenSecretEntered == "":
        tkMessageBox.showinfo("Missing Information", "Please enter the correct information for all the text fields!")
    else:
        apiList = []
        apiList.append(consumerKeyEntered)
        apiList.append(consumerSecretEntered)
        apiList.append(accessTokenEntered)
        apiList.append(accessTokenSecretEntered)
        
        with open("apiinfo.txt", "w") as f:
            for item in apiList:
                f.write("%s\n" % item)
        
        auth = tweepy.OAuthHandler(consumerKeyEntered, consumerSecretEntered)
        auth.set_access_token(accessTokenEntered, accessTokenSecretEntered)
        api = tweepy.API(auth)
        startButton.pack()




getValuesButton = Tkinter.Button(gui, text="Set API Information", command = getValues)
getValuesButton.pack()


if os.path.exists("quotes.txt"):
    append_write_quotes = 'r+'
else:
    append_write_quotes = 'w+'
    open("quotes.txt", append_write_quotes)

if os.path.exists("newquotes.txt"):
    append_write_quotes = 'r+'
else:
    append_write_quotes = 'w+'
    open("newquotes.txt", append_write_quotes)


###Here I am checking to see if the program has been running before. If that is the case
###Then the file that has delete the previous tweets should be used to eliminate duplicate tweets
##if os.stat("newquotes.txt").st_size == 0:
##    f = "quotes.txt"
##    print("getting first list")
##else:
##    f = "newquotes.txt"
##
##
##with open(f, append_write_quotes) as f:
##    mylist = f.read().splitlines()
##
##print mylist

#add some hastags to the post so people can find it
hashtags = "#inspirational #quote #inspire #android #encouragement #thought #motivation"





##quitButton = Tkinter.Button(gui, text="Quit", command = gui)
##quitButton.pack()


gui.mainloop()


#tweetit()


#api.update_status(tweet)
