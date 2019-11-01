from flask import Flask, request, jsonify, make_response
from flask import current_app as app
from app.models import GeneAutoComplete, db
from sqlalchemy import func


# Will automatically return 405 for all except get
@app.route('/<name>', defaults={'species': None}, methods=['GET'])
@app.route('/<name>/<species>', methods=['GET'])
def searchGene(name, species):

    # name = request.args.get('name')
    # species = request.args.get('species')

    if len(name) >= 3:
        try:
            # print(db)
            # print(app)

            if species:
                genes = GeneAutoComplete.query.filter(func.lower(GeneAutoComplete.display_label).startswith(func.lower(name)), GeneAutoComplete.species == species).all()
            else:
                genes = GeneAutoComplete.query.filter(func.lower(GeneAutoComplete.display_label).startswith(func.lower(name))).all()
            output = []
            for gene in genes:
                output.append({
                    'id' : gene.stable_id,
                    'name' : gene.display_label,
                    'species' : gene.species
                })

            return jsonify(result=output), 200
        except:
            return 'Unable to execute query', 400
    else:
        return 'Query parameters do not satisfy requirements', 400


@app.route('/', methods=['GET'])
def welcome():
    return ' Welcome to Search Gene API.', 200
