import smtplib
import time
import datetime
import praw
import configv2

#Program opens a file and sends every hour a line in that file to a phonenumber via sms
def smssender(strip): #Makes a function called smssender to run code
    #print("smssender start") #DEBUG Let me know when it started
    #print(strip)# DEBUG LINE Made sure line was getting what was needed
    server=smtplib.SMTP("smtp.gmail.com",587) #Defines connection to a gmail server which can send text
    server.starttls() #Connects to a server to send text
    server.login(configv2.sender_email, configv2.sender_email_pass) #Login information to that server
    server.sendmail(configv2.sender_num,configv2.reciever_num,strip) #send a sms through the server from this number, to this number on this cell service, with this message 
    #server.sendmail(configv2.DEBUG_num_sender , configv2.DEBUG_num_reciever , strip) #DEBUG Sends text to me so I can check result
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
    r=praw.Reddit(username = configv2.username, #Logs into reddit using these criteria so a bot account can read through post made on the website
                password = configv2.password,
                client_id = configv2.client_id,
                client_secret=configv2.client_secret,
                user_agent = configv2.agent)
    #print ("Logged in!") #DEBUG Let's me know when the program finished loginin
    return r #This is the output of this function, so it is basically just the bot

def run_dog_bot(r,quantity,subreddit):
    submissions = r.subreddit(subreddit).top('day', limit=quantity) #Makes a list of quantity submissions from a subreddit and those submissions are the top for the day
    for item in submissions: #For each item in the list do these things
        url=item.shortlink #Takes the item from the list of submissions and shortens the url
        #print(url) #DEBUG Test to see if it got the url
        stripper(url) #Sends the URL to Stripper function

def main():
    #print("main") #DEBUG told me main is running
    r=bot_login() #runs bot_login and assigns the value to r
    quantity=int(input("Please input the number of dog pictures you would like to send: "))
    x=0 #Assigns 1 to x
    z=['dogpictures','PuppySmiles','corgi','lookatmydog','chihuahua','roughcollies','airedaleterrier','beagle','bernesemountaindogs','BrittanySpaniel','Bulldogs','dogswearinghats','EnglishSetter','germanshepherds','greatpyrenees','Greyhounds','Maltese','pitbulls','pug','AmericanBully']
    #print(len(z))#DEBUG check length of array z
    while x!=-1: #While x does not equal 1 run this
        hour_clock=int(time.strftime("%H",time.localtime()))#Pull the hour of the local time and make it an int
        if hour_clock>=7 and hour_clock<=22:#if the hour is between 07 and 22 then run this
            if x>=len(z):#if x greater than the length of array z then do this
                x=0
            run_dog_bot(r,quantity,z[x])
            x=x+1
            if x>=len(z):#if x greater than the length of array z then do this
                x=0
            run_dog_bot(r,quantity,z[x])
            x=x+1
            time.sleep(3600) #Puts the program to sleep for 3600 seconds or 60 minutes or 1 hour
        else:
            print(x)
            time.sleep(900) #Puts the program to sleep for 900 seconds or 15 minutes if condition above isn't meet

main()
#TO DO
    #convert code to work on Rasberry Pi
        #y value texted to user when changed
        #y should be changed by 2 buttons (-2,+2)
            #y should not go below 2 or above 10 (1 picture per subreddit to 5 per sub)
        #Start on power up
    #Need to implement threading to run function to change y variable

