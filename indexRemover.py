#import boto3
#from requests_aws4auth import AWS4Auth
from elasticsearch import Elasticsearch, RequestsHttpConnection
import curator
import os
import sys
import settings

host = settings.elasticsearch_host
#region = os.environ['region_es'] # For example, us-west-1

#service = 'es'
#credentials = boto3.Session().get_credentials()
#awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

# Lambda execution starts here.
def lambda_handler(event, context):
    # Build the Elasticsearch client.
    es = Elasticsearch(
        hosts = [{'host': host, 'port': 443}],
        use_ssl = True,
        verify_certs = True,
        connection_class = RequestsHttpConnection
    )

    index_list = curator.IndexList(es)

    # Filters by age, anything with a time stamp older than 30 days in the index name.
    index_list.filter_by_age(source='name', direction='older', timestring='%Y.%m.%d', unit='days', unit_count=30)
    # If our filtered list contains any indices, delete them.
    if index_list.indices:
        print(f'Indices que finalmente se eliminaran: {index_list.indices}')
        curator.DeleteIndices(index_list).do_action()
    else:
        print("Ningun indice para eliminar")