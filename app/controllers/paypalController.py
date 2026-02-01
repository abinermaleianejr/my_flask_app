from flask import request, jsonify
from app.models.paypalTransactions import create_order, capture_order

# ==========================
# Endpoint para criar pedido
# ==========================
def create_order_endpoint():
    token_data = request.json.get('token')
    print("Dados recebidos:", token_data)

    if not token_data:
        return jsonify({'error': 'Missing token'}), 400

    try:
        # Se futuramente usar JWT, aqui você faria decode:
        # payload = decode_token(token_data)
        # amount = payload.get("amount")
        # currency = payload.get("currency", "USD")

        # Pegando direto do JSON enviado pelo Node
        amount = token_data.get("amount")
        currency = token_data.get("currency", "USD")

        if not amount:
            return jsonify({'error': 'Missing amount'}), 400

        response, status = create_order(amount, currency)
        return jsonify(response), status

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ==========================
# Endpoint para capturar pedido
# ==========================
def capture_order_endpoint():
    token_data = request.json.get('token')
    print("Dados recebidos:", token_data)

    if not token_data:
        return jsonify({'error': 'Missing token'}), 400

    try:
        # Pegando orderId direto do JSON enviado pelo Node
        order_id = token_data.get("orderId")

        if not order_id:
            return jsonify({'error': 'Missing orderId'}), 400

        response, status = capture_order(order_id)
        return jsonify(response), status

    except Exception as e:
        return jsonify({'error': str(e)}), 500
