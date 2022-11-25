from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

from .models import Account

class AccountBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        username = kwargs['username']
        password = kwargs['password']
        try:
            usr = Account.objects.get(username=username)
            
            if usr.check_password(password) is True:
                return usr
        except Account.DoesNotExist:
            pass
    @staticmethod
    def get_user(id_):
        try:
            return Account.objects.get(pk=id_) # <-- tried to get by email here
        except Account.DoesNotExist:
            return None