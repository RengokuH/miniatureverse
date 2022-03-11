# Generated by Django 3.1 on 2021-03-03 18:03

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', ckeditor.fields.RichTextField()),
                ('dev_title', models.CharField(max_length=255)),
                ('dev_desc', ckeditor.fields.RichTextField()),
                ('dob', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=1000)),
                ('phone', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('degree', models.CharField(max_length=100)),
                ('email', models.EmailField(default='singhalabhya32@gmail.com', max_length=254)),
                ('freelance', models.CharField(default='Available', max_length=100)),
                ('end_desc', ckeditor.fields.RichTextField()),
                ('photo', models.ImageField(default='', upload_to='media/about/')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(max_length=255)),
                ('your_email', models.CharField(max_length=500)),
                ('subject', models.CharField(max_length=255)),
                ('message', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('iam', models.CharField(max_length=255)),
                ('fb_url', models.CharField(default='', max_length=1000)),
                ('insta_url', models.CharField(default='', max_length=1000)),
                ('github_url', models.CharField(default='', max_length=1000)),
                ('li_url', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Portfoliodesc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(choices=[('Web', 'Web'), ('App', 'App')], default='', max_length=255)),
                ('type', models.CharField(choices=[('web', 'web'), ('app', 'app'), ('active', 'active')], max_length=255)),
                ('date', models.CharField(blank=True, default='', max_length=150)),
                ('photo', models.ImageField(upload_to='media/projects/')),
                ('photo1', models.ImageField(blank=True, upload_to='media/projects/')),
                ('photo2', models.ImageField(blank=True, upload_to='media/projects/')),
                ('img_link', models.CharField(default='', max_length=255)),
                ('detail_link', models.CharField(default='', max_length=1500)),
                ('desc', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle1', models.CharField(max_length=255)),
                ('date1', models.CharField(blank=True, max_length=255)),
                ('desc1', ckeditor.fields.RichTextField()),
                ('subtitle2', models.CharField(blank=True, max_length=255)),
                ('date2', models.CharField(blank=True, max_length=255)),
                ('desc2', ckeditor.fields.RichTextField()),
                ('subtitle3', models.CharField(blank=True, max_length=255)),
                ('date3', models.CharField(blank=True, max_length=255)),
                ('desc3', ckeditor.fields.RichTextField()),
                ('subtitle4', models.CharField(blank=True, max_length=255)),
                ('date4', models.CharField(blank=True, max_length=255)),
                ('desc4', ckeditor.fields.RichTextField()),
                ('subtitle5', models.CharField(blank=True, max_length=255)),
                ('date5', models.CharField(blank=True, max_length=255)),
                ('desc5', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Resume_Desc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(blank=True, max_length=255)),
                ('photo', models.ImageField(blank=True, upload_to='media/services/')),
            ],
        ),
        migrations.CreateModel(
            name='ServicesDesc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill_Desc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='SkillValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=100)),
                ('skillvalue', models.IntegerField(default=0)),
            ],
        ),
    ]
