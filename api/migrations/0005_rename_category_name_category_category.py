# Generated by Django 5.1.1 on 2024-10-03 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_categories_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='category',
        ),
    ]
