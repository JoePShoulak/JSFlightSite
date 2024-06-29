import ariadne
from flask import Flask, jsonify, request, Response
from ariadne.contrib.federation import make_federated_schema

from resolvers import query, mutation
from scalars import scalars

def main():
    application = Flask(__name__)

    type_defs = ariadne.load_schema_from_path('schemas')
    application.schema = make_federated_schema(type_defs, [query, mutation] + scalars)

    @application.route('/api')
    def api_call() -> Response:
        data = request.get_json()
        success, result = ariadne.graphql_sync(application.schema, data, context_value=request)

        if not success:
            result_code = 400
        elif result.get('errors'):
            result_code = 500
        else:
            result_code = 200

        return jsonify(result), result_code
    
    @application.route('/')
    def main_page() -> Response:
         with open('index.html', 'r') as fp:
              return fp.read(), 200


    application.run('0.0.0.0', 5000, threaded=True)

if __name__ == '__main__':
	main()