from fastapi import FastAPI
from scrape_linkedin import ProfileScraper
from selenium import webdriver
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

    return profile_info
