# AWS Lambda implementation to dele older indices in Elasticsearch using Curator API in Python

## Requierements:
1. AWS Account
2. Permissions to create lambda
3. Elasticsearch with indices that have as a suffix like yyyy.MM.dd, i.e: my_index_2019.07.31

## Deployments Steps:
1. pip install --target ./package elasticsearch-curator
2. Copy folder package to an outside folder
3. Remove unnecessary packages like all boto3 reated
4. Copy function.py to folder move in previous step
5. Enter the root of the folder and create zip file
6. rename zip file to function.zip
7. Login in aws console
8. Go to Lambda
9. Create new function
10. Select Python 3.7 as platform
11. Upload function.zip
12. create new role (leave default value)
13. add environment variable ELASTIC_URL with yor elasticsearch endpoint

Note: if your elastic require authentication, you must provide inside the function code, on elasticsearch instantiation
