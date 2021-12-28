import smtplib
import time
import datetime
import praw
import config

#Program opens a file and sends every hour a line in that file to a phonenumber via sms
def smssender(strip): #Makes a function called smssender to run code 
    #print("smssender start") #DEBUG Let me know when it started
    #print(strip)# DEBUG LINE Made sure line was getting what was needed
    server=smtplib.SMTP("smtp.gmail.com",587) #Defines connection to a gmail server which can send text
    server.starttls() #Connects to a server to send text
    server.login("jacksms.send@gmail.com ", "password") #Login information to that server
    server.sendmail("5617130630","7274242869 <domain of service provider>",strip) #send a sms through the server from this number, to this number on this cell service, with this message 
    #server.sendmail(x , y , strip) #DEBUG Sends text to me so I can check result
    print("done") #Prints done in text on screen so I know the code ran
    #print(strip) #DEBUG LINE makes sure line is correct is redudent

def stripper(url):
    #print("Strip Start") #DEBUG Told me function started
    #print("URL: "+url) #DEBUG Told me what the input was before going into function
    strip=url.replace("https://","") #Finds all instances of https:// and replaces it with nothing or a space
    #print("Strip: "+strip) #DEBUG Told me what the output was
    #print("strip end") #DEBUG Told me the function ended
    smssender(strip) #Sends the strip result to smssender
    
def bot_login():
    #print ("Logging in") #DEBUG let me know when the program started by printing
    r=praw.Reddit(username = config.username, #Logs into reddit using these criteria so a bot account can read through post made on the website
                password = config.password,
                client_id = config.client_id,
                client_secret=config.client_secret,
                user_agent = "Dog Picture Grabber")
    #print ("Logged in!") #DEBUG Let's me know when the program finished loginin
    return r #This is the output of this function, so it is basically just the bot

def run_bot_MassiveCock(r):
    submissions = r.subreddit('MassiveCock').top('all', limit=1) #Makes a list of 2 submissions from a subreddit and those submissions are the top for the day
    for item in submissions: #For each item in the list do these things
        url=item.shortlink #Takes the item from the list of submissions and shortens the url
        #print(url) #DEBUG Test to see if it got the url
        stripper(url) #Sends the URL to Stripper function

def main():
    #print("main") #DEBUG told me main is running
    r=bot_login() #runs bot_login and assigns the value to r
    x=1 #Assigns 0 to x
    run_bot_MassiveCock(r)


main()
#TO DO
#Switch from
