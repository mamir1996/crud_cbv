
from django.db import migrations

def fill_genre(apps, schema_editor):
    Book = apps.get_model('book', 'Book')
    Book.objects.filter(genre__isnull=True).update(genre="Fiction")

class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_book_genre'),  # ⚠️ Update this to your actual previous migration name
    ]

    operations = [
        migrations.RunPython(fill_genre),
    ]

