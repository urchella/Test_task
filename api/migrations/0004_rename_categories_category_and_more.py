# Generated by Django 5.1.1 on 2024-10-03 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_categories_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='category_name',
        ),
    ]
