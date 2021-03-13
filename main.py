from flask import Flask, render_template
from utils import returnStreamers
from datetime import datetime
import os

# Importar e setar o dotenv apenas se 
# tivermos em um ambiente de desenvolvimento
if os.environ.get("FLASK_ENV") == "development":
	from dotenv import load_dotenv
	load_dotenv()


app = Flask(__name__)
app.jinja_env.filters['zip'] = zip

# Processador de contexto que irá ser executado antes do template
# e possibilitará termos acesso à variável now dentro do index.html
# para assim termos dinâmicamente o ano do copyright
# https://stackoverflow.com/questions/41231290/how-to-display-current-year-in-flask-template
@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


@app.route("/", methods=["GET"])
def index():
	streamers1, streamers2 = returnStreamers()
	return render_template("index.html", streamers1=streamers1, streamers2=streamers2)


if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)