from portalsdk import APIContext, APIMethodType, APIRequest
from config import Config
from pprint import pprint


def make_payment(transaction_reference, customer_msisdn, amount, third_party_reference):
    api_context = APIContext()
    api_context.api_key = Config.API_KEY
    api_context.public_key = Config.PUBLIC_KEY
    api_context.ssl = Config.SSL
    api_context.method_type = APIMethodType.POST
    api_context.address = Config.ADDRESS
    api_context.port = Config.PORT
    api_context.path = Config.PATH

    api_context.add_header('Origin', '*')

    api_context.add_parameter('input_TransactionReference', transaction_reference)
    api_context.add_parameter('input_CustomerMSISDN', customer_msisdn)
    api_context.add_parameter('input_Amount', amount)
    api_context.add_parameter('input_ThirdPartyReference', third_party_reference)
    api_context.add_parameter('input_ServiceProviderCode', Config.service_provider_code)

    api_request = APIRequest(api_context)
    result = api_request.execute()

    response = {
        "status_code": result.status_code,
        "headers": dict(result.headers),
        "body": result.body
    }

    pprint(response)

    return response


def make_refund(transaction_id, security_credential, initiator_identifier, third_party_reference,
                reversal_amount):
    api_context = APIContext()
    api_context.api_key = Config.API_KEY
    api_context.public_key = Config.PUBLIC_KEY
    api_context.ssl = Config.SSL
    api_context.method_type = APIMethodType.PUT
    api_context.address = Config.ADDRESS
    api_context.port = Config.PORT
    api_context.path = Config.PATH

    api_context.add_header('Origin', '*')

    api_context.add_parameter('input_TransactionID', transaction_id)
    api_context.add_parameter('input_SecurityCredential', security_credential)
    api_context.add_parameter('input_InitiatorIdentifier', initiator_identifier)
    api_context.add_parameter('input_ThirdPartyReference', third_party_reference)
    api_context.add_parameter('input_ServiceProviderCode', Config.service_provider_code)
    api_context.add_parameter('input_ReversalAmount', reversal_amount)

    api_request = APIRequest(api_context)
    result = api_request.execute()

    response = {
        "status_code": result.status_code,
        "reason": result.reason,
        "result": result.body,
        "parameters": {key: result.get_parameter(key) for key in result.parameters}
    }

    pprint(response)

    return response


def make_withdraw(transaction_reference, customer_msisdn, amount, third_party_reference):
    api_context = APIContext()
    api_context.api_key = Config.API_KEY
    api_context.public_key = Config.PUBLIC_KEY
    api_context.ssl = Config.SSL
    api_context.method_type = APIMethodType.POST
    api_context.address = Config.ADDRESS
    api_context.port = Config.PORT
    api_context.path = Config.PATH

    api_context.add_header('Origin', '*')

    api_context.add_parameter('input_TransactionReference', transaction_reference)
    api_context.add_parameter('input_CustomerMSISDN', customer_msisdn)
    api_context.add_parameter('input_Amount', amount)
    api_context.add_parameter('input_ThirdPartyReference', third_party_reference)
    api_context.add_parameter('input_ServiceProviderCode', Config.service_provider_code)

    api_request = APIRequest(api_context)
    result = api_request.execute()

    response = {
        "status_code": result.status_code,
        "headers": dict(result.headers),
        "body": result.body
    }

    pprint(response)

    return response


def query_transaction_status(third_party_reference, query_reference):
    api_context = APIContext()
    api_context.api_key = Config.API_KEY
    api_context.public_key = Config.PUBLIC_KEY
    api_context.ssl = Config.SSL
    api_context.method_type = APIMethodType.GET
    api_context.address = Config.ADDRESS
    api_context.port = Config.PORT
    api_context.path = Config.PATH

    api_context.add_header('Origin', '*')

    api_context.add_parameter('input_ThirdPartyReference', third_party_reference)
    api_context.add_parameter('input_QueryReference', query_reference)
    api_context.add_parameter('input_ServiceProviderCode', Config.service_provider_code)

    api_request = APIRequest(api_context)
    result = api_request.execute()

    response = {
        "status_code": result.status_code,
        "headers": dict(result.headers),
        "body": result.body
    }

    pprint(response)

    return response
