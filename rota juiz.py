from flask import Flask, jsonify
import pandas as pd 

app = Flask(__name__)


@app.route('/juizes/')
def juiz():
    
    df_juiz = pd.read_csv('./futebol.csv', sep=';')
    df_juiz = df_juiz.replace({'á':'a','ã':'a', 'â':'a', 'í':'i','\W':'','ÅŸ':'s', 'Ä°':'I','Ä±':'i','Ã¶':'o','Ã§':'c', 'ÄŸ':'g','Ã¼':'u','Ã©':'e','Ã¡':'a','Ã³':'o','Ã±':'nh','&':'','Ã…Ë†':'n','Ã§':'c',' ':'','Ã­':'i','Ã£':'a','Ãº':'u','Ã':'a','Ãª':'e','Ã‘':'N','aÂ¢':'a','aÂª':'e','aÂ�':'a',"á":"a","é":"e","í":"i","ó":"o","ú":"u","ã":"a","õ":"o","aª":"e","á":"a","é":"e","í":"i","ó":"o","ú":"u","ã":"a","õ":"o","ê":"e","â":"a","ô":"o","ê":"e","â":"a","ô":"o"  }, regex=True)
    df_juiz = df_juiz.groupby('referee')['home_team_name'].agg('count').reset_index().rename(mapper={'referee': 'juiz', 'home_team_name': 'partidas'}, axis=1)

    return df_juiz.to_json (orient ='index')


app.run(debug=True)
