from django.contrib import admin
from django.utils.translation import gettext_lazy as _

# Register your models here.
from main_app.models import *

admin.site.site_header = _('Learning Management')
admin.site.site_title = _('Learning Management')


class RequirementsAdmin(admin.ModelAdmin):
    list_display = ('professional_requirement', 'description', 'type', 'validity')


class SkillsAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'description', 'aircraft_type', 'category')


class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'post', 'certificate_num')


admin.site.register(Requirement, RequirementsAdmin)
admin.site.register(Skill, SkillsAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(ListOfApprovedStaff)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(AircraftType)
admin.site.register(EngineType)
