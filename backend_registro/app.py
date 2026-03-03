from flask import Flask, request, jsonify, g
from flask_cors import CORS
from auth import require_auth, require_role
from db_wrapper import DBWrapper

app = Flask(__name__)
CORS(app)
db = DBWrapper()

# --- ROTTE DOCENTE ---
@app.route("/voti", methods=["POST"])
@require_auth
@require_role("docente")  # Solo il docente può inserire voti
def add_voto():
    data = request.get_json()
    studente = data.get("studente")
    materia = data.get("materia")
    voto = data.get("voto")

    if not all([studente, materia, voto]):
        return jsonify({"error": "Dati mancanti"}), 400

    db.inserisci_voto(studente, materia, voto)
    return jsonify({"message": "Voto inserito con successo!"}), 201

@app.route("/voti/tutti", methods=["GET"])
@require_auth
@require_role("docente")  # Solo il docente può vedere tutto
def get_tutti_voti():
    voti = db.get_tutti_voti()
    return jsonify({"voti": voti})


# --- ROTTE STUDENTE ---
@app.route("/voti/me", methods=["GET"])
@require_auth
@require_role("studente")  # Solo lo studente vede i propri
def get_miei_voti():
    # Estraiamo l'username dallo studente loggato tramite il token JWT
    username_studente = g.user.get("preferred_username") 
    
    if not username_studente:
         return jsonify({"error": "Impossibile determinare l'utente"}), 400
         
    voti = db.get_voti_studente(username_studente)
    return jsonify({"voti": voti})


if __name__ == "__main__":
    app.run(debug=True, port=5000)