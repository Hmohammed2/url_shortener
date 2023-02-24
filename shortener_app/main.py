# shortener_app.main.py

import validators
from fastapi import FastAPI, HTTPException
from . import schemas

app = FastAPI()

# Raises status_code 400 when provided url does not exist
def raise_bad_exceptions(message):
    return HTTPException(status_code=400, detail=message)

@app.post("/url")
def create_url(url:schemas.URLBase):
    # check to see if url is valid with the validators package
    if not validators.url(url.target_url):
        raise_bad_exceptions(f"provided URL is not valid!")
    return f"TODO: return database entry for {url.target_url}"