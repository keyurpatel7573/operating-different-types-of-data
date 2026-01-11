import requests
import pandas as pd 
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('TMDB_API-KEY')
# for the first page from the Api
url = f"https://api.themoviedb.org/3/tv/top_rated?api_key={api_key}&language=en-us&page=1"

response = requests.get(url)
jason_format = response.json()['results']
df = pd.DataFrame(jason_format)[["id","original_name","overview","popularity","vote_average","vote_count"]]

# for all the pages from the api
df =[]
for i in range(1,119):
  response = requests.get( f"https://api.themoviedb.org/3/tv/top_rated?api_key={api_key}&language=en-us&page={i}")

  temp_df = pd.DataFrame(response.json()["results"])[["id","original_name","overview","popularity","vote_average","vote_count"]]
  df.append(temp_df)

dfs = pd.concat(df, ignore_index=True)
dfs.to_csv("tranding_movies.csv")