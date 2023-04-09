from flask import Flask, jsonify
import pandas as pd 

app = Flask(__name__)


@app.route('/rota/casa/chelsea')
def Chelsea():
    
    df = pd.read_csv('./futebol.csv', sep=';', encoding="UTF-8")
    #comando dos pandas para ler uma base de dados
    df = df[['home_team_name', 'away_team_name', 'home_team_goal_count', 'away_team_goal_count']]
    #criando uma base apenas com as colunas que vamos usar
    dft1c = df.loc[(df['home_team_name']) == 'Chelsea'].reset_index()
    #base com todos os dados onde o chelsea foi o time de casa
    dft1v = df.loc[(df['away_team_name']) == 'Chelsea'].reset_index()
    #base com todos os dados onde o chelsea foi o time visitante
    dfttgc = dft1c['home_team_goal_count'].sum()
    #soma dos gols na base onde o chelsea foi o time de casa
    dfttgv = dft1v['away_team_goal_count'].sum()
    #soma dos gols na base onde o chelsea foi o time visitante
    dfttgols = dfttgc + dfttgv
    dfttgols = dfttgols.astype(str)
    resposta= {'Time: Chelsea - Total Gols':dfttgols}

    return jsonify (resposta)


@app.route('/rota/casa/Palmeiras') 
def Palmeiras(): 
    
    df2 = pd.read_csv('./futebol.csv', sep=';', encoding="UTF-8")
    #comando dos pandas para ler uma base de dados
    df2 = df2[['home_team_name', 'away_team_name', 'home_team_goal_count', 'away_team_goal_count']]
    #criando uma base apenas com as colunas que vamos usar
    dft2c = df2.loc[(df2['home_team_name']) == 'Palmeiras'].reset_index()
    #base com todos os dados onde o palmeiras foi o time de casa
    dft2v = df2.loc[(df2['away_team_name']) == 'Palmeiras'].reset_index()
    #base com todos os dados onde o palmeiras foi o time visitante
    dftt2gc = dft2c['home_team_goal_count'].sum()
    #soma dos gols na base onde o palmeiras foi o time de casa
    dftt2gv = dft2v['away_team_goal_count'].sum()
    #soma dos gols na base onde o palmeiras foi o time visitante
    dftt2gols = dftt2gc + dftt2gv
    dftt2gols = dftt2gols.astype(str)
    resposta= {'Time: Palmeiras - ' 'Total Gols':dftt2gols}

    return jsonify (resposta)
    
@app.route('/rota/casa/Internacional') 
def Internacional(): 
    
    df3 = pd.read_csv('./futebol.csv', sep=';', encoding="UTF-8")
    #comando dos pandas para ler uma base de dados
    df3 = df3[['home_team_name', 'away_team_name', 'home_team_goal_count', 'away_team_goal_count']]
    #criando uma base apenas com as colunas que vamos usar
    dft3c = df3.loc[(df3['home_team_name']) == 'Internacional'].reset_index()
    #base com todos os dados onde o internacional foi o time de casa
    dft3v = df3.loc[(df3['away_team_name']) == 'Internacional'].reset_index()
    #base com todos os dados onde o internacional foi o time visitante
    dftt3gc = dft3c['home_team_goal_count'].sum()
    #soma dos gols na base onde o internacional foi o time de casa
    dftt3gv = dft3v['away_team_goal_count'].sum()
    #soma dos gols na base onde o internacional foi o time visitante
    dftt3gols = dftt3gc + dftt3gv
    dftt3gols = dftt3gols.astype(str)
    resposta= {'Time: Internacional - ' 'Total Gols':dftt3gols}

    return jsonify (resposta)


app.run(debug=True)