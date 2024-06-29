from django.contrib import admin
from users.models import Reviews
# Register your models here.


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('author', 'rating', 'comment', 'created_at')
    list_filter = ('author','created_at', 'rating',"updated_at")
    search_fields = ('author', 'rating', 'comment')
