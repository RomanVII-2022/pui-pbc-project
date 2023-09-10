from django.contrib import admin
from myapp.models import PendingBeforeCourt, PendingUnderInvestigation, MyUser, PUILog, PBCLog


admin.site.register(PendingBeforeCourt)
admin.site.register(PendingUnderInvestigation)
admin.site.register(MyUser)
admin.site.register(PUILog)
admin.site.register(PBCLog)
