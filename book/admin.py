from django.contrib import admin
from .models import Book 
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=('id','title','author','description','genre','isbn','created_at','updated_at','publ_date','avg_rating')
