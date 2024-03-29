# Generated by Django 3.0.2 on 2020-01-12 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='', max_length=20)),
                ('follower', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baseurl', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('date_uploaded', models.DateTimeField(auto_now=True)),
                ('owner', models.CharField(max_length=20)),
                ('likes', models.IntegerField()),
                ('caption', models.CharField(default='', max_length=140)),
                ('tags', models.IntegerField(default=0)),
                ('main_colour', models.CharField(default='', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoLikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postid', models.IntegerField()),
                ('liker', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photoid', models.IntegerField()),
                ('coords', models.CharField(max_length=20)),
                ('tagged_user', models.CharField(default='', max_length=20)),
                ('tagged_by', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('sign_up_date', models.DateTimeField(auto_now=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('profilepic', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
