from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
import re
import random
import pygame
from pygame import mixer
import time
from time import ctime
import forecastio
from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("Jarvis")


def say(audio):
    "speaks audio passed as argument"
    print(audio)
    for line in audio.splitlines():   
    #  use the system's inbuilt say command instead of mpg123
       tts = gTTS(text=audio, lang='en')
       pygame.mixer.init(28000, -8,2,8000)
       mixer.music.load('blank.mp3')
       tts.save("audio.mp3")
       mixer.music.load('audio.mp3')
       mixer.music.play()



def myCommand():
    "listens for commands"

def reflect(fragment):
    tokens = fragment.lower().split()
    for i, token in enumerate(tokens):
        if token in reflections:
            tokens[i] = reflections[token]
    return ' '.join(tokens)
 
 
def analyze(statement):
    ''' Write code which matches responses with all patterns given'''
    for pattern, responses in psychobabble:
    match = re.match(pattern, statement.rstrip(".!"))
    if match:
        response = random.choice(responses)
        return response.format(*[reflect(g) for g in match.groups()])



def assistant(command):
    '''if statements for executing commands, add as many commands as you like'''

    if 'open' in command:

      if 'C drive' in command:
        os.startfile('C:\\') 
        say('Done!')

      if 'D drive' in command:
        os.startfile('D:\\') 
        say('Done!')
        
      if 'quora' in command:
        webbrowser.open('www.quora.com')
        say('Done!')
        
      if 'facebook' in command:
        webbrowser.open('www.facebook.com')
        say('Done!')

      if 'reddit' in command:
         reg_ex = re.search('open reddit (.*)', command)
         url = 'https://www.reddit.com/'
         if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
         webbrowser.open(url)
         say('Done!')

      if '.com' in command:
        sf=re.split('\\bopen \\b',command)[-1]
        greet='I have opened '+sf
        say(greet)
        webbrowser.open('www.'+sf)
       
        
      else:
        sf=re.split('\\bopen\\b',command)[-1]
        greet='I have opened '+sf
        say(greet)
        os.system('start'+ sf)
        


    elif 'quit' in command:
    	exit()

    elif "time" in command:
        say(ctime())


    elif 'what up' in command:
        say('Just doing my thing')
    elif 'joke' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            say(str(res.json()['joke']))
        else:
            say('oops!I ran out of jokes')

    elif "where is" in command:
        data = re.split('\\bis \\b',command)[-1]
        l2=data
        location = data.replace(' ','+')
        mixer.music.load('blank.mp3')
        say("Hold on, I will show you where   " + l2 + " is.")
        webbrowser.open('https://www.google.nl/maps/place/' + location + '/&amp;')
        time.sleep(4)
       
    else:
        response = chatbot.get_response(command)
        answer=str(response)
        say(answer)
        



say('I am ready for your command..')

#loop to continue executing multiple commands
while True:
    assistant(myCommand())
