from elasticsearch import Elasticsearch, RequestsHttpConnection
import curator
import os
import settings

host = settings.elasticsearch_host

es = Elasticsearch(
        hosts = [{'host': host, 'port': 443}],
        use_ssl = True,
        verify_certs = True,
        connection_class = RequestsHttpConnection
    )

document = {
        "title": "Moneyball",
        "director": "Bennett Miller",
        "year": "2011"
    }

index_list = settings.test_indices_names

for idx in index_list:
    if not es.indices.exists(index=idx):
        es.index(index=idx, doc_type="movie", id="1", body=document)
        print(f'Indice : {idx} creado')