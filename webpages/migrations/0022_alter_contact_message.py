# Generated by Django 4.0.3 on 2022-03-10 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0021_rename_your_email_contact_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(max_length=1500),
        ),
    ]
