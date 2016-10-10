from django.contrib import admin
from django.forms import ModelForm
from .models import Institution, Person, Reunion
from suit.widgets import SuitDateWidget, SuitTimeWidget
from suit_ckeditor.widgets import CKEditorWidget
# Register your models here.
from . import views
from django.conf.urls import url

class PersonAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone", "mobile", "email", "institution")


class ReunionChangeForm(ModelForm):

    class Meta:
        model = Reunion
        fields = ('place', 'date', 'time_start', 'time_end', 'subject', 'participants', 'pv')
        widgets = {
            "date" : SuitDateWidget,
            "time_start" : SuitTimeWidget,
            "time_end" : SuitTimeWidget,
            "pv" : CKEditorWidget,
        }

class ReunionAdmin(admin.ModelAdmin):
    form = ReunionChangeForm
    filter_horizontal = ('participants',)
    list_display = ("subject", "date", "place")

    def get_urls(self):
        urls = super(ReunionAdmin, self).get_urls()
        my_urls = [
            url(r'^(\d+)/change/print/$', views.home, name='print_pv'),
        ]
        return my_urls + urls

admin.site.register(Institution)
admin.site.register(Person, PersonAdmin)
admin.site.register(Reunion, ReunionAdmin)
