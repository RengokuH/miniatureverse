# Generated by Django 4.0.3 on 2022-03-15 06:47

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0029_remove_landingpage_animationtext2'),
    ]

    operations = [
        migrations.AddField(
            model_name='roadmap',
            name='desc',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
