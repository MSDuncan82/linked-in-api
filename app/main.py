from fastapi import FastAPI
from scrape_linkedin import ProfileScraper
from selenium import webdriver
from mongo_exec import upload_profile
from pymongo import MongoClient
import dotenv

dotenv.load_dotenv()

def scrape_user(user_id):
    """
    Scrape a user
    """
    with ProfileScraper() as scraper:
        profile = scraper.scrape(user=user_id)

    return profile.to_dict()

app = FastAPI()

@app.get("/profile/{user_id}")
def read_item(user_id: str):

    profile_info = scrape_user(user_id)

    upload_profile(user_id, profile_info)

    return profile_info

@app.get("/connections")
def list_connections():

    # host = 'localhost'
    host = 'mongo'
    client = MongoClient(f'mongodb://{host}:27017')

    db = client.connections
    col = db['connections']

    results = col.find({})

    return [x for x in results]
