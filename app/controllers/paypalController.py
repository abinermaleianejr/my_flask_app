from flask import request, jsonify
from app.models.paypalTransactions import create_order, capture_order
from app.utils.jwt_utils import decode_token
from jwt import InvalidTokenError

def create_order_endpoint():
    token = request.json.get('token')
     print(token)

    if not token:
        return jsonify({'error': 'Missing token'}), 400

    try:
        payload = decode_token(token, 'oi')
        print(payload)
        amount = payload.get("amount")
        currency = payload.get("currency", "USD")

        if not amount:
            return jsonify({'error': 'Missing amount'}), 400

        response, status = create_order(amount, currency)
        return jsonify(response), status

    except InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def capture_order_endpoint():
    token = request.json.get('token')

    if not token:
        return jsonify({'error': 'Missing token'}), 400

    try:
        payload = decode_token(token, 'oi')
        order_id = payload.get("order_id")

        if not order_id:
            return jsonify({'error': 'Missing order_id'}), 400

        response, status = capture_order(order_id)
        return jsonify(response), status

    except InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

