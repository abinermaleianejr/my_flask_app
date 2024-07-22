from app.models.transactionsMobileWallet import query_transaction_status, make_refund, make_withdraw, make_payment
from app.utils.jwt_utils import decode_token
from flask import request, jsonify
from jwt import InvalidTokenError


# Endpoint para consulta do estado da transação
def query_transaction_status_endpoint():
    token = request.json.get('token')

    if not token:
        return jsonify({'error': 'Missing token'}), 400

    try:
        payload = decode_token(token)
        third_party_reference = payload.get('third_party_reference')
        query_reference = payload.get('query_reference')
        service_provider_code = payload.get('service_provider_code')

        if not (third_party_reference and query_reference and service_provider_code):
            return jsonify({'error': 'Missing required parameters in token'}), 400

        response = query_transaction_status(third_party_reference, query_reference)
        return jsonify(response), response['status_code']

    except InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def make_payment_endpoint():
    token = request.json.get('token')
    print(token)

    if not token:
        return jsonify({'error': 'Missing token'}), 400

    try:
        payload = decode_token(token, 'oi')
        transaction_reference = payload.get('transaction_reference')
        customer_msisdn = payload.get('customer_msisdn')
        amount = payload.get('amount')
        third_party_reference = payload.get('third_party_reference')

        if not (transaction_reference and customer_msisdn and amount and third_party_reference):
            return jsonify({'error': 'Missing required parameters in token'}), 400

        response = make_payment(transaction_reference, customer_msisdn, amount, third_party_reference)
        print(response)
        return jsonify(response), response['status_code']

    except InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def make_refund_endpoint():
    token = request.json.get('token')

    if not token:
        return jsonify({'error': 'Missing token'}), 400

    try:
        payload = decode_token(token)
        transaction_id = payload.get('transaction_id')
        security_credential = payload.get('security_credential')
        initiator_identifier = payload.get('initiator_identifier')
        third_party_reference = payload.get('third_party_reference')
        service_provider_code = payload.get('service_provider_code')
        reversal_amount = payload.get('reversal_amount')

        if not (
                transaction_id and security_credential and initiator_identifier and third_party_reference and reversal_amount):
            return jsonify({'error': 'Missing required parameters in token'}), 400

        response = make_refund(transaction_id, security_credential, initiator_identifier, third_party_reference,
                               reversal_amount)
        return jsonify(response), response['status_code']

    except InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def make_withdraw_endpoint():
    token = request.json.get('token')

    if not token:
        return jsonify({'error': 'Missing token'}), 400

    try:
        payload = decode_token(token)
        transaction_reference = payload.get('transaction_reference')
        customer_msisdn = payload.get('customer_msisdn')
        amount = payload.get('amount')
        third_party_reference = payload.get('third_party_reference')
        service_provider_code = payload.get('service_provider_code')

        if not (transaction_reference and customer_msisdn and amount and third_party_reference):
            return jsonify({'error': 'Missing required parameters in token'}), 400

        response = make_withdraw(transaction_reference, customer_msisdn, amount, third_party_reference)
        return jsonify(response), response['status_code']

    except InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
