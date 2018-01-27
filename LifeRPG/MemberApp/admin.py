from django.contrib import admin
from .models import(Aspect, UserAspect, IntakeQuestion, UserIntakeQuestion,
                    Mission, UserMissionRating, MissionAspect)


class AspectAdmin(admin.ModelAdmin):
    list_display = ['name']


class UserAspectAdmin(admin.ModelAdmin):
    list_display = ['user', 'aspect_name',
                    'points']

    def aspect_name(self, obj):
        return obj.aspect.name


class IntakeQuestionAdmin(admin.ModelAdmin):
    list_display = ['question']


class UserMissionRatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'log_time' 'mission_title',
                    'rating']

    def mission_title(self, obj):
        return obj.mission.title


class MissionAdmin(admin.ModelAdmin):
    list_display = ['title']


class MissionAspectAdmin(admin.ModelAdmin):
    list_display = ['mission_title', 'aspect_name']

    def mission_title(f, obj):
        return obj.mission.title

    def aspect_name(f, obj):
        return obj.aspect.name


admin.site.register(Aspect, AspectAdmin)
admin.site.register(UserAspect, UserAspectAdmin)
admin.site.register(IntakeQuestion, IntakeQuestionAdmin)
admin.site.register(UserIntakeQuestion)
admin.site.register(UserMissionRating,)
admin.site.register(Mission, MissionAdmin)
admin.site.register(MissionAspect, MissionAspectAdmin)
