import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os
import playsound
import time
import requests
from playsound import playsound
import msvcrt as m
import pyjokes
from email.message import EmailMessage
import smtplib
import pywhatkit as kit
import requests


def wait():
    m.getch()

engine=pyttsx3.init()
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
    url= f'https://timesles.com/en/calendar/weeks/days/today/'
    wb.get().open(url)
    speak('This is the date today')

def send_email(receiver_address, subject, message):
    EMAIL = "pothuchandana510@gmail.com"
    PASSWORD = "qsromvewubkirtqy"
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email["Subject"] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False

def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)

def get_latest_news():
    news_headlines = []
    NEWS_API_KEY = '99c43d99c03942cda00e95403dfd0ee2'
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general"

    res = requests.get(url).json()
    if res['status'] == 'ok':
        articles = res["articles"]

        for article in articles:
            news_headlines.append(article["title"])
    else:
        print("Error fetching news headlines:", res.get('message'))
    return news_headlines[:5]

def get_trending_movies():
    trending_movies = []
    TMDB_API_KEY = '18e51278a7cac9bd52ac4b6988e61526'
    res = requests.get(f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
    results = res["results"]
    
    for r in results:
        trending_movies.append(r["original_title"])
    
    return trending_movies[:5]

def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']


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

internetstatus=0
url = "https://www.google.com/"
timeout = 1.5
try:
	request = requests.get(url, timeout=timeout)
	internetstatus=1
except (requests.ConnectionError, requests.Timeout) as exception:
	internetstatus=2

def command():
    if internetstatus==1:
        print(' ')
        print('Listening . . .')
        print(' ')
        c=sr.Recognizer()
        with sr.Microphone() as source:
            c.pause_threshold=1
            audio=c.listen(source,phrase_time_limit=5)
        try:
            query = c.recognize_google(audio,language='en-US')#en-US #vi
            print('Boss: ' + query)
        except sr.UnknownValueError:
            print('Sorry, I did\'t get that. :( Try typing the command, (tips: type 10 instead of "ten") ')
            query = str(input('your favor is: '))
        return query
    if internetstatus==2:
        print('No internet! If your pc have connected to the internet, type: internet')
        print('Or if your pc have not connected to the internet,')
        query = str(input('Try typing your command: '))
        return query


def init_online_module_of_Assistant():
    os.system('cls')
    speak('successfully switch to online mode')
    playsound('assets/PTNK-on.mp3')
    welcome()
    while True:
        query=command().lower()
        if "map" in query:
            os.system('cls')
            print('Boss: ' + query)
            url = f'https://www.google.com/maps/'
            wb.get().open(url)
            speak(f'This is google maps')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')

        elif "hello" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak(f'Hello my boss')
            speak(f'How can I help you now boss?')

        elif "how are you" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak(f'I am feeling good today. Thank you')
            speak(f'How can I help you now boss?')

        elif "maps" in query:
            os.system('cls')
            print('Boss: ' + query)
            url = f'https://www.google.com/maps/'
            wb.get().open(url)
            speak(f'This is google maps')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')

        elif "globe" in query: #all global or globe returns to this code
            os.system('cls')
            print('Boss: ' + query)
            url = f'https://earth.google.com/web/@16.24291914,105.7762962,-1110.77003945a,12946843.60659599d,35y,0h,0t,0r'
            wb.get().open(url)
            speak(f'This is google earth')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')

        elif "earth" in query:
            os.system('cls')
            print('Boss: ' + query)
            url = f'https://earth.google.com/web/@16.24291914,105.7762962,-1110.77003945a,12946843.60659599d,35y,0h,0t,0r'
            wb.get().open(url)
            speak(f'This is google earth')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')

        elif 'translate' in query:
            os.system('cls')
            print('Boss: ' + query)
            url=f'https://www.dict.cc/'
            wb.get().open(url)
            speak(f'This is german-english dictionary.')
            url2=f'https://jdict.net/'
            speak('...')
            speak('...')
            wb.get().open(url2)
            speak('this is Japanese-Vietnamese dictionary.')
            speak('...')
            url3=f'https://translate.google.com/'
            speak('...')
            wb.get().open(url3)
            speak('this is google translate.')
            url4=f'https://www.oxfordlearnersdictionaries.com/'
            speak('...')
            speak('...')
            wb.get().open(url4)
            speak(' and this is Oxford dictionary')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')
        
        elif 'google' in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('What should I search now boss?')
            search=command().lower()
            url=f'https://www.google.com/search?q={search}'
            wb.get().open(url)
            speak(f'I found something on Google for your search:')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')
        elif 'weather' in query: 
            os.system('cls')
            print('Boss: ' + query)
            url=f'https://www.google.com/search?q=weather'
            wb.get().open(url)
            speak(f'This is your local weather!')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')

        elif 'climate' in query: 
            os.system('cls')
            print('Boss: ' + query)
            url=f'https://www.google.com/search?q=weather'
            wb.get().open(url)
            speak(f'This is your local weather!')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')

        elif 'type' in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('Which language do you want to type?')
            search=command().lower()
            if 'english' in search:
                url=f'https://10fastfingers.com/typing-test/english'
                wb.get().open(url)
                speak(f'Try your best with this English typing test!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                wait()
                speak(f'what else you would like me to do, boss?')

        elif 'search' in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('What should I search now boss?')
            search=command().lower()
            url=f'https://www.google.com/search?q={search}'
            wb.get().open(url)
            speak(f'I found something on Web for your search:')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')

        elif 'joke' in query:
            os.system('cls')
            print('Boss: ' + query)
            get = pyjokes.get_joke()
            speak(f'Here is a Joke for you boss!')
            speak(get)
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')

        elif "send an email" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak("To which email address should I send it? Please enter it in the console.")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject?")
            subject = command().capitalize()
            speak("What is the message?")
            message = command().capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email.")
            else:
                speak("Something went wrong while I was sending the email. Please check the error logs.")

            speak("What else would you like me to do?")

        elif "send whatsapp message" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = command().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")
            speak("What else would you like me to do?")

        elif 'news' in query:
            os.system('cls')
            print('Boss: ' + query)
            speak(f"I'm reading out the latest news headlines, sir")
            news_headlines = get_latest_news()
            for headline in news_headlines:
                print(headline)
                print("For your convenience, I am printing it on the screen, sir.")
                speak(" ".join(news_headlines))
                print(*news_headlines, sep='\n')
            speak("What else would you like me to do?")

        elif "trending movies" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak(f"Some of the trending movies are: {get_trending_movies()}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_trending_movies(), sep='\n')
            speak("What else would you like me to do?")

        elif "advice" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_random_advice(), sep='\n')
            speak("What else would you like me to do?")

        elif 'web' in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('What should I search now boss?')
            search=command().lower()
            url=f'https://www.google.com/search?q={search}'
            wb.get().open(url)
            speak(f'I found something on Web for your search:')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')

        elif 'facebook' in query:
            os.system('cls')
            print('Boss: ' + query)
            url=f'https://www.facebook.com/'
            wb.get().open(url)
            speak(f'This is facebook for you')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')
            
        elif 'twitter' in query:
            os.system('cls')
            print('Boss: ' + query)
            url=f'https://twitter.com/'
            wb.get().open(url)
            speak(f'This is twitter for you')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')
            
        elif 'browser' in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('What should I search now boss?')
            search=command().lower()
            url=f'https://www.google.com/search?q={search}'
            wb.get().open(url)
            speak(f'I found something on Web for your search:')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')

        elif "youtube" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('What should I search on youtube now boss?')
            search=command().lower()
            url = f'https://youtube.com/search?q={search}'
            wb.get().open(url)
            speak(f'I found something on Youtube for your search:')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')
        
        elif "quit" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak("Assistant is off. Goodbye boss")
            playsound('assets/Windows Notify Calendar.wav')
            quit()
        elif "stop" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak("Assistant is off. Goodbye boss")
            playsound('assets/Windows Notify Calendar.wav')
            quit()
        elif "bye" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak("Assistant is off. Goodbye boss")
            playsound('assets/Windows Notify Calendar.wav')
            quit()
        elif "see you later" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak("Assistant is off. Goodbye boss")
            playsound('assets/Windows Notify Calendar.wav')
            quit()

        elif "see you" in query:
            os.system('cls')
            print('Boss: ' + query)
            speak("Assistant is off. Goodbye boss")
            playsound('assets/Windows Notify Calendar.wav')
            quit()

        elif 'time' in query:
            os.system('cls')
            print('Boss: ' + query)
            time()
            speak(f'what else you would like me to do, boss?')
        elif 'clock' in query:
            os.system('cls')
            print('Boss: ' + query)
            time()
            speak(f'what else you would like me to do, boss?')

        elif 'date' in query:
            os.system('cls')
            print('Boss: ' + query)
            date()
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')
        elif 'day' in query:
            os.system('cls')
            print('Boss: ' + query)
            date()
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')
        

        elif 'month' in query:
            os.system('cls')
            print('Boss: ' + query)
            date()
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')

        elif 'year' in query:
            os.system('cls')
            print('Boss: ' + query)
            date()
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak(f'what else you would like me to do, boss?')

        elif 'you can' in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('I can tell you the time and weather.')
            speak('I also can open browser or youtube.')
            speak('In addition, I can open some review tests for your grade.')
            speak('Besides, I can open a typing test with english')
            speak('I can open translator, google maps and google earth too!')
            speak('So, what would you like me to do now boss?')
        elif 'ability' in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('I can tell you the time and weather.')
            speak('I also can open browser or youtube.')
            speak('In addition, I can open some review tests for your grade.')
            speak('Besides, I can open a typing test with many languages supported')
            speak('I can open translator, google maps and google earth too!')
            speak('So, what would you like me to do now boss?')
            
        elif 'function' in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('I can tell you the time and weather.')
            speak('I also can open browser or youtube.')
            speak('In addition, I can open some review tests for your grade.')
            speak('Besides, I can open a typing test with many languages supported')
            speak('I can open translator, google maps and google earth too!')
            speak('So, what would you like me to do now boss?')

        elif 'create you' in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('Batch 9  created me. How can I help you now, boss?')
        elif 'created you' in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('Batch 9 created me. How can I help you now, boss?')
        elif 'made you' in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('Batch 9 created me. How can I help you now, boss?')
        elif 'make you' in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('Batch 9 created me. How can I help you now, boss?')
        elif 'help' in query: 
            os.system('cls')
            print('Boss: ' + query)
            speak('This is the instruction')
            os.startfile('instruction.docx')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak('So, what would you like me to do now boss?')
        elif 'instruct' in query: 
            os.system('cls')
            print('Boss: ' + query)
            speak('This is the instruction')
            os.startfile('instruction.docx')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak('So, what would you like me to do now boss?')
        elif 'how to use' in query: 
            os.system('cls')
            print('Boss: ' + query)
            speak('This is the instruction')
            os.startfile('instruction.docx')
            speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
            wait()
            speak('So, what would you like me to do now boss?')


        elif 'relax' in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('Do you want to listen to music or play a game?')
            search=command().lower()
            if 'music' in search:
                speak('Hope you enjoy!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                os.startfile('chill songs.mp3')
                wait()
                speak(f'what else you would like me to do, boss?')
                
            elif 'song' in search:
                speak('Hope you enjoy!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                os.startfile('chill songs.mp3')
                wait()
                speak(f'what else you would like me to do, boss?')
                
            elif 'game' in search:
                speak('Hope you enjoy!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                os.startfile('ball.exe')
                wait()
                speak(f'what else you would like me to do, boss?')
            
        elif 'stress' in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('Do you want to listen to music or play a game?')
            search=command().lower()
            if 'music' in search:
                speak('Hope you enjoy!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                os.startfile('chill songs.mp3')
                wait()
                speak(f'what else you would like me to do, boss?')
                
            elif 'song' in search:
                speak('Hope you enjoy!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                os.startfile('chill songs.mp3')
                wait()
                speak(f'what else you would like me to do, boss?')
            elif 'game' in search:
                speak('Hope you enjoy!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                os.startfile('ball.exe')
                wait()
                speak(f'what else you would like me to do, boss?')

        elif 'hang out' in query:
            os.system('cls')
            print('Boss: ' + query)
            speak('Do you want to listen to music or play a game?')
            search=command().lower()
            if 'music' in search:
                speak('Hope you enjoy!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                os.startfile('chill songs.mp3')
                wait()
                speak(f'what else you would like me to do, boss?')
                
            elif 'song' in search:
                speak('Hope you enjoy!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                os.startfile('chill songs.mp3')
                wait()
                speak(f'what else you would like me to do, boss?')
                
            elif 'game' in search:
                speak('Hope you enjoy!')
                speak('Assistant is paused. You can later click on me and press any key on keyboard to resume me')
                os.startfile('ball.exe')
                wait()
                speak(f'what else you would like me to do, boss?')


if __name__ =='__main__':
    init_online_module_of_Assistant()