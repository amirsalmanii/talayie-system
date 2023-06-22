from flask import jsonify, request
from . import user


@user.route('/test', methods=['GET'])
def test_view():
    return jsonify({"messeage":'test-view'})