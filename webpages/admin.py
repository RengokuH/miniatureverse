from django.contrib import admin
from .models import *

# Register your models here.


class PortfolioPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')


admin.site.register(LandingPage)
admin.site.register(RoadmapDesc)
admin.site.register(Collection)
admin.site.register(CollectionsInfo)
admin.site.register(Journey)
admin.site.register(Roadmap)
admin.site.register(OurCollection, PortfolioPageAdmin)
admin.site.register(ComingSoon)
admin.site.register(MyContact)
admin.site.register(Contact, ContactAdmin)



