# Generated by Django 4.0.3 on 2022-03-10 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0024_contact_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
