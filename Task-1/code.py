import pandas as pd
from Similarity import DocSim

docsim_obj = DocSim(verbose=True)
print(f'Model ready: {docsim_obj.model_ready}')

if docsim_obj.model_ready:
    df = pd.read_csv(r'./questions.csv')
    titles = df['summary']
    documents = df['summary']

    print(f'{len(documents)} documents')

    query_string = 'Optimising subgraph of a large graph'

    similarities = docsim_obj.similarity_query(query_string, documents)

    print(similarities[0])
    for idx, score in (sorted(enumerate(similarities), reverse=True, key=lambda x: x[1])[:15]):
        print(f'{idx} \t {score:0.3f} \t {titles[idx]}')