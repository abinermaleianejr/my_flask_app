from flask import Blueprint, request, jsonify
from app.controllers.mobileWalletController import (
    query_transaction_status_endpoint,
    make_payment_endpoint,
    make_refund_endpoint,
    make_withdraw_endpoint
)

main = Blueprint('main', __name__)

@main.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'GET':
        return jsonify({"message": "GET request received"})
    elif request.method == 'POST':
        data = request.get_json()
        return jsonify({"message": "POST request received", "data": data})

@main.route('/query_transaction_status', methods=['POST'])
def query_transaction_status_route():
    return query_transaction_status_endpoint()

@main.route('/make_payment', methods=['POST'])
def make_payment_route():
    return make_payment_endpoint()

@main.route('/make_refund', methods=['POST'])
def make_refund_route():
    return make_refund_endpoint()

@main.route('/make_withdraw', methods=['POST'])
def make_withdraw_route():
    return make_withdraw_endpoint()
