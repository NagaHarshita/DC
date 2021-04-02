## Set Up:
```
git clone https://github.com/NagaHarshita/DC.git
pip3 install virtualvenv
source venv/bin/activate
```
## Crawling 

Framework: scrapy 
<br/>

Collected 20k questions from stackoverflow website and stored it in a questions.csv file

```
scrapy crawl answered_questions -o questions.csv
```

Collected 1k questions which are unanswered and stored it in unanswered.csv file

```
scrapy crawl unanswered_questions -o unanswered.csv
```
Each question has the following attributes: 
* quesId, ownerId, summary, answers, tags, votes, views

## Task 

Take the questions which are unanswered and map to the most similar questions which are answered.
```
cd Task-1
jupyter notebook Task1.ipynb
```

```
 Corpus: answered questions (questions.csv)
 Queries:  each unanswered question (unanswered.csv)
 Libraries used: pandas, gensim, multiprocessing, threading 
```

```
1. Performed soft cosine similarity on each query and the document set
2. Provided the set of possible similar questions which have the score > 0.5
```




