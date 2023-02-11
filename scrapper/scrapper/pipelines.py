# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import psycopg2


class ScrapperPipeline:
    def __init__(self) -> None:
        self.connection = psycopg2.connect(
            host="database",
            user="postgres",
            password="supersecretpassword",
            dbname="postgres",
        )
        self.cur = self.connection.cursor()

        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS properties(
                id serial PRIMARY KEY, 
                name text,
                locality text,
                price text,
                image_url text
            )
            """
        )

    def process_item(self, item, spider):
        self.cur.execute(
            "insert into properties (name, locality, price, image_url) values (%s,%s,%s,%s)",
            (item["name"], str(item["locality"]), item["price"], item["image_url"]),
        )
        self.connection.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()
