from django.contrib import admin

from adhocracy4.projects.admin import ProjectAdminFilter

from . import models


class ChoiceInline(admin.TabularInline):
    model = models.APlusChoice


class ProjectFilter(ProjectAdminFilter):
    project_key = 'poll__module__project'


@admin.register(models.APlusQuestion)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        ChoiceInline
    ]
    list_filter = (
        'poll__module__project__organisation',
        'poll__module__project__is_archived',
        ProjectFilter
    )
    date_hierarchy = 'poll__created'
    search_fields = ('label',)
