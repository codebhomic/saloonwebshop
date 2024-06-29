from django.db import models
from django.contrib.auth.models import User

# class UserEdit(User):
#     phone = models.PhoneNumberField(_(""))

# Create your models here.
class Reviews(models.Model):
    author = models.CharField(max_length=100)  # Name or username of the reviewer
    email = models.EmailField(blank=True,null=True)  # Email of the reviewer (optional)
    phone = models.IntegerField(blank=True,null=True)  # Phone number of reviewer
    rating = models.IntegerField()  # Rating given by the reviewer (e.g., 1 to 5 stars)
    comment = models.TextField()  # Review text
    created_at = models.DateTimeField(auto_now_add=True)  # Date and time when the review was submitted
    updated_at = models.DateTimeField(auto_now=True)  # Date and time when the review was edited

    def __repr__(self) -> str:
        return f'author: {self.author}, rating: {self.rating}, comment: {self.comment}'
    
    def __str__(self):
        return f'author: {self.author}, rating: {self.rating}, comment: {self.comment}'