from django.contrib import admin

# Register your models here.



from .models import list_name , ver , log   , logins


admin.site.register(list_name)
admin.site.register(ver)
admin.site.register(log)
admin.site.register(logins)