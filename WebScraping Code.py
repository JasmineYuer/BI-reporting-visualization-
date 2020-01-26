# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 19:23:24 2019

@author: jasmine
"""

import requests
import json
from time import sleep
import pandas as pd

movies = pd.read_csv('movieids.csv')
movies = movies['tconst'].tolist()

Title = []
Rated = []
Released = []
Awards = []
imdbVotes = []
DVD = []
BoxOffice = []
Production = []
imdbRating = [None] * len(movies)
RottenTomatoes = [None] * len(movies)
Metacritic = [None] * len(movies)
imdbID = []


for i in movies:
    print(movies.index(i)+1,'/',len(movies))
    url = 'http://www.omdbapi.com/?i='+ str(i) +'&apikey=a79ea526'
    response = requests.get(url)
    data = response.json()
    try:
        BoxOffice.append(data['BoxOffice'])
    except KeyError: 
        BoxOffice.append('N/A')     
    try:
        Title.append(data['Title'])
    except KeyError:
        Title.append('N/A')
    try:
        Rated.append(data['Rated'])
    except KeyError:
        Rated.append('N/A')
    try:
        Released.append(data['Released'])
    except KeyError:
        Released.append('N/A')
    try:
        Awards.append(data['Awards'])
    except KeyError:
        Awards.append('N/A')
    try:
        imdbVotes.append(data['imdbVotes'])
    except KeyError:
        imdbVotes.append('N/A')
    try:
        DVD.append(data['DVD'])
    except KeyError:
        DVD.append('N/A')
    try:
        Production.append(data['Production'])
    except KeyError:
        Production.append('N/A')
    try:
        imdbID.append(data['imdbID'])
    except KeyError:
        imdbID.append('N/A')
    try: 
        for j in range(len(data['Ratings'])):
            if data['Ratings'][j]['Source'] == 'Internet Movie Database':
                imdbRating[movies.index(i)] = data['Ratings'][j]['Value']
            if data['Ratings'][j]['Source'] == 'Rotten Tomatoes':              
                RottenTomatoes[movies.index(i)] = data['Ratings'][j]['Value']
            if data['Ratings'][j]['Source'] == 'Metacritic':              
                Metacritic[movies.index(i)] = data['Ratings'][j]['Value']
    except KeyError:
        imdbRating[movies.index(i)] = 'N/A'
        RottenTomatoes[movies.index(i)] = 'N/A'
        Metacritic[movies.index(i)] = 'N/A'  
    sleep(2)


moviedf = pd.DataFrame(list(zip(imdbID, Title, Rated, Released, Awards, 
                                imdbVotes, DVD, BoxOffice, Production, imdbRating, 
                                RottenTomatoes, Metacritic)), 
                        columns = ['tconst','Title', 'Rated', 'Released', 'Awards',
                                   'imdbVotes', 'DVD', 'BoxOffice', 'Production',
                                   'imdbRating', 'RottenTomatoes', 'Metacritic'])
        

    
    
                
            
                

                    
                    

                
    
    
    

