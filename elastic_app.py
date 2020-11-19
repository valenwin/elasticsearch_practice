import json
import settings

from bottle import get, run
from elasticsearch import Elasticsearch


@get('/')
def elastic_app():
    client = settings.get_client()
    if client is None:
        html = '<h3 style="color:red">Warning: Elasticsearch cluster is not running on'
        html += ' port: ' + str(settings.ELASTIC_PORT) + '</h3>'
    else:
        # get the Elasticsearch client info
        client_info = Elasticsearch.info(client)

        # return the client data as JSON object to front end
        html = "<h2>Elasticsearch client information:</h2><br>"
        html += '<h3 id="elastic-resp"></h3><br>'
        html += '<script>'
        html += 'var respEle = document.getElementById("elastic-resp");'
        html += 'var elasticResp = JSON.stringify(' + json.dumps(client_info)
        html += ', null, 4);'
        html += 'respEle.innerHTML = elasticResp;'
        html += '</script>'

    return html


if __name__ == '__main__':
    run(
        host=settings.DOMAIN,
        port=settings.BOTTLE_PORT,
        debug=True
    )
