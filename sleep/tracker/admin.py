# Cofiguring the admin file to manage the models(perform data management tasks efficiently)

# Register your models here.
from django.contrib import admin
from .models import SleepSession, SleepGoal


@admin.register(SleepGoal)
class SleepGoalAdmin(admin.ModelAdmin):
    list_display = ("user", "target_hours", "target_bedtime", "target_waketime", "updated_at")


@admin.register(SleepSession)
class SleepSessionAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('user', 'start', 'end', 'duration_hours','quality','awakenings', 'meets_goal', 'notes',  'created_at')

    # Fields to filter by
    list_filter = ('user', 'start', 'quality', 'tags')
    
    # Fields to search
    search_fields = ('user__username', 'notes', 'tags')
    
    # Default ordering
    ordering = ('-start',)
    
    # Read-only fields (including computed property)
    readonly_fields = ('created_at', 'updated_at', 'duration_hours')
    
    # Fields to display in the detail view (form)
    fields = (
        'user', 'start', 'end', 'notes', 'quality', 
        'latency_minutes', 'awakenings', 'tags', 
        'stages_json', 'created_at', 'updated_at', 
        'duration_hours'
    )
    
    # Number of items per page
    list_per_page = 20
    
    # Optional: Customizing the display of duration_hours
    def duration_hours(self, obj):
        return obj.duration_hours
    duration_hours.short_description = 'Duration (hours)'