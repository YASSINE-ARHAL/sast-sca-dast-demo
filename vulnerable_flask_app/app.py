import os
import secrets
import subprocess
from flask import Flask, request, render_template_string
from markupsafe import escape

app = Flask(__name__)

# La clé doit être définie dans l'environnement en production.
app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY") or secrets.token_hex(32)


@app.route("/")
def index():
    return """
    <h1>Welcome to our Flask App</h1>
    <ul>
        <li><a href="/hello?name=World">Hello Page</a></li>
        <li><a href="/execute?cmd=date">Execute an allowed command</a></li>
        <li><a href="/admin">Admin Area</a></li>
    </ul>
    """


@app.route("/hello")
def hello():
    name = request.args.get("name", "Guest")
    return render_template_string(
        "<h1>Hello Page</h1><p>Hello, {{ name }}!</p>"
        '<p><a href="/">Back to Homepage</a></p>',
        name=name,
    )


@app.route("/execute")
def execute():
    # Liste blanche : aucune commande fournie librement par l'utilisateur.
    allowed_commands = {
        "date": ["date"],
        "uptime": ["uptime"],
    }

    command_name = request.args.get("cmd", "date")
    if command_name not in allowed_commands:
        return "Commande non autorisée.", 400

    try:
        result = subprocess.run(
            allowed_commands[command_name],
            shell=False,
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
    except (subprocess.SubprocessError, OSError):
        app.logger.exception("Échec de la commande autorisée")
        return "Impossible d'exécuter la commande.", 500

    return render_template_string(
        "<h1>Résultat</h1><pre>{{ output }}</pre>"
        '<p><a href="/">Back to Homepage</a></p>',
        output=result.stdout if result.returncode == 0 else result.stderr,
    )


@app.route("/admin")
def admin():
    # Cette page de démonstration n'est pas une véritable zone admin.
    return """
    <h1>Admin Area</h1>
    <p>Aucun secret n'est affiché ici.</p>
    <p>Attention : une véritable zone d'administration doit exiger une authentification.</p>
    <p><a href="/">Back to Homepage</a></p>
    """


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")

