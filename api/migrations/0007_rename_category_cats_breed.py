# Generated by Django 5.1.1 on 2024-10-03 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_category_breeds_rename_category_breeds_breed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cats',
            old_name='category',
            new_name='breed',
        ),
    ]
