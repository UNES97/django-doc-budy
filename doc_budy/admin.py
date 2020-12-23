from django.contrib import admin
from doc_budy.models import Patient , Consulation , Rv , Ordonance , Certificat
# Register your models here.

admin.site.register(Patient)
admin.site.register(Consulation)
admin.site.register(Rv)
admin.site.register(Ordonance)
admin.site.register(Certificat)