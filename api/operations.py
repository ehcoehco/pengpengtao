from django.shortcuts import get_object_or_404
from pengpengtao.models.models import UserDeal, Deal, Merchant , MerchantDeal, User 

def get_deal_by_id(id):
    deal = get_object_or_404(Deal, pk=id)

def get_user_by_id(id):
    user = get_object_or_404(Deal, pk=id)

def get_deal_list_of_user(user):
    #bad
    deal_list = []
    deal_list = UserDeal.object.filter(user=user)# can only get the deal part
    return deal_list

def get_deal_list_by_state(user, state):
    state_deal_list = []
    state_deal_list = UserDeal.object.filter(user=user, state=state)

    return state_deal_list
