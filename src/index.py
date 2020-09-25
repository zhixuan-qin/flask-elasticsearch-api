from elasticsearch import Elasticsearch
import json
'''
Refer to the links below for the details regarding the elasticsearch liabrary 
https://elasticsearch-py.readthedocs.io/en/master/
https://elasticsearch-py.readthedocs.io/en/master/api.html#elasticsearch
'''


# Initialize the Elasticsearch client, and connect it to the elasticsearch server
es = Elasticsearch(hosts=[{'host': "localhost", 'port': 9200}])

# Delete Index "test-index" if it exists
if es.indices.exists('test-index'):
    es.indices.delete(index='test-index', ignore=[400, 404])

# Create Index "test-index" in the Elasticsearch database in the Elasticsearch server
es.indices.create(index='test-index', ignore=400)

# I copied the "SPORTS.json" from your 253 project to the data folder, and indexed it into the elasticsearch database
for line in open('../data/SPORTS.json'):
    doc = json.loads(line) # convert the dictionary string to dictionary
    print(doc)
    es.index(index='test-index', body=doc) # index the doc into the elasticsearch database
