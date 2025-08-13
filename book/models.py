from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MinLengthValidator,MaxLengthValidator
from django.urls import reverse
# Create your models here.
genre_choices=[
     ('Fiction', 'Fiction'),
    ('Non-Fiction', 'Non-Fiction'),
    ('Science', 'Science'),
    ('Technology', 'Technology'),
    ('History', 'History'),
    ('Other', 'Other'),
]
class Book(models.Model):
    title=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    description=models.TextField()
    # genre=models.CharField(max_length=30,choices=genre_choices)
    genre=models.CharField(max_length=30,choices=genre_choices, default='Fiction')
    isbn = models.CharField(max_length=13, unique=True)
    publ_date=models.DateField()
    avg_rating=models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[MinLengthValidator(0),MaxLengthValidator(5)],
        blank=True,
        null=True
    )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title # What shows up in admin and shell
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])  # Redirect after create
        












