from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from diploma.instagram.spiders.instagram_hw import InstagramSpider
import os
import dotenv

if __name__ == "__main__":
    dotenv.load_dotenv(".env")
    crawler_settings = Settings()
    tags = ["climatechange","globalwarming"]
    crawler_settings.setmodule("instagram.settings")
    crawler_proc = CrawlerProcess(settings=crawler_settings)
    crawler_proc.crawl(
        InstagramSpider,
        login=os.getenv("INST_LOGIN"),
        password=os.getenv("INST_PASSWORD"),
        tags=tags,
    )
    crawler_proc.start()