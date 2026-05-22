from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    return render_template("index.html")


@app.route("/window/buscarCep", methods=["GET"])
def windowBuscarCep():
    return render_template("searchCep.html")

@app.route("/window/buscarCnpj", methods=["GET"])
def windowBuscarCnpj():
    return render_template("searchCnpj.html")


@app.route("/api/buscarCep", methods=["GET"])
def apiBuscarCep():
    cep = request.args.get("cep")
    
    if not cep:
        return jsonify({
            "erro":"A busca do cep esta errada!",
            "dica":"Coloque  ( /buscarCep?cep='seu cep' ) "
        }),400    
            
    url = f"https://brasilapi.com.br/api/cep/v2/{cep}"
    response = requests.get(url)

    dados = response.json()
    return jsonify(dados)


@app.route("/api/BuscarCnpj", methods=["GET"])
def apiBuscarCnpj():
    cnpj = request.args.get("cnpj")
    
    if not cnpj:
        return jsonify({
            "erro":"A busca do CNPJ esta errada!",
            "dica":"Coloque  ( /BuscarCnpj?cnpj='seu cep' ) "
        }),400
    
    
    url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}"
    response = requests.get(url)
    
    dados = response.json()
    return jsonify(dados)



if __name__ == '__main__':
    app.run(debug=True)