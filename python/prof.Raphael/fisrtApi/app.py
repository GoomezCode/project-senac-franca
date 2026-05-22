from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

person = [
    {"nome": "daniel", "password": "10/09/2008"},
    {"nome": "daniel", "password": "10/09/2008"},
    {"nome": "daniel", "password": "10/09/2008"},
    {"nome": "daniel", "password": "10/09/2008"}
]





@app.route('/')
def helloWord():
    return render_template("index.html")

@app.route('/sobre')
def sobre():
    return jsonify(person)

@app.route('/sobre/filter', methods=['GET'])
def sobreFilter():
    filtrado = []
    filter = request.args.get("filter")
    return filtrado
            

@app.route('/addPerson', methods=['POST'])
def addPerson():
    username = request.form['username']
    password = request.form['password']
    person.append({"nome": username, "password": password})
    return redirect(url_for("sobre"))


@app.route('/buscarPerson', methods=['GET'])
def buscarPerson():
    tipo = request.args.get("tipo")
    # verificar se a busca está errada
    if not tipo:
        return jsonify({
            "erro": "Parametro nao encontrado",
            "Dica": "Utilizar parametro tipo",
            "exemplo":"/buscarPerson?tipo=nome"
        }),400
        
    itens_filtrados = []
    for i in person:
        if i["nome"].lower() == tipo.lower():
            itens_filtrados.append(i)
            
    if itens_filtrados:    
        return jsonify(itens_filtrados)
    else:
        return jsonify({
            "Erro":f"""A pessoa: "{tipo}" nao foi encontrada!!"""
        }), 404


if __name__ == '__main__':
    app.run(debug=True)