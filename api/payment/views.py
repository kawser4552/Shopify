from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
import braintree

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id="kycts2ygd2mkbn9x",
        public_key="g2qpkqwg9fpp5pqp",
        private_key="21f55ea874ca4a4a68bf976d66a47c46"
    )
)

def validate_user_session(id,token):
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False


@csrf_exempt
def generate_token(request,id,token):
    if not validate_user_session(id, token):
        return JsonResponse({'error':'Invalid session, Please login again'})

    return JsonResponse({'clienttoken':getway.client_token.generate(),'success':True})


@csrf_exempt
def process_payment(request, id ,token):
    if not validate_user_session(id, token):
        return JsonResponse({'error':'Invalid session, Please login again'})

    nonce_from_the_client = request.POST["paymentMethodNonce"]
    amount_from_the_client = request.POST["amount"]

    result = getway.transaction.sale({
        "amount": amount_from_the_client,
        "payment_method_nonce": nonce_from_the_client,
        "options": {
          "submit_for_settlement": True
    }

    })

    if result.is_success:
        return JsonResponse({
            
            
            "success":result.is_success,
            "transaction":{'id':result.transaction.id,'amount':result.transaction.amount}
        
        
        
        })
    
    else:
        return JsonResponse({'error': True, 'success': False})



