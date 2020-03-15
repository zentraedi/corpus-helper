from flask import Blueprint, jsonify
from .models import Corpus

# Define the blueprint
mod_corpus = Blueprint('corpus', __name__)


@mod_corpus.route('/all', methods=['GET'])
def records():
    data = Corpus.datatables()
    print(data)
    # output = {'data': data}
    return jsonify(data)
