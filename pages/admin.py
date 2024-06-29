from django.contrib import admin
from pages.models import ContactModel,Content,Tag,Category
# Register your models here.


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'services', 'created_at')
    list_filter = ('created_at', 'services')
    search_fields = ('name', 'phone', 'email', 'message', 'services')

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}