import os
import openai
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

app = FastAPI()


@app.get('/')
async def root():
    prompt = 'Hello, how are you today?'
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        temperature=0.7,
    )
    result = response.choices[0].text
    return {'result': result}
