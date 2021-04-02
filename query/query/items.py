# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuestionItem(scrapy.Item):
    # define the fields for your item here likes
    summary = scrapy.Field()
    # body = scrapy.Field()
    tags = scrapy.Field()
    quesId = scrapy.Field()
    ownerId = scrapy.Field()
    views = scrapy.Field()
    answers = scrapy.Field()
    votes = scrapy.Field()

class AnswerItem(scrapy.Item):
    ansId = scrapy.Field()
    ownerId = scrapy.Field()
    tags = scrapy.Field()
    answer = scrapy.Field()


