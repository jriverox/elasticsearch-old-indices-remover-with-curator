# settings.py
from dotenv import load_dotenv
load_dotenv()

import os
elasticsearch_host=os.getenv("ELASTIC_URL")
test_indices_names = ["prd-consultoras-ws-sbm-buscador-search-2019.01.12", "prd-ffvv-ws-unete-2019.04.01", "prd-ffvv-ws-portal-2019.07.25", "prd-ffvv-web-unete-2018.05.11", "test_producto_v4_co_201920"]