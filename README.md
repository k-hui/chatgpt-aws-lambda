# ChatGPT with AWS Lambda

## Getting Started

### Create a new virtual environment

```bash
python -m venv venv
venv/bin/activate
```

### Install the requirements

```bash
pip install -r requirements.txt
```

### Make a copy of the example environment variables file

```bash
cp .env.example .env
```

### Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file

### Run the app

```bash
uvicorn main:app --reload
```

# FastAPI Installation

```bash
pip install fastapi
pip install "uvicorn[standard]"
pip install mangum

sls plugin install -n serverless-python-requirements
```

### Run the api server

```bash
# without serverless  offline
uvicorn main:app --reload
# with serverless offline
sls offline --noPrependStageInUrl
```
