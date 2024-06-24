import streamlit as st
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import random
from streamlit_card import card

st.set_page_config(page_title= "Yanakhasy", page_icon = "https://cdn.discordapp.com/attachments/1243172985502961727/1243173051185762365/logo.webp?ex=665082a0&is=664f3120&hm=fdfbae8bfd6a4ab5941daeb0b85566425615d30cb110951a55b60af2b7097315&",
layout="wide")



df_film = pd.read_csv("C:\\Users\\sylva\\OneDrive\\Documents\\Wild Code School\\Projet_2\\Datasets Nettoyés\\df_actu.csv")
df_intervenants_f = pd.read_csv("C:\\Users\\sylva\\OneDrive\\Documents\\Wild Code School\\Projet_2\\Datasets Nettoyés\\df_intervenant_f (1).csv", sep=",")

def card_custom(titre, image_url,tmdb,width = "150px"):
     return card(
                    title=titre,
                    text="",
                    image=image_url,
                    url=f"https://www.imdb.com/title/{tmdb}/",
                    styles={
                        "card": {
                            "width": width,
                            "height": "400px",
                            "border-radius": "20px",
                            "box-shadow": "0 0 10px rgba(0,0,0,0.5)"
                        },
                        "text": {
                            "font-family": "serif",
                            "font-size": "0px"  # Ajustez la taille de la police ici
                        },
                        "title": {
                            "font-family": "Arial",  # Changez le type de police ici
                            "font-size": "24px"  # Ajustez la taille de la police ici
                        }
                    }
                )



page = st.sidebar.selectbox("Choisissez une page", ["Accueil", "Recommandation par Film", "Recommandation par Mots-Clés", "Acteurs"])
if page == "Accueil":
    col1, col2, col3 = st.columns([0.2,0.2, 0.6])

    with col1:
       image_path = "https://cdn.discordapp.com/attachments/1243172985502961727/1243173051185762365/logo.webp?ex=665082a0&is=664f3120&hm=fdfbae8bfd6a4ab5941daeb0b85566425615d30cb110951a55b60af2b7097315&"
       st.image(image_path)

    with col3:
        st.title("Yanakhasy")
    #st.title("Accueil")
    #st.write("")
    #st.header("Bienvenue sur notre application de recommandation de films.")
    st.title("🎬 Bienvenue à nos cinéphiles de la Creuse ! 🍿")
    st.markdown("""
    Salut et bienvenue dans notre cinémathèque numérique ! 🎥 Laissez-vous embarquer dans un voyage cinématographique unique, spécialement conçu pour nos amis de la Creuse. Explorez notre sélection de films triés sur le volet et découvrez des pépites qui correspondent à vos goûts les plus subtils. 🌟 Préparez-vous à être éblouis par des histoires captivantes, des intrigues palpitantes et des émotions à couper le souffle ! 💫

    🎉 Alors, prêt à plonger dans l'univers magique du cinéma ? Cliquez, découvrez et laissez-vous emporter ! 🎬
    """)

    st.write("------------------------")

    images_films = df_film["poster_path"].iloc[72]
    images_acteurs = df_intervenants_f["images"].iloc[1]

    def card_accueil(titre, image_url,tmdb,width = "300px"):
     return card(
                    title="",
                    text="",
                    image=image_url,
                    url="",
                    styles={
                        "card": {
                            "width": width,
                            "height": "400px",
                            "border-radius": "20px",
                            "box-shadow": "0 0 10px rgba(0,0,0,0.5)"
                        },
                        "text": {
                            "font-family": "serif",
                            "font-size": "0px"  # Ajustez la taille de la police ici
                        },
                        "title": {
                            "font-family": "Arial",  # Changez le type de police ici
                            "font-size": "24px"  # Ajustez la taille de la police ici
                        }
                    }
                )
        

    col1, col2, col3 =st.columns([0.3, 0.6, 0.1])
    with col2:
        st.title("Exemples d'affichage")

    col1, col2, col3, col4, col5 = st.columns([0.2, 0.2, 0.3, 0.2, 0.1])
    with col2:
        st.header("Films")
    with col4:
        st.header("Acteurs")

    col1, col2 = st.columns([0.5, 0.5])
    with col1:
        hasClicked = card_accueil(images_films, images_films, df_film["title"].iloc[72], width = "300px")
    with col2:
        hasClicked = card_accueil(images_acteurs, images_acteurs, df_intervenants_f["name"].iloc[1], width = "300px")
    
