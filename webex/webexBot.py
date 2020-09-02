import os
import requests
from webexteamsbot import TeamsBot
from webexteamsbot.models import Response
import sys
import json
from configparser import SafeConfigParser
from apscheduler.scheduler import Scheduler  
from datetime import date
import operator

cron = Scheduler(daemon=True)
cron.start()

os.system("curl  http://localhost:4040/api/tunnels > tunnels.json")
with open('tunnels.json') as data_file:    
    datajson = json.load(data_file)
# print (datajson['tunnels'][0]['public_url'])

parser = SafeConfigParser()
parser.read('config.ini')

#Take inputs from config.ini file
bot_url = datajson['tunnels'][0]['public_url']
bot_email = parser.get('bot_details', 'TEAMS_BOT_EMAIL')
teams_token = parser.get('bot_details', 'TEAMS_BOT_TOKEN')
bot_app_name = parser.get('bot_details', 'TEAMS_BOT_APP_NAME')
URL=parser.get('url', 'url')

# If any of the bot environment variables are missing, terminate the app
if not bot_email or not teams_token or not bot_url or not bot_app_name:
    print("Checking the config file")
    if not bot_email:
        print("TEAMS_BOT_EMAIL")
    if not teams_token:
        print("TEAMS_BOT_TOKEN")
    if not bot_url:
        print("TEAMS_BOT_URL")
    if not bot_app_name:
        print("TEAMS_BOT_APP_NAME")
    sys.exit()

# Example: How to limit the approved Webex Teams accounts for interaction
#          Also uncomment the parameter in the instantiation of the new bot
# List of email accounts of approved users to talk with the bot
# approved_users = [
#     "josmith@demo.local",
# ]

# Create a Bot Object
#   Note: debug mode prints out more details about processing to terminal
#   Note: the `approved_users=approved_users` line commented out and shown as reference
bot = TeamsBot(
    bot_app_name,
    teams_bot_token=teams_token,
    teams_bot_url=bot_url,
    teams_bot_email=bot_email,
    debug=True,
    # approved_users=approved_users,
    webhook_resource="memberships",
    webhook_resource_event=[
        {"resource": "messages", "event": "created"},
        {"resource": "attachmentActions", "event": "created"},
        {"resource": "memberships", "event": "created"},
    ],
)


def load_allowedusers():
    print("load users here")

registeredusers={}
def load_registeredusers():
    r = requests.post(URL+'registered')
    global registeredusers
    try:
        registeredusers=json.loads(r.text)
    except:
        print("some issue")

def inform_birthday():
    headers = {
        "content-type": "application/json; charset=utf-8",
        "authorization": "Bearer " + teams_token,
    }
    # msgtxt="Don't forget to take break and spend some time away from the screen"
    # url ="https://webexapis.com/v1/messages"
    # msgfile=["https://barrister-suites.com/wp-content/uploads/2016/06/BarristerSuites-TakingBreaks.jpg"]
    # for rid in registeredusers.values():
    #     print(rid)
    #     data = {"roomId": rid, "markdown": msgtxt,"files": msgfile}
    #     response = requests.post(url, json=data, headers=headers)
    # return "done"
    r = requests.get(URL+'upcomingbirthdays')
    data = json.loads(r.text)
cron.add_cron_job(inform_birthday, second='50')


def inform_break():
    headers = {
        "content-type": "application/json; charset=utf-8",
        "authorization": "Bearer " + teams_token,
    }
    msgtxt="Don't forget to take break and spend some time away from the screen"
    url ="https://webexapis.com/v1/messages"
    msgfile=["https://barrister-suites.com/wp-content/uploads/2016/06/BarristerSuites-TakingBreaks.jpg"]
    for rid in registeredusers.values():
        print(rid)
        data = {"roomId": rid, "markdown": msgtxt,"files": msgfile}
        response = requests.post(url, json=data, headers=headers)
    return "done"
cron.add_cron_job(inform_break, hour='10-18',minute="50")



