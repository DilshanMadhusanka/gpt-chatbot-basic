from openai import OpenAI  # to work with the gpt modal
import os  # to work with the local variables ( API key eka env eke hadal import krann )
from dotenv import load_dotenv  # USE THE environment varibles 


# load the environmental varibale ( API KEY)
load_dotenv()

# print the API KEY that are in the .env file 
#print( os.environ["OPENAI_API_KEY"])

# Assing the api key to varible 
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# create the object of OpenAI
client = OpenAI()

# use the object to get the response form the gpt modal 
while True:
    # get the question as input ( from user )
    question = input("User: ")

    if (question != "bye"):
        response = client.chat.completions.create(
            # Parameters of the create function( openAI library eken enne)
            model="gpt-3.5-turbo", # modal name that we use 
            messages=[{"role": "user", "content": question}], 
            max_tokens=50, # number of maximum token in the response
            n=1, # number of responce 
            temperature=0  # randomness of the responce. meke 0. e kiyanne out put eka random wen na. 
        )

        # print the response
        for choice in response.choices:
            print(f"AI: {choice.message.content}")
    else:
        print("AI: Bye...")
        break