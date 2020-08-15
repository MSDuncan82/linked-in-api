#!/bin/bash

docker build --no-cache -t linkedin_scraper . && docker run -d --name linkedin_scraper -p 80:80 -p 27017:27017 linkedin_scraper