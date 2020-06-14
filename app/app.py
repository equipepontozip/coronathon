from flask import Flask
import os
#from swagger.swagger_config import swagger_configuration
from flasgger import Swagger
from logging.config import dictConfig
import json

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

@app.route('/status')
def status():
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

app.run(host=os.environ['HOST'],port=os.environ['PORT'])