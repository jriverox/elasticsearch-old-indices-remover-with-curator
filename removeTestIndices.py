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

index_list = settings.test_indices_names

for idx in index_list:
    if es.indices.exists(index=idx):
        es.indices.delete(index=idx)
        print(f'Indice : {idx} borrado')