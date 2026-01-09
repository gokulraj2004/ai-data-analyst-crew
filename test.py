# Source - https://stackoverflow.com/q
# Posted by HARSHIL PRAVEEN, modified by community. See post 'Timeline' for change history
# Retrieved 2026-01-10, License - CC BY-SA 4.0

import google.generativeai as genai

genai.configure(api_key="AIzaSyBdXPiX7DGOuP9Qzcb0OdwwLvOPSJSGJDc")
model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content("my name is gokul i am going to do project in ai")
print(response.text)
