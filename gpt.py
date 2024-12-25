from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def GptResponse(message):
    
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional and extremely efficient email writer."},
            {
                "role": "user",
                "content": f"{message}"
            }
        ],
       
    )
    


    res = completion.choices[0].message.content
    return res
    

    

