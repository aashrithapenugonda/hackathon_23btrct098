import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import logging
import random
import sys
import time
import requests
import pywhatkit as kit
import psutil
import re
import pyjokes
import math
import wikipedia
import smtplib
from email.message import EmailMessage

# Set up logging
logging.basicConfig(filename='assistant.log', level=logging.ERROR, 
                    format='%(asctime)s:%(levelname)s:%(message)s')


class VirtualAssistant:
    def __init__(self, name="Assistant"):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1.0)
        
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)

        self.recognizer = sr.Recognizer()
        self.logger = logging.getLogger(__name__)
        self.name = name

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def get_input(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        try:
            try:
                command = self.recognizer.recognize_google(audio)
            except Exception as e:
                self.logger.error(f"Error recognizing command: {e}")
                return "I couldn't understand. Please repeat."
            print(f"User said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            return "I couldn't understand. Please repeat."

    def calculate(self, query):
        try:
            query = query.replace('x', '*').replace('X', '*')
            result = eval(re.sub(r'[^0-9+\-*/().]', '', query))
            self.speak(f"The result is {result}")
        except Exception as e:
            self.speak("Sorry, I couldn't calculate that. Please check your input.")
            self.logger.error(f"Calculation error: {e}")

    def send_whatsapp_message(self, number, message):
        try:
            try:
                kit.sendwhatmsg_instantly(f"+{number}", message)
                self.speak(f"Sending your message to {number}")
            except Exception as e:
                self.speak(f"Failed to send message: {e}")
                self.logger.error(f"WhatsApp message sending error: {e}")
            self.speak(f"Sending your message to {number}")
        except Exception as e:
            self.speak(f"Failed to send message: {e}")

    def tell_time(self):
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        self.speak(f"The current time is {current_time}")

    def tell_joke(self):
        joke = pyjokes.get_joke()
        self.speak(joke)

    def tell_date(self):
        today = datetime.datetime.now().strftime("%A, %B %d, %Y")
        self.speak(f"Today's date is {today}")
    
    def identify_number(self, number_type):
        try:
            if "even" in number_type:
                numbers = list(range(2, 20, 2))  # Even numbers from 2 to 100
                result = f"Even numbers are: {', '.join(map(str, numbers))}"
        
            elif "odd" in number_type:
                numbers = list(range(1, 20, 2))  # Odd numbers from 1 to 99
                result = f"Odd numbers are: {', '.join(map(str, numbers))}"
        
            elif "prime" in number_type:
                primes = [n for n in range(2, 50) if all(n % i != 0 for i in range(2, int(n**0.5) + 1))]
                result = f"Prime numbers are: {', '.join(map(str, primes))}"
        
            elif "composite" in number_type:
                composites = [n for n in range(4, 20) if any(n % i == 0 for i in range(2, n))]
                result = f"Composite numbers are: {', '.join(map(str, composites))}"
        
            elif "negative" in number_type:
                numbers = list(range(-1, -10))
                result = f"Negative numbers are: {', '.join(map(str, numbers))}"
        
            elif "positive" in number_type:
                numbers = list(range(1, 10))
                result = f"Positive numbers are: {', '.join(map(str, numbers))}"
        
            elif "whole" in number_type:
                numbers = list(range(0, 10))  # Whole numbers from 0 to 100
                result = f"Whole numbers are: {', '.join(map(str, numbers))}"
        
            elif "integer" in number_type:
                numbers = list(range(-10, 10))  # Integers from -50 to 50
                result = f"Integers are: {', '.join(map(str, numbers))}"
        
            else:
                result = "I'm sorry, I couldn't identify the number type. Please say even, odd, prime, composite, etc."

            print(result)
            self.speak(result)

        except Exception as e:
            self.speak("Sorry, something went wrong. Please try again. Please ensure the input is valid.")
            self.logger.error(f"Number identification error: {e}")

    def get_weather(self):
        api_key ="b02f2b1fcf150005eee65f2d0301cc97"
        city = "bengaluru"

        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url).json()
            weather_desc = response['weather'][0]['description']
            temp = response['main']['temp']
            self.speak(f"The weather in {city} is currently {weather_desc} with a temperature of {temp} degrees Celsius.")
        except:
            self.speak("Sorry, I couldn't fetch the weather information.")
            self.logger.error("Weather fetching error")

    def tell_about_person(self, person):
        try:
            url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{person.replace(' ', '_')}"
            response = requests.get(url).json()
            summary = response.get('extract', "Sorry, I couldn't find information on that person.")
            self.speak(summary)
        except:
            self.speak("Sorry, I couldn't fetch the information.")
            self.logger.error("Wikipedia fetching error")

    def tell_battery_status(self):
        battery = psutil.sensors_battery()
        percent = battery.percent
        self.speak(f"Your battery is at {percent} percent.")

    def test_send_whatsapp(self):
        try:
            # Test sending a WhatsApp message
            kit.sendwhatmsg_instantly("+919390709805", "Hello!")
            print("Message sent successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def calculate_number_operations(self, command):
        try:
            # Extract the number from the command
            number = int(re.search(r'\d+', command).group())

            if "square root" in command:
                result = math.sqrt(number)
                self.speak(f"The square root of {number} is {result:.2f}")

            elif "square" in command:
                result = number ** 2
                self.speak(f"The square of {number} is {result}")
            
            elif "cube root" in command:
                result = round(number ** (1/3), 2)
                self.speak(f"The cube root of {number} is {result}")
            
            elif "cube" in command:
                result = number ** 3
                self.speak(f"The cube of {number} is {result}")
            
            elif "power 4" in command:
                result = number ** 4
                self.speak(f"The fourth power of {number} is {result}")
            
            elif "fourth root" in command:
                result = round(number ** (1/4), 2)
                self.speak(f"The fourth root of {number} is {result}")
            
            else:
                self.speak("Sorry, I didn't understand the calculation request.")

        except Exception as e:
            self.speak("Sorry, I couldn't calculate that.")
            self.logger.error(f"Calculation error: {e}")

    def open_google(self):
        webbrowser.open("https://www.google.com")
        self.speak("Opening Google")

    def search_google(self, query):
        webbrowser.open(f"https://www.google.com/search?q={query}")
        self.speak(f"Searching Google for {query}")

    def open_whatsapp(self):
        webbrowser.open("https://web.whatsapp.com/")
        self.speak("Opening WhatsApp")

    def open_whatsapp_and_message(self):
        contacts = {
        "dad": "9290457733", 
        "mom": "8555850543"
    }

        self.speak("Whom would you like to message?")
        contact_name = self.get_input().strip().lower()


        if contact_name in contacts:
            number = contacts[contact_name]
            self.speak(f"What message would you like to send to {contact_name}?")
            message = self.get_input()
            kit.sendwhatmsg_instantly(f"+91{number}", message)
            self.speak(f"Sending your message to {contact_name}")
        else:
            self.speak("I couldn't find that contact. Please provide the phone number.")
            number = self.get_input().replace(" ", "")
            self.speak("What message would you like to send?")
            message = self.get_input()
            kit.sendwhatmsg_instantly(f"+91{number}", message)
            self.speak(f"Sending your message to {number}")

    def open_spotify(self):
        os.system("start spotify")
        self.speak("Opening Spotify")

    def open_netflix(self):
        try:
            os.system("start shell:AppsFolder\\4DF9E0F8.Netflix_mcm4njqhnhss8!Netflix")
            self.speak("Opening Netflix app")
        except Exception as e:
            self.speak("Sorry, I couldn't open the Netflix app.")

    def open_bing(self):
        webbrowser.open("https://www.bing.com")
        self.speak("Opening Bing")

    def open_files(self):
        os.system("explorer")
        self.speak("Opening Files")

    def open_teams(self):
        os.system("start teams")
        self.speak("Opening Microsoft Teams")

    def open_calculator(self):
        os.system("calc")
        self.speak("Opening Calculator")

    def open_notepad(self):
        os.system("notepad")
        self.speak("Opening Notepad")

    def open_control_panel(self):
        os.system("control")
        self.speak("Opening Control Panel")

    def open_cmd(self):
        os.system("cmd")
        self.speak("Opening Command Prompt")

    def get_president(self, country):
        president_data = {
            "India": "Droupadi Murmu",
            "united states": "Joe Biden",
            "france": "Emmanuel Macron",
            "russia": "Vladimir Putin",
            "china": "Xi Jinping",
            "germany": "Frank-Walter Steinmeier",
            "brazil": "Luiz Inácio Lula da Silva"
        }

        if country in president_data:
            self.speak(f"The President of {country.title()} is {president_data[country]}.")
        else:
            self.speak(f"Sorry, I couldn't find the President of {country}. Try asking something else.")
    def get_news(self):
        self.speak("Opening latest news.")
        webbrowser.open("https://news.google.com/topstories")
# Traffic Conditions Function
    def get_traffic_conditions(self):

        location = input("Enter your area for traffic updates: ").strip()
        url = f"https://www.google.com/maps/search/traffic+conditions+in+{location.replace(' ', '+')}"
        webbrowser.open(url)
        self.speak(f"Showing traffic conditions in {location}.")

# Maps Navigation Function
    def show_map(self):
        location = input("Enter the place you want to locate on maps: ").strip()
        url = f"https://www.google.com/maps/search/{location.replace(' ', '+')}"
        webbrowser.open(url)
        self.speak(f"Showing location for {location} on Google Maps.")

    def get_input(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            self.speak("I couldn't understand. Please repeat.")
            return get_input()

    def send_email(self):
        try:
            sender_email = "your_email@gmail.com"
            sender_password = "your_app_password"

            self.speak("Please say the recipient's email address.")
            recipient_email = get_input().replace(" ", "").replace("at", "@").replace("dot", ".")
        
            self.speak("What should be the subject of the email?")
            subject = get_input()
        
            self.speak("Please say your message.")
            body = get_input()

            message = EmailMessage()
            message['From'] = sender_email
            message['To'] = recipient_email
            message['Subject'] = subject
            message.set_content(body)

            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.send_message(message)

            self.speak("✅ Email sent successfully!")
    
        except Exception as e:
            self.speak("❌ Failed to send email. Please try again.")
            print(f"Error: {e}")

    
    def get_capital(self, country):
        try:
            url = f"https://restcountries.com/v3.1/name/{country}"
            response = requests.get(url).json()

            if isinstance(response, list):
                data = response[0]
                capital = data.get('capital', ["I couldn't find the capital."])[0]
                self.speak(f"The capital of {country} is {capital}.")
            else:
                self.speak("Sorry, I couldn't retrieve information for that country.")
        except Exception as e:
            self.speak("Sorry, I couldn't fetch the information. Please try again.")

    def greet_user(self):
        greetings = ["Hello! How can I assist you today?", "Hey there! What can I do for you?", "Hi! How may I help you?"]
        self.speak(random.choice(greetings))

    def run(self):
        self.greet_user()
        while True:
            command = self.get_input()
            if "time" in command:
                self.tell_time()
            elif "date" in command:
                self.tell_date()
            elif "president of" in command:
                country = command.replace("president of", "").strip()
                self.get_president(country)

            elif "capital of" in command:
                country = command.replace("what is the capital of", "").strip()
                self.get_capital(country)
            elif "weather" in command:
                self.get_weather()
            elif "battery" in command or "charge" in command:
                self.tell_battery_status()
            elif "calculate" in command or "what is" in command:
                self.calculate(command)
            elif "open calculator" in command:
                self.open_calculator()
            elif "open bing " in command:
                self.open_bing()
            elif "open notepad" in command:
                self.open_notepad()
            elif "tell me a joke" in command:
                self.tell_joke()
            elif "open control panel" in command:
                self.open_control_panel()
            elif "open command prompt" in command or "open cmd" in command:
                self.open_cmd()
            elif "open spotify" in command:
                self.open_spotify()
            elif "news" in command or "latest news" in command:
                self.get_news()

            elif "traffic" in command or "road condition" in command:
                self.get_traffic_conditions()

            elif "map" in command or "show location" in command:
                self.show_map()
            elif "open netflix" in command:
                self.open_netflix()
            elif "open teams" in command:
                self.open_teams()
            elif "open files" in command:
                self.open_files()
                number = self.get_input()
            elif any(op in command for op in ["square", "square root", "cube", "cube root", "power 4", "fourth root"]):
                self.calculate_number_operations(command)
            elif "open google" in command:
                self.open_google()
            elif "send message in whatsapp" in command:
                self.test_send_whatsapp()
            elif "exit" in command or "stop" in command:
                self.speak("Goodbye! Have a great day.")
                sys.exit()
            elif "send a message to" in command:
                self.open_whatsapp_and_message()
            elif "send email" in command:
                self.send_email()

            elif "hi" in command or "hello" in command or "hey" in command:
                self.greet_user()
            elif "show" in command or "display" in command:
                self.speak("Please say the type of numbers you want to see.")
                number_type = self.get_input()
                self.identify_number(number_type)
            else:
                self.speak("I didn't understand that")

if __name__ == "__main__":
    assistant = VirtualAssistant()
    assistant.run()
