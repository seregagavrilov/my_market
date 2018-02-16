from app import app, db
from app.model import Product


@app.shell_context_processor
def make_shell_context():
    return {'Product': Product, 'db': db}