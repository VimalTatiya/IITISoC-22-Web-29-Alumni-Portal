
from django.contrib import admin
from Home.models import Event
from Home.models import Info
from Home.models import Story

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    fields=(('event_name'),('event_city') , ('start_date' , 'finish_date'),('start_time' , 'finish_time'))
    list_display = ('event_name', 'start_date', 'finish_date')
    empty_value_display = '-empty-'
    list_filter = ('event_city', 'start_date')
    search_fields = ['event_name', 'event_city']
    
class InfoAdmin(admin.ModelAdmin):
    fields=(('name'),('branch','rollnum','yog'),('email','contact'),('current_city'),('status'),('password'))
    list_display = ('name', 'email', 'rollnum')
    empty_value_display = '-empty-'
    list_filter = ('branch', 'yog','current_city')
    search_fields = ['name', 'branch','rollnum','current_city']
    
  
admin.site.register(Story)  
admin.site.register(Info, InfoAdmin) 
admin.site.register(Event, EventAdmin)


  