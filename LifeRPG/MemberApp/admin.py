from django.contrib import admin
from .models import(Aspect, UserAspect, IntakeQuestion, UserIntakeQuestion, Mission, UserMissionRatings)


class AspectAdmin(admin.ModelAdmin):
    list_display = ['name']


class UserAspectAdmin(admin.ModelAdmin):
    list_display = ['points', 'user']


class IntakeQuestionAdmin(admin.ModelAdmin):
    list_display = ['question']


admin.site.register(Aspect, AspectAdmin)
admin.site.register(UserAspect, UserAspectAdmin)
admin.site.register(IntakeQuestion, IntakeQuestionAdmin)
admin.site.register(UserIntakeQuestion)
admin.site.register(UserMissionRatings)
admin.site.register(Mission)
