Virtual Assistant using Python
This Virtual Assistant is a Python-based voice-controlled assistant capable of performing various tasks
such as:
• Telling the time, date, weather, and battery status
• Sending WhatsApp messages
• Sending emails
• Providing information about presidents and capitals of countries
• Performing arithmetic calculations
• Telling jokes
• Opening popular websites like Google, Bing, and Netflix
• Showing traffic conditions and map locations
• Identifying types of numbers (prime, odd, even, etc.)
Features
• Voice recognition and response
• Error logging for debugging
• OpenWeather API integration for weather updates
• Wikipedia API integration for person details
• Google Maps link generation for traffic updates
• PyWhatKit for instant WhatsApp messaging
Prerequisites
Before running the project, ensure you have the following installed:
• Python 3.10+
• Required libraries:
pip install pyttsx3 speechrecognition wikipedia requests pywhatkit pyjokes psutil
• Google App Password for sending emails securely. How to get one?
Installation
1. Clone the repository or copy the source code to your local machine:
git clone <repository_link>
2. Navigate to the project folder:
cd virtual_assistant
3. Install dependencies:
pip install -r requirements.txt
Usage
1. Run the assistant.py file:
python assistant.py
2. The assistant will greet you and start listening for commands.
3. Example Commands:
 "What is the time?" → Tells the current time
 "Who is the president of India?" → Provides the president's name
 "Send email" → Guides you to send an email through voice command
 "Open Netflix" → Opens Netflix
 "Show traffic in Hyderabad" → Displays traffic conditions on Google Maps
Configuration
Email Configuration
1. Enable 2-Step Verification on your Gmail account.
2. Generate an App Password and replace the following in the code:
3. sender_email = "aashrithapenugonda@gmail.com"
sender_password = "your_app_password"
OpenWeather API Configuration
1. Sign up on OpenWeather.
2. Generate your API key.
3. Use the generated key in the get_weather() method:
api_key = "b02f2b1fcf150005eee65f2d0301cc97"
Troubleshooting
• If the assistant doesn't recognize your voice clearly, try speaking slower or in a quieter
environment.
• Ensure you have an active internet connection for online features like news, weather, and
maps.
• If you face issues with sending WhatsApp messages, ensure your WhatsApp Web is logged in
and active.
Future Enhancements
• Add support for playing music directly via Spotify API.
• Improve voice recognition accuracy with better noise handling.
• Integrate more APIs for enhanced news updates and real-time alerts.
Contributing
Contributions are welcome! If you encounter bugs or have feature requests, feel free to create an
issue or submit a pull request.
License
This project is licensed under the MIT License.
Author
P.Aashritha mounika
