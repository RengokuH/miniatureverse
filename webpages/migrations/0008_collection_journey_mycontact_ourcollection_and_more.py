# Generated by Django 4.0.2 on 2022-03-08 15:00

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0007_alter_collectionsinfo_floor_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_title', models.CharField(max_length=255)),
                ('desc', ckeditor.fields.RichTextField()),
                ('photo', models.ImageField(blank=True, upload_to='media/about/')),
            ],
        ),
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('desc', ckeditor.fields.RichTextField()),
                ('photo1', models.ImageField(blank=True, upload_to='media/about/')),
                ('photo2', models.ImageField(blank=True, upload_to='media/about/')),
                ('photo3', models.ImageField(blank=True, upload_to='media/about/')),
                ('photo4', models.ImageField(blank=True, upload_to='media/about/')),
            ],
        ),
        migrations.CreateModel(
            name='MyContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='OurCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.CharField(blank=True, default='', max_length=150)),
                ('photo1', models.ImageField(upload_to='media/projects/')),
                ('photo2', models.ImageField(blank=True, upload_to='media/projects/')),
                ('photo3', models.ImageField(blank=True, upload_to='media/projects/')),
                ('photo4', models.ImageField(blank=True, upload_to='media/projects/')),
                ('photo5', models.ImageField(blank=True, upload_to='media/projects/')),
                ('img_link', models.CharField(default='', max_length=255)),
                ('opensea_link', models.CharField(default='', max_length=1500)),
            ],
        ),
        migrations.RenameModel(
            old_name='Services',
            new_name='ComingSoon',
        ),
        migrations.RenameModel(
            old_name='Resume',
            new_name='Roadmap',
        ),
        migrations.DeleteModel(
            name='My_Contact',
        ),
        migrations.DeleteModel(
            name='Portfoliodesc',
        ),
        migrations.DeleteModel(
            name='PortfolioPage',
        ),
        migrations.DeleteModel(
            name='Resume_Desc',
        ),
        migrations.DeleteModel(
            name='ServicesDesc',
        ),
        migrations.DeleteModel(
            name='Skill_Desc',
        ),
        migrations.DeleteModel(
            name='SkillValue',
        ),
        migrations.RenameField(
            model_name='landingpage',
            old_name='discord_url',
            new_name='linktree_url',
        ),
        migrations.RenameField(
            model_name='landingpage',
            old_name='fb_url',
            new_name='opensea_url',
        ),
        migrations.RemoveField(
            model_name='collectionsinfo',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='collectionsinfo',
            name='end_desc',
        ),
        migrations.RemoveField(
            model_name='collectionsinfo',
            name='floor_price',
        ),
        migrations.RemoveField(
            model_name='collectionsinfo',
            name='items',
        ),
        migrations.RemoveField(
            model_name='collectionsinfo',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='collectionsinfo',
            name='twitter_url',
        ),
        migrations.RemoveField(
            model_name='collectionsinfo',
            name='volume_traded',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='your_name',
        ),
    ]
