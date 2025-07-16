# importa o framework flask
from flask import Flask

# cria a aplicação
app = Flask(__name__)

 #define uma rota para o endereço principal "/"
@app.route("/")
def home():
  return "Bem vindo"

# define uma rota extra chamada "/sobre"
@app.route("/sobre")
def sobre():
  return "essa é a pagina sobre."

#roda o servidor local com debug ativado
if __name__ == "__main__":
  app.run(debug=True)