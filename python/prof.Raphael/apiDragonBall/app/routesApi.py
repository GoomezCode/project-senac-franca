from flask import request, jsonify
import requests
from app import app

@app.route("/api/getCharacter", methods=["GET"])
def getCharacter():
    BASE_URL = "https://dragonball-api.com/api/characters"
    params = {}
    
    if request.args.get("name"):
        params["name"] = request.args.get("name")

    if request.args.get("gender"):
        params["gender"] = request.args.get("gender")

    if request.args.get("race"):
        params["race"] = request.args.get("race")

    if request.args.get("affiliation"):
        params["affiliation"] = request.args.get("affiliation")

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()

        data = response.json()

        return jsonify({
            "filters_used": params,
            "api_response": data
        })
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/api/getPlanet", methods=["GET"])
def getPlanets():
    BASE_URL_PLANETS = "https://dragonball-api.com/api/planets"
    try:
        # Captura filtros da URL (name e isDestroyed)
        params = {}

        if request.args.get("name"):
            params["name"] = request.args.get("name")

        if request.args.get("isDestroyed"):
            params["isDestroyed"] = request.args.get("isDestroyed").lower()

        # Faz a requisição para a API externa
        response = requests.get(BASE_URL_PLANETS, params=params)
        response.raise_for_status()

        return jsonify({
            "filters_used": params,
            "api_response": response.json()
        })

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
