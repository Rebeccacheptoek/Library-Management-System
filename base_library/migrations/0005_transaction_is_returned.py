# Generated by Django 4.2.1 on 2023-06-22 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_library', '0004_member_debt'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='is_returned',
            field=models.BooleanField(default=False),
        ),
    ]