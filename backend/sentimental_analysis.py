import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import string
import seaborn as sns
import matplotlib.pyplot as plt

base_url="https://www.airlinequality.com/airline-reviews/emirates"
page_size=100
page=1

url = f"{base_url}/page/{page}/?sortby=post_date%3ADesc&pagesize={page_size}"

response = requests.get(url)

content = response.content

print(response,'check!')

