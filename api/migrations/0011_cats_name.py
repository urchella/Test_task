# Generated by Django 5.1.1 on 2024-10-04 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_cats_owner_delete_owners'),
    ]

    operations = [
        migrations.AddField(
            model_name='cats',
            name='name',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
