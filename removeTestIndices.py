from elasticsearch import Elasticsearch, RequestsHttpConnection
import curator

host = 'vpc-es-sbsearch-qa-6lqloaf2kfljixcaekbyqxu2aa.us-east-1.es.amazonaws.com' # For example, search-my-domain.region.es.amazonaws.com
region = 'us-east-1'

es = Elasticsearch(
        hosts = [{'host': host, 'port': 443}],
        use_ssl = True,
        verify_certs = True,
        connection_class = RequestsHttpConnection
    )

index_list = ["prd-consultoras-ws-sbm-buscador-search-2019.01.12", "prd-ffvv-ws-unete-2019.04.01", "prd-ffvv-ws-portal-2019.07.25", "prd-ffvv-web-unete-2018.05.11", "test_producto_v4_co_201920"]

for idx in index_list:
    if es.indices.exists(index=idx):
        es.indices.delete(index=idx)
        print(f'Indice : {idx} borrado')