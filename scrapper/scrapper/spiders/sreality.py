import scrapy

from scrapper.items import PropertyItem


class SrealitySpider(scrapy.Spider):
    name = "sreality"
    allowed_domains = ["sreality.cz"]
    start_urls = [
        f"https://sreality.cz/en/search/for-sale/apartments?page={page}"
        for page in range(1, 27)
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                meta={"playwright": True},
            )

    def parse(self, response):
        property_item = PropertyItem()
        for property in response.css("div.property"):
            property_item["name"] = property.css("span.name::text").get()
            property_item["locality"] = property.css("span.locality::text").get()
            property_item["price"] = property.css("span.norm-price::text").get()
            property_item["image_url"] = property.css("img").xpath("@src").get()
            yield property_item
