from flask import Flask, jsonify
import pandas as pd 
import numpy as np

app = Flask(__name__)

@app.route('/jogo')
def historico_jogo():
    df=pd.read_csv("futebol.csv", sep=';')
    df.replace({'á':'a','ã':'a', 'â':'a', 'í':'i','\W':'','ÅŸ':'s', 'Ä°':'I','Ä±':'i','Ã¶':'o','Ã§':'c', 'ÄŸ':'g','Ã¼':'u','Ã©':'e','Ã¡':'a','Ã³':'o','Ã±':'nh','&':'','Ã…Ë†':'n','Ã§':'c',' ':'','Ã­':'i','Ã£':'a','Ãº':'u','Ã':'a','Ãª':'e','Ã‘':'N','aÂ¢':'a','aÂª':'e','aÂ�':'a',"á":"a","é":"e","í":"i","ó":"o","ú":"u","ã":"a","õ":"o","aª":"e","á":"a","é":"e","í":"i","ó":"o","ú":"u","ã":"a","õ":"o","ê":"e","â":"a","ô":"o","ê":"e","â":"a","ô":"o"  }, regex=True)
    df = df[['date_GMT','home_team_name', 'away_team_name', 'home_team_goal_count', 'away_team_goal_count']]
    df['Jogos']=df['home_team_name'].astype(str) + ' x '+ df['away_team_name'].astype(str).rename({'home_team_name': 'Time Casa', 'away_team_name': 'Time Visitante',})
    df['Placar']=df['home_team_goal_count'].astype(str) + ' - ' + df ['away_team_goal_count'].astype(str) + ' - ' + df['date_GMT'].astype(str)
    
    return df[['Jogos','Placar']].to_json(orient='index')


#print ('resposta')

app.run(debug=True)