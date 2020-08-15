#!/bin/bash

docker build --no-cache -t linkedin_scraper . && docker run -d --name linkedin_scraper -p 80:80 -p 27020:27020 linkedin_scraper