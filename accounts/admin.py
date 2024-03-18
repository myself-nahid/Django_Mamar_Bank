from django.contrib import admin
from .models import UserBankAccount, UserAddress
# Register your models here.
# admin name: nahid
# admin password: nahid9613
admin.site.register(UserBankAccount)
admin.site.register(UserAddress)
