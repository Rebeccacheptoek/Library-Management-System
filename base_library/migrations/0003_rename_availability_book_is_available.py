# Generated by Django 4.2.1 on 2023-06-22 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_library', '0002_alter_book_availability_alter_member_penalty_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='availability',
            new_name='is_available',
        ),
    ]
