from flask import Flask, request
from flask_restplus import Api, Resource
from elasticsearch import Elasticsearch
import requests
from flask import jsonify

flask_app = Flask(__name__)
api = Api(app=flask_app)
es = Elasticsearch(hosts=[{'host': "localhost", 'port': 9200}])  # start the elasticsearch client

name_space = api.namespace('main', description='Main APIs')


@name_space.route("/search")
class Search(Resource):
    @name_space.doc(params={
        "search_terms": "something you want to search..."
    })
    def get(self):
        search_terms = request.args.get("search_terms")  # get the search term inputs from web browser
        print(search_terms)
        # it is very important to learn how to build advance query body,
        # refer to "https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html"
        query_body = {
            "query": {
                "multi_match": {
                    "query": search_terms,
                    "fields": ["headline", "short_description"]
                    # search the "search terms" in the "headline", "short_description" in your indexed data
                }
            }
        }
        res = es.search(index='text-index', body=query_body)
        # sent the query body to the elasticsearch server, and search in the "text-index", and return results
        print(res)
        return jsonify(res)  # convert the result into json format, and return


if __name__ == '__main__':
    flask_app.run(debug=True)
