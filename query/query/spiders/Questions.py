import scrapy
from ..items import QuestionItem


class Questions(scrapy.Spider):

    name = "answered_questions"
    pages = 1

    start_urls = [
        "https://stackoverflow.com/questions?tab=votes&page=1"
    ]

    def parse(self, response):

        links = response.css("a.question-hyperlink::attr(href)").extract()
        allQuestions = []
        # questions = []
        for link in links:
            if(link[0]=="/"):
                next_ques = "https://stackoverflow.com" + link
            else:
                next_ques = link
            req = scrapy.Request(url=next_ques, callback = self.send_request)
            req.meta['data'] = ""
            yield req
        
        next_page = "https://stackoverflow.com/questions?tab=votes&page=" + str(Questions.pages)
        if(Questions.pages <= 1000):
            Questions.pages += 1
            yield response.follow(next_page, callback = self.parse)
        

    def send_request(self, response):
        data = response.meta.get('data')

        question = QuestionItem()
        summary = response.css("div#question-header h1 a.question-hyperlink::text").extract_first()
        body = response.xpath('string(//*[contains(concat( " ", @class, " " ), concat( " ", "s-prose", " " ))])').get()
        quesId = response.css("div.question::attr(data-questionid)").extract_first()
        tags = response.css("div.post-taglist a::text").extract()
        ownerId = response.css("div.question::attr(data-ownerid)").extract_first()
        votes = response.css("div.question::attr(data-score)").extract_first()
        if(votes is not None):
            votes = int(votes)
        answers = response.css("div#answers-header h2::attr(data-answercount)").extract_first()
        if(answers is not None):
            answers = int(answers)
        views = response.css("div.question div.js-vote-count ::attr(data-value)").extract_first()
        if(views is not None):
            views = int(views)


        question['summary'] = summary
        question['quesId'] = quesId
        question['ownerId'] = ownerId
        question['tags'] = tags
        question['votes'] = votes
        question['views']  = views
        question['answers']  = answers 
        # question['body'] = body

        yield question

        
