import os
import openai
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

app = FastAPI()


class ChatModel(BaseModel):
    model: Union[str, None] = 'text-davinci-003'
    prompt: str
    temperature: Union[float, None] = 0.7


@app.get('/')
async def root():
    return {'version': '1.0.0'}


@app.post('/')
async def chat(model: ChatModel):
    print(model)
    response = openai.Completion.create(
        model=model.model,
        prompt=model.prompt,
        temperature=model.temperature
    )
    result = response.choices[0].text
    return {'result': result}


# Wrapper for lambda
handler = Mangum(app)
