import pandas as pd 
import requests
from bs4 import BeautifulSoup

requests.get('http://testphp.vulnweb.com/listproducts.php?cat=1')