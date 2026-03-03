from functools import wraps
from flask import jsonify, g

# (Assicurati di includere qui il tuo decoratore require_auth della lezione "Keycloak pt1"
# che verifica il JWT e salva il payload in g.user)

def get_roles(payload: dict) -> list:
    """Cerca i ruoli nel jwt"""
    return payload.get("realm_access", {}).get("roles", [])

def require_role(role: str):
    """Decoratore per proteggere le rotte in base al ruolo"""
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            # g.user esiste già perché @require_auth è passato prima
            if role not in get_roles(g.user):
                # ruolo non trovato -> 403 Forbidden
                return jsonify({"error": "Permesso negato. Non sei autorizzato a visualizzare questa risorsa."}), 403
            
            # ruolo trovato, esegue la route normalmente
            return f(*args, **kwargs)
        return wrapper
    return decorator