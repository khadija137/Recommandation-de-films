import pandas as pd
import requests
def find_movie_by_id(maliste) :

                list_df = []

                for id in maliste :

                    language = "fr"
                    key = "e96a78ea12a5b06071ae2278954655a9"
                    url = f"https://api.themoviedb.org/3/find/{id}?api_key={key}&external_source=imdb_id&language={language}"
                    response = requests.get(url)
                    r_js = response.json()
                    df_movie_tmdb = pd.json_normalize(r_js, record_path = "movie_results")
                    df_movie_tmdb['id_tmdb'] = id
                    list_df.append(df_movie_tmdb)
                return  pd.concat(list_df)