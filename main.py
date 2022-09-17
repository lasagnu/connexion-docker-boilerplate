import connexion
import os
from typing import Tuple

from models.messages import DefaultMessage

def healthcheck() -> Tuple[str, int]:
    msg = DefaultMessage('ok').serialize()
    return msg, 200

 
SECRET_KEY = os.environ.get('SECRET')
if not SECRET_KEY:
    raise ValueError('No SECRET env var set for Flask application.')

app = connexion.FlaskApp(__name__, port=8080, specification_dir='openapi/', debug=True)
app.add_api('spec.yaml', resolver_error=501)
app.app.secret_key = SECRET_KEY

if __name__ == '__main__':
    app.run()
