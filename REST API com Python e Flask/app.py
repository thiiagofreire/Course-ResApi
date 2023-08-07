from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Hoteis(Resource): # Hoteis e uma classe que tem recursos, sempre vai ter get,post,put,delete
    def get(self):
        return {'hoteis': 'meus hoteis'}

api.add_resource(Hoteis, '/hoteis')

if __name__ == '__main__':
    app.run(debug=False)

