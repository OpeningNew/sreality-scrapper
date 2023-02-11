# Luxonis - test task

## Original task

Use scrapy framework to scrape the first 500 items (title, image url) from sreality.cz (flats, sell) and save it in the Postgresql database. Implement a simple HTTP server in python and show these 500 items on a simple page (title and image) and put everything to single docker-compose command so that I can just run "docker-compose up" in the Github repository and see the scraped ads on <http://127.0.0.1:8080> page.

## How to run

```bash
docker-compose up -d
```

Then open http://127.0.0.1:8080. It will be empty at first, just wait till scraper starts filling database.
