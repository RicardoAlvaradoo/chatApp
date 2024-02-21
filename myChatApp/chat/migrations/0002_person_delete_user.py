# Generated by Django 4.1.7 on 2024-02-19 06:01

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('interest', models.CharField(max_length=50)),
                ('countries', django_countries.fields.CountryField(max_length=2)),
                ('langChosen', models.CharField(choices=[('En', 'English'), ('Sp', 'Spanish'), ('Ger', 'German'), ('Flip', 'Filipino'), ('Jap', 'Japanese')], default='English', max_length=4)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