########################################### Recommandation par Film ###############################################################
elif page == "Recommandation par Film":
    st.title("Recommandation par Film")

    #random_index_1 = random.randint(0, len(df_film) - 1)
    #default_option_1 = df_film.loc[random_index_1, 'title']
    
    liste_films = df_film["title"]
    film_choisi = st.selectbox(label="", options = liste_films, index = 0, placeholder = "Choisir un film")
    condition = df_film["title"] == film_choisi

    #duree = f"{(df_film[condition]["runtime"]//60)}h +  {(df_film[condition]["runtime"]%60)}min"

    col1, col2 = st.columns(2)

    with col1:
        if df_film[condition]["backdrop_path"].isnull().all():
            st.write("Pas de backdrop path disponible.")
        else:
            st.image( df_film[condition]["backdrop_path"].values[0])

    with col2:
        if df_film[condition]["release_date"].isnull().all():
            st.write("Pas de date de sortie disponible.")
        else:
            st.write(f'année de sortie:  {df_film[condition]["release_date"].values[0]}')
        if df_film[condition]["averageRating"].isnull().all():
            st.write("Pas de averageRating disponible.")
        else:
            st.write(f'évaluation:  {df_film[condition]["averageRating"].values[0]}')
        if df_film[condition]["numVotes"].isnull().all():
            st.write("Pas de nombre de vote disponible.")
        else:
            st.write(f'nombre de votes:  {df_film[condition]["numVotes"].values[0]}')
        if df_film[condition]["popularity"].isnull().all():
            st.write("Pas d'information sur la popularité.") 
        else: 
            st.write(f'popularité:  {df_film[condition]["popularity"].values[0]}')
        st.write(f'durée:  {df_film[condition]["runtime"].values[0]}')
        st.write(f"")
    st.write("Résumé")
    st.write(df_film[condition]["overview"].values[0])


    def recommend(film_choisi):
        index = df_film[df_film["title"]==film_choisi].index[0]
        
        df_dummies = df_film["genres"].str.get_dummies(sep=",")
        df_all = pd.concat([df_film,df_dummies],axis=1)
        X = df_all[["averageRating", "numVotes", "popularity", "release_date", "runtime", "budget", "revenue","vote_count","vote_average",
                        'Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                        'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'Romance', 'Sci-Fi',
                        'Sport', 'Thriller', 'War', 'Western']]

        scaler = MinMaxScaler()
        X_scaled = scaler.fit_transform(X)
        model = NearestNeighbors(n_neighbors=6).fit(X_scaled)
        var1,var2 = model.kneighbors(X_scaled)
        var2 = var2[:, 1:]
        indice = var2[index]
        df_reco = df_film.iloc[indice]
        films = []
        backdrop_path = []
        id_reco = []
        for i in (df_reco["title"]):
            films.append(i)
        for j in df_reco["backdrop_path"]:
            backdrop_path.append(j)
        for id in df_reco["imdb_id"]: 
            id_reco.append(id)
            

        return id_reco,films,backdrop_path


    id_reco,liste_films_reco, backdrop_path_reco = recommend(film_choisi)
    #st.write(id)
    col1,col2,col3,col4,col5 =st.columns(5)
    with col1:
        url = f"https://www.imdb.com/title/{id}/"
        hasClicked = card_custom(liste_films_reco[0], backdrop_path_reco[0],id_reco[0])

        # Utilisation de HTML et CSS pour personnaliser la couleur du lien
        #st.markdown(f"""
        #<a href="{url}" style="color: black; text-decoration: none; font-weight: bold; font-size: 15px;">{titre}</a>
        #""", unsafe_allow_html=True)


        #st_clickable_images(image_paths = backdrop_path_reco[0], titles=liste_films_reco[0], div_style={}, img_style={})
    with col2:
        url = f"https://www.imdb.com/title/{id}/"
        hasClicked = card_custom(liste_films_reco[1], backdrop_path_reco[1],id_reco[1])

    with col3:
        url = f"https://www.imdb.com/title/{id}/"
        hasClicked = card_custom(liste_films_reco[2], backdrop_path_reco[2],id_reco[2])

    with col4:
        url = f"https://www.imdb.com/title/{id}/"
        hasClicked = card_custom(liste_films_reco[3], backdrop_path_reco[3],id_reco[3])

    with col5:
        url = f"https://www.imdb.com/title/{id}/"
        hasClicked = card_custom(liste_films_reco[4], backdrop_path_reco[4],id_reco[4])


