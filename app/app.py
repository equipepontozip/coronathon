from flask import Flask, render_template, request
import os
#from swagger.swagger_config import swagger_configuration
from flasgger import Swagger
from logging.config import dictConfig
import json

from surprise import KNNBasic
from surprise import dump

import pandas as pd

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


app = Flask(__name__, template_folder='/code/app/templates', static_url_path='/code/app/static')

#swagger = Swagger(app, config=swagger_configuration)

df_trabalhadores = pd.read_csv("data/D_ETL_IMO_EXTRACAO_SINE_ABERTO_TRABALHADORES_SP.csv", sep=";", encoding="iso8859-1")
df_trabalhadores['id'] = df_trabalhadores.index

df_vagas = pd.read_csv("data/vagas_mock.csv")

df_results = pd.read_csv("data/match_database.csv")

@app.route('/status')
def status():
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

## Recebe id de usuario e de empresa e calcula o match de ambos
@app.route('/predict')
def predict():
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

## recebe o id de trabalhador e procura os melhores matches de empresas
@app.route('/get_empresas', methods = ['POST'])
def get_empresas():

    input_dict = request.get_json()
    app.logger.info(f"JSON object received in /get_empresas route: {input_dict}")

    id_trabalhador = input_dict['id_trabalhador']

    vagas = df_results[df_results['id_trabalhador']==id_trabalhador].sort_values(by=['prediction_rating'], ascending=False).head(10).id_posicao.values

    results = df_vagas[df_vagas['id_empresa'].isin(vagas)]

    return json.dumps(results.to_dict(orient="records")), 200, {'ContentType':'application/json'}

## recebe o id de empresa e procura os melhores matches de trabalhadores
@app.route('/get_trabalhadores', methods = ['POST'])
def get_trabalhador():

    input_dict = request.get_json()
    app.logger.info(f"JSON object received in /get_trabalhadores route: {input_dict}")

    id_vaga = input_dict['id_posicao']

    trabalhadores = df_results[df_results['id_posicao']==id_vaga].sort_values(by=['prediction_rating'], ascending=False).head(10).id_trabalhador.values

    results = df_trabalhadores[df_trabalhadores['id'].isin(trabalhadores)]

    return json.dumps(results.to_dict(orient="records")), 200, {'ContentType':'application/json'}

app.run(host=os.environ['HOST'],port=os.environ['PORT'])