import json

from elasticsearch import Elasticsearch

DOMAIN = "localhost"
ELASTIC_PORT = 9200
BOTTLE_PORT = 1234


def get_client():
    try:
        domain_str = DOMAIN + ":" + str(ELASTIC_PORT)
        client = Elasticsearch(domain_str)
        print(json.dumps(Elasticsearch.info(client), indent=4), "\n")
    except Exception as err:
        print("Elasticsearch() ERROR:", err, "\n")
        client = None

    return client
