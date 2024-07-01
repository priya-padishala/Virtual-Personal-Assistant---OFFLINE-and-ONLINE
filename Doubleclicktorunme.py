from vosk import Model, KaldiRecognizer
import pyttsx3
import datetime
import pyaudio
import json
import os
import time
import playsound
from playsound import playsound
import subprocess as sp
import msvcrt as m
def wait():
    m.getch()

engine=pyttsx3.init()  # init text to speech
voice=engine.getProperty('voices')
assistant_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0' 
engine.setProperty('voice',assistant_voice_id)

def speak(audio):
    print('Assistant: ' + audio)
    engine.say(audio)
    engine.runAndWait()


def time():
    Time=datetime.datetime.now().strftime('%I:%M: %p')
    speak('It is')
    speak(Time)

def date():
    today=datetime.datetime.now().strftime('the date today is %d %m %Y, please notice that the format is day, month, year')
    speak(today)

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)
    
def open_cmd():
    os.system('start cmd')

def welcome():
    hour=datetime.datetime.now().hour
    if hour >=3 and hour <12:
        speak('Good morning boss')
    elif hour >=12 and hour <18:
        speak('Good afternoon boss')
    elif hour >=18 and hour <21:
        speak('Good evening boss')
    elif hour >=21 and hour <24:
        speak('Good night and have a nice dream boss!')
    elif hour >=0 and hour <3:
        speak('It is late boss, let us take a nap')
    speak('How can I help you now')
    print('')
    print('listening ...')
    print('')

playsound('assets/PTNK-on.mp3') #assets/PTNK-on.mp3
model=Model("assets/model-light-with-graph")     #assets/vosk-model-en-us-0.22 ## assets/model-light-with-graph
os.system('cls')
welcome()
rec = KaldiRecognizer(model, 16000)

cap=pyaudio.PyAudio()
stream=cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)

stream.start_stream()

a=0

while True:
    data=stream.read(4000, exception_on_overflow=False)
    if len(data)==0:
        break

    if rec.AcceptWaveform(data):
        result=rec.Result()
        result=json.loads(result)
        print('Boss: ' + result['text'])
        if "hello" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak('Hello my boss, how can I help you?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "who are you" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak('Hi, I am your virtual assistant. How can I help you now, boss?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "who made you" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak('Batch 9 created me. Is there something else you need me to help you with?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "who make you" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak('Batch 9 created me. Is there something else you need me to help you with?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "who created you" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak('Batch 9 created me. Is there something else you need me to help you with?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "who create you" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak('Batch 9 created me. Is there something else you need me to help you with?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "where are you from" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak('Batch 9 created me. Is there something else you need me to help you with?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "time" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            time()
            speak(f'What else would you like me to do, boss?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "date" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            date()
            speak(f'What else would you like me to do, boss?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "music" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak(f'This is some music for you, hope you enjoy')
            os.startfile('chill songs.mp3')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'What else would you like me to do, boss?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "stress" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak(f'This is some music for you, hope you enjoy')
            os.startfile('chill songs.mp3')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'What else would you like me to do, boss?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "game" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak(f'This is a small game for you, hope you enjoy')
            os.startfile('ball.exe')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'What else would you like me do do, boss?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "relax" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak(f'This is some music for you, hope you enjoy')
            os.startfile('chill songs.mp3')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'What else would you like me do do, boss?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "help" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak(f'This is the instruction file')
            os.startfile('instruction.docx')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'What else would you like me do do, boss?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "instruct" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak(f'This is the instruction file')
            os.startfile('instruction.docx')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'What else would you like me do do, boss?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "how to use" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak(f'This is the instruction file')
            os.startfile('instruction.docx')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'What else would you like me do do, boss?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif "note" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak(f'This is notepad for sir to note')
            os.system('notepad')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me.')
            wait()
            speak(f'What else would you like me do do, boss?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif 'open calculator' in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak(f'This is calculator sir')
            os.system('C:/WINDOWS/system32/calc.exe')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me.')
            wait()
            speak(f'What else would you like me do do, boss?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif 'open camera' in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak(f'Opening Camera sir')
            open_camera()
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me.')
            wait()
            speak(f'What else would you like me do do, boss?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif 'open command prompt' in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak(f'Opening Command prompt sir')
            open_cmd()
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me.')
            wait()
            speak(f'What else would you like me do do, boss?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        elif 'alarm' in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak(f'Enter the Time!')
            time = input(": Enter the Time :")
            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")
                if now == time:
                    speak("Time to wake up sir!")
                    playsound('chill songs.mp3')
                    speak("Alarm Closed!")
                elif now>time:
                    break
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me.')
            wait()
            speak(f'What else would you like me do do, boss?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')
            

        elif "stop" in result['text']:
            speak("Assistant is off. Goodbye boss")
            playsound('assets/Windows Notify Calendar.wav')
            quit()
        elif "quit" in result['text']:
            speak("Assistant is off. Goodbye boss")
            playsound('assets/Windows Notify Calendar.wav')
            quit()
        elif "bye" in result['text']:
            speak("Assistant is off. Goodbye boss")
            playsound('assets/Windows Notify Calendar.wav')
            quit()
        elif "buy" in result['text']:
            speak("Assistant is off. Goodbye boss")
            playsound('assets/Windows Notify Calendar.wav')
            quit()
        elif "see you later" in result['text']:
            speak("Assistant is off. Goodbye boss")
            playsound('assets/Windows Notify Calendar.wav')
            quit()
        elif "enough" in result['text']:
            speak("Assistant is off. Goodbye boss")
            playsound('assets/Windows Notify Calendar.wav')
            quit()

        
        elif "online" in result['text']:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak('Switching to online mode ...')
            os.startfile('module-onl.exe')
            quit()

        else:
            os.system('cls')
            stream.stop_stream()
            print('Boss: ' + result['text'])
            speak('I am sorry. That is beyond my ability now.')
            speak('Is there anything else I can help you with?')
            stream.start_stream()
            print('')
            print('listening ...')
            print('')

        


