from flask_restx import Resource, fields
from app import db, api 
from . import user_ns
from .models import Client


@user_ns.route("/create")
class ClientCreate(Resource):
    #serializers
    client_serializer = api.model(
        "Client",
        {
            "personnel_id": fields.Integer,
        }
    )

    @user_ns.expect(client_serializer)
    def post(self):
        personnel_id = user_ns.payload.get("personnel_id")
        client = Client.get_or_create(personnel_id)
        if type(client) == dict: # if we have err message
            return client
        return {"client_id": client.id, "personnel_id": client.personnel_id}