########################################### Recommandation par keywords #########################################################

elif page == "Recommandation par Mots-Clés":
    st.title("Recommandation par Mots-Clés")

    #random_index_2 = random.randint(0, len(df_film) - 1)
    #default_option_2 = df_film.loc[random_index_2, 'title']

    liste_films = df_film["title"]
    film_choisi = st.selectbox(label="", options = liste_films, index = 0, placeholder = "Choisir un film")
    condition = df_film["title"] == film_choisi

    col1, col2 = st.columns(2)

    with col1:
        if df_film[condition]["backdrop_path"].isnull().all():
            st.write("Pas de backdrop path disponible.")
        else:
            st.image( df_film[condition]["backdrop_path"].values[0])

    with col2:
        if df_film[condition]["release_date"].isnull().all():
            st.write("Pas de date de sortie disponible.")
        else:
            st.write(f'année de sortie:  {df_film[condition]["release_date"].values[0]}')
        if df_film[condition]["averageRating"].isnull().all():
            st.write("Pas de averageRating disponible.")
        else:
            st.write(f'évaluation:  {df_film[condition]["averageRating"].values[0]}')
        if df_film[condition]["numVotes"].isnull().all():
            st.write("Pas de nombre de vote disponible.")
        else:
            st.write(f'nombre de votes:  {df_film[condition]["numVotes"].values[0]}')
        if df_film[condition]["popularity"].isnull().all():
            st.write("Pas d'information sur la popularité.") 
        else: 
            st.write(f'popularité:  {df_film[condition]["popularity"].values[0]}')
            st.write(f'durée:  {df_film[condition]["runtime"].values[0]}')
            
    st.write(f"")
    st.write("Résumé")
    st.write(df_film[condition]["overview"].values[0])

    count = CountVectorizer()
    count_matrix = count.fit_transform(df_film['mot_cle'])
    cosine_sim = cosine_similarity(count_matrix, count_matrix)

    def recommend_par_keyword(film_choisi, cosine_sim = cosine_sim):
        recommended_movies = []
        backdrop_path = []
        id_reco = []
        idx = df_film[df_film["title"] == film_choisi].index[0]   # to get the index of the movie title matching the input movie
        score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)   # similarity scores in descending order
        top_5_indices = list(score_series.iloc[1:6].index)   # to get the indices of top 6 most similar movies
        # [1:6] to exclude 0 (index 0 is the input movie itself)
        
        for i in top_5_indices:   # to append the titles of top 10 similar movies to the recommended_movies list
            recommended_movies.append(list(df_film['title'])[i])
            
        for j in top_5_indices : 
            backdrop_path.append(df_film["backdrop_path"][j])
        for id in top_5_indices:
            id_reco.append(df_film["imdb_id"][id])
        return id_reco,recommended_movies,backdrop_path

    id_reco,liste_films_reco,backdrop_path = recommend_par_keyword(film_choisi,cosine_sim)
    col1,col2,col3,col4,col5 =st.columns(5)
    with col1:
        url = f"https://www.imdb.com/title/{id}/"
        hasClicked = card_custom(liste_films_reco[0], backdrop_path[0],id_reco[0])

    with col2:
        url = f"https://www.imdb.com/title/{id}/"
        hasClicked = card_custom(liste_films_reco[1], backdrop_path[1],id_reco[1])

    with col3:
        url = f"https://www.imdb.com/title/{id}/"
        hasClicked = card_custom(liste_films_reco[2], backdrop_path[2],id_reco[2])

    with col4:
        url = f"https://www.imdb.com/title/{id}/"
        hasClicked = card_custom(liste_films_reco[3], backdrop_path[3],id_reco[3])
        
    with col5:
        url = f"https://www.imdb.com/title/{id}/"
        hasClicked = card_custom(liste_films_reco[4], backdrop_path[4],id_reco[4])




