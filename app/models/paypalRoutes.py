from flask import Blueprint, jsonify, request
from app.controllers.paypalController import (
    create_order_endpoint,
    capture_order_endpoint
)

paypal_bp = Blueprint('paypal', __name__)
@paypal_bp.route('/paypal', methods=['GET'])
def health_check():
    return jsonify({"message": "PayPal integration is working"})


@paypal_bp.route('/paypal/create_order', methods=['POST'])
def create_order():
    return create_order_endpoint()

@paypal_bp.route('/paypal/capture_order', methods=['POST'])
def capture_order():
    return capture_order_endpoint()

