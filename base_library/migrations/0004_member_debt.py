# Generated by Django 4.2.1 on 2023-06-22 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_library', '0003_rename_availability_book_is_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='debt',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
    ]