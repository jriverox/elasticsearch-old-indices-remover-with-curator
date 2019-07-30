# Example Of How to remove older indices in Elasticsearch using Curator API in Python

### indexRemover.py contain the logic for remove indices in elasticsearch using curator.filter_by_age

### createTestIndices.py can be used for create test indices tha will be used por testing purpose

### removeTestIndices.py can be used for remove indices that were not removed by indexRemover

To test all script, run in following order:
1. python createTestIndices.py
2. python -c "from indexRemover import *; lambda_handler()"
3. python removeTestIndices.py