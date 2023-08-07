from flask_restful import Resource, reqparse
from models.hotel import HotelModel
from models.site import SiteModel
from resources.filtros import normalize_path_params
from flask_jwt_extended import jwt_required
import sqlite3


#path /hoteis?cidade= Rio de Janeiro&estrelas_min=4&diaria_max=400

class Hoteis(Resource):
    query_params = reqparse.RequestParser()
    query_params.add_argument("cidade", type=str, default="", location="args")
    query_params.add_argument("estrelas_min", type=float, default=0, location="args")
    query_params.add_argument("estrelas_max", type=float, default=0, location="args")
    query_params.add_argument("diaria_min", type=float, default=0, location="args")
    query_params.add_argument("diaria_max", type=float, default=0, location="args")

    def get(self):
        filters = Hoteis.query_params.parse_args()

        query = HotelModel.query

        if filters["cidade"]:
            query = query.filter(HotelModel.cidade == filters["cidade"])
        if filters["estrelas_min"]:
            query = query.filter(HotelModel.estrelas >= filters["estrelas_min"])
        if filters["estrelas_max"]:
            query = query.filter(HotelModel.estrelas <= filters["estrelas_max"])
        if filters["diaria_min"]:
            query = query.filter(HotelModel.diaria >= filters["diaria_min"])
        if filters["diaria_max"]:
            query = query.filter(HotelModel.diaria <= filters["diaria_max"])

        return {"hoteis": [hotel.json() for hotel in query]}

        for linha in resultado:
            hoteis.append({
            "hotel_id": linha[0],
            "nome": linha[1],
            "estrelas": linha[2],
            "diaria": linha[3],
            "cidade": linha[4],
            'site_id':linha[5]
            })

        return {'hoteis': hoteis}
class Hotel(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('nome', type=str, required=True, help="The field 'nome' cannot be left blank")
    atributos.add_argument('estrelas')
    atributos.add_argument('diaria')
    atributos.add_argument('cidade')
    atributos.add_argument('site_id', type=int, required=True, help="Every hotel needs to be linked with a site.")

    def get(self, hotel_id):
        hotels = HotelModel.find_hotel(hotel_id)
        if hotels:
            return hotels.json()
        return {'message': 'No hotels found.'}, 404

    @jwt_required()
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {"message": "Hotel id '{}' already exists.".format(hotel_id)}, 400  # bad request
        dados = Hotel.atributos.parse_args()
        hotel = HotelModel(hotel_id, **dados)

        if not SiteModel.find_by_id(dados['site_id']):
            return {'message': 'The hotel must be associated to a valid site id. '}, 400

        try:
            hotel.save_hotel()
        except:
            return {'message': 'An internal error occurred trying to save hotel.'}, 500  # Internal server error
        return hotel.json()

    @jwt_required()
    def put(self, hotel_id):
        dados = Hotel.atributos.parse_args()
        hotel_enontrado = HotelModel.find_hotel(hotel_id)
        if hotel_enontrado:
            hotel_enontrado.update_hotel(**dados)
            hotel_enontrado.save_hotel()
            return hotel_enontrado.json(), 200  # OK
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'message': 'An internal error occurred trying to save hotel.'}, 500  # Internal server error
        return hotel.json(), 201  # created criado

    @jwt_required()
    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return {'message': 'An error occurred trying to delete.'}, 500
            return {'message': 'Hotel deleted.'}
        return {'message': 'Hotel not found.'}, 404