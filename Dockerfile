FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN pip install python-dotenv pymongo selenium git+git://github.com/MSDuncan82/scrape-linkedin-selenium.git

ADD install_chromedriver.sh /

RUN /install_chromedriver.sh

COPY ./app /app