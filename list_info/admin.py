from django.contrib import admin

from list_info.models import Task, Category, Tag



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'created_date', 'category')
    list_filter = ('status', 'created_date', 'category')
    search_fields = ('title', 'description')
    filter_horizontal = ('tags',)