def checkregistereduser(name,id):
    if name in registeredusers:
        print("already registered")
    else:
        data = {'name':name,'id':id} 
        r = requests.post(URL+'register',data=data)
        registeredusers[name]=id

# Create a custom bot greeting function returned when no command is given.
# The default behavior of the bot is to return the '/help' command response
def greeting(incoming_msg):
    # Loopkup details about sender
    sender = bot.teams.people.get(incoming_msg.personId)

    # Create a Response object and craft a reply in Markdown.
    response = Response()
    response.markdown = "Hello {}, I'm a chat bot.  \n".format(sender.displayName)
    response.markdown += "You can use:  \n /holidays : To list the manditory holidays  \n /floaters : To list the floaters  \n /helpdesk : To get helpdesk contact"
    return response

def listfloaters(incoming_msg):
    r = requests.get(URL+'listfloaters')
    data = json.loads(r.text)
    response = Response()
    response.text=""
    sorted_d = dict(sorted(data.items(), key=operator.itemgetter(1),reverse=True))
    for x in sorted_d.keys():
        response.text = data[x]+" "+x+'\n'+response.text
    return response

def listholidays(incoming_msg):
    r = requests.get(URL+'listholidays')
    data = json.loads(r.text)
    response = Response()
    response.text=""
    sorted_d = dict(sorted(data.items(), key=operator.itemgetter(1),reverse=True))
    for x in sorted_d.keys():
        response.text = data[x]+" "+x+'\n'+response.text
    return response

def listbirthdays(incoming_msg):
    r = requests.get(URL+'listbirthdays')
    data = json.loads(r.text)
    response = Response()
    response.text=""
    for x in data.keys():
        response.text = x+" Birthday is  "+data[x][0]+" and team members are" +data[x][1] +'\n'+response.text
    return response

def listhelpdeskemployees(incoming_msg):
    r = requests.get(URL+'listhelpdeskemployees')
    data = json.loads(r.text)
    response = Response()
    response.text=""
    for x in data.keys():
        response.text += "Email : "+ data[x][0] +" Contact Number:  " +data[x][1] +" Name : " + x +'\n'
    return response


# An example using a Response object.  Response objects allow more complex
# replies including sending files, html, markdown, or text. Rsponse objects
# can also set a roomId to send response to a different room from where
# incoming message was recieved.
def ret_message(incoming_msg):
    checkregistereduser(incoming_msg.personEmail,incoming_msg.roomId)
    # Create a object to create a reply.
    response = Response()
    response.text = "Happy birthday and have a nice day."
    response.files = "https://thumbs.dreamstime.com/b/happy-birthday-cheerful-colleagues-office-congratulate-vector-full-color-graphics-cute-characters-156278742.jpg"
    # response.files = "https://static.officeholidays.com/images/1280x853c/india-flag-01.jpg"
    return response

def memberadded(api, incoming_msg):
    print(incoming_msg)
    response = Response()

    # Set the text of the reply.
    response.text = "Hi "+((incoming_msg['data'])['personDisplayName'])+". On behalf of all of us, welcome onboard! We believe you will be a terrific asset to our team, and we look forward to your input! We are so excited about having you on our team!"
    return response

# Set the bot greeting.
bot.set_greeting(greeting)

# Add new commands to the bot.
bot.add_command("/demo", "Sample that creates a Teams message to be returned.", ret_message)
bot.add_command('memberships', '*', memberadded)
bot.add_command("/floaters", "List floaters .", listfloaters)
bot.add_command("/listbirthdays", "List Birthdays .", listbirthdays)
bot.add_command("/holidays", "List Holidays .", listholidays)
bot.add_command("/helpdesk", "List HelpDeskEMployees .", listhelpdeskemployees)
# Every bot includes a default "/echo" command.  You can remove it, or any other command with the remove_command(command) method.
bot.remove_command("/echo")
bot.remove_command("/help")


if __name__ == "__main__":
    load_allowedusers()
    load_registeredusers()
    bot.run(host="0.0.0.0", port=5000)
