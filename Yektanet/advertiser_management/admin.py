from django.contrib import admin
from .models import Advertiser,Ad,Click,View

admin.site.register(Ad)
admin.site.register(Advertiser)
admin.site.register(Click)
admin.site.register(View)
# Register your models here.