################################################ Page Acteurs #########################################################################


elif page == "Acteurs":
    import random
    import requests
    from api_fct import find_movie_by_id


    df_intervenants_f = pd.read_csv("C:\\Users\\sylva\\OneDrive\\Documents\\Wild Code School\\Projet_2\\Datasets Nettoyés\\df_intervenant_f (1).csv", sep=",")

    names = df_intervenants_f["name"] 

    df_actu = pd.read_csv("C:\\Users\\sylva\\OneDrive\\Documents\\Wild Code School\\Projet_2\\Datasets Nettoyés\\df_actu.csv", sep=",")

    #col1, col2, col3 = st.columns([0.3, 0.5, 0.2])

    #with col2:
        #image_path = "https://cdn.discordapp.com/attachments/1243172985502961727/1243173051185762365/logo.webp?ex=665082a0&is=664f3120&hm=fdfbae8bfd6a4ab5941daeb0b85566425615d30cb110951a55b60af2b7097315&"

        #st.image(image_path)

    st.title("Sur cette page tu trouveras une photo de l'intervenant.e que tu as choisi")
    st.write("Et si tu as de la chance il y aura peut-être d'autres infos ;)")

    ######################################### présentation de l'image et des affiches de films #############################################
    #random_index_3 = random.randint(0, len(df_intervenants_f) - 1)
    #default_option_3 = df_intervenants_f.loc[random_index_3, 'name']


    with st.container():
    
        option = st.selectbox("Choisissez un nom :", names, index = 0)
        df_filter = df_intervenants_f[df_intervenants_f["name"] == option]

        def rechercher():
            recherche_nom = st.text_input("Saisissez votre terme de recherche :")
            if recherche_nom:
                df_filter_2 = df_intervenants_f[df_intervenants_f["name"] == recherche_nom]

        
        col1, col2= st.columns([0.5, 0.5])

        with col1:
            image_path = df_filter["images"].iloc[0]
            img_remp = "https://i.ytimg.com/vi/_g9Bfj1yy-c/hqdefault.jpg"
            if pd.isna(df_filter["images"].iloc[0]) or (df_filter["images"].iloc[0] == '') or (df_filter["images"].iloc[0].endswith("nan")):
                st.image(img_remp)
                st.text("")
                st.write("Désolé nous n'avons pas d'image à te proposer")
                st.write("Nous t'encourageons à aller voir les sites recommandés sur ta droite")
            else:
                st.image(image_path)

        st.write("----------------------------")



    ################################################# informations ######################################################################

        with col2:
            st.header("Informations diverses")

            birth = df_filter["birthday"].iloc[0] if not pd.isna(df_filter["birthday"].iloc[0]) else "Pas d'information disponible"
            death = df_filter["deathday"].iloc[0] if not pd.isna(df_filter["birthday"].iloc[0]) else "PAs d'information disponible"
            birth_place = df_filter["place_of_birth"].iloc[0] if not pd.isna(df_filter["birthday"].iloc[0]) else "PAs d'information disponible"

            st.write("----------------------------")

            if not pd.isna(df_filter["birthday"].iloc[0]):
                if not pd.isna(df_filter["place_of_birth"]).iloc[0]:
                    st.write("Né le", birth, "à", birth_place)
                else:
                    st.write("Né le", birth)
            else:
                st.write("Pas d'information disponible")

            if not pd.isna(df_filter["deathday"].iloc[0]):
                st.write("Date de décès :", death)

            st.write("----------------------------")

            popularity = df_filter["popularity"].iloc[0]
            if popularity >= 50:
                st.write("Côte de popularité :", popularity)
                st.write("Extrêmement populaire")
            elif 20 <= popularity < 50:
                st.write("Côte de popularité :", popularity)
                st.write("Populaire")
            elif 10 <= popularity < 20:
                st.write("Côte de popularité :", popularity)
                st.write("Pas très populaire")
            elif popularity < 10:
                st.write("Côte de popularité :", popularity)
                st.write("Peu populaire")

            st.write("----------------------------")

            homepage = df_filter["homepage"].iloc[0]
            imdb = "https://www.imdb.com/name/" + df_filter["imdb_id"].iloc[0]
            wiki = "https://fr.wikipedia.org/wiki/" + df_filter["name"].iloc[0].replace(" ", "_")
            if not pd.isna(df_filter["homepage"].iloc[0]):
                col1, col2, col3 = st.columns([0.3, 0.3, 0.3])
                with col1:
                    st.markdown(f"[Page Perso]({homepage})")
                with col2:
                    st.markdown(f"[Page imdb]({imdb})")
                with col3:
                    st.markdown(f"[Page Wikipedia]({wiki})")

            else:
                col1, col2, col3, col4, col5 = st.columns([0.05, 0.4, 0.1, 0.4, 0.05])
                with col2:
                    st.markdown(f"[Page imdb]({imdb})")
                with col4:
                    st.markdown(f"[Page Wikipedia]({wiki})")

            st.write("----------------------------")

    ################################### Récupération des titres de films et affichage #################################################
    col1, col2, col3 = st.columns([0.35, 0.5, 0.15])
    with col2:
        st.title("Films notables")

    knownFor = df_filter["knownForTitles"].iloc[0]
    if not pd.isna(knownFor):
        knownFor = knownFor.split(",")            # transforme la chaîne de caractères en liste
        df_actor = find_movie_by_id(knownFor)     # applique la fonction find_movie_by_id sur la liste
        df_actor = df_actor.reset_index(drop = True)   # utiliser pour éviter d'avoir un nouvel index
        df_actor['poster_path'] = df_actor.poster_path.apply(lambda image : "https://media.themoviedb.org/t/p/w300_and_h450_bestv2" +  image)
        #print(df_actor['poster_path'].to_markdown())
        #st.dataframe(df_actor)


    result = st.columns(len(df_actor))
            #va adapter le nombre de colonnes au nombre de titres
    if result != 0:
        for i in range(len(df_actor)):              #on parcoure df_actor
            with result[i] :                        # selon la valeur de i => i est l'indice de la ligne sur laquelle il travaille
                #st.write('hey')
                titre = df_actor.iloc[i, -9]        # récupère le title dans df_actor
                image_index = list(df_actor.columns).index("poster_path") # trouve l'indice où se trouve le poster_path => ici 4 
                image_url = df_actor.iloc[i,image_index]   # créé une variable image_url qui va récupérer dans df_actor i pour la ligne, image_index pour la colonne
                tmdb = df_actor.iloc[i, -1]                 # récupère pour la ligne d'indice i la dernière colonne: id_tmdb
                url = f"https://www.imdb.com/title/{tmdb}/"   # concaténation
                # Configuration de la carte avec des styles personnalisés
                
                hasClicked = card_custom(titre, image_url,tmdb, width = "200px")

    else:
        st.write("Désolé, nous n'avons pas de films à vous présenter")
        pass



    ################################################## biographie #########################################################################

    biography = df_filter["biography"].iloc[0]
    autre = df_filter["known_for_department"].iloc[0]

    #dico = {"Directing" : "Directeur / Directrice",
            #"Acting" : "Acteur / Actrice",
            #"Poduction" : "Producteur / Productrice",
            #"Writing" : "Scénariste",
            #"Creator"}
    if not pd.isna(df_filter["biography"].iloc[0]):
        st.title("Biographie")
        st.markdown(biography)
    else:
        col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
        with col2:
            st.header("Aïe nous n'avons pas de biographie à te proposer")
            st.write("Nous t'encourageons à aller voir les sites recommandés un peu plus haut")
    
    

        


        
        
        
            

