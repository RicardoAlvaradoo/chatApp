# Generated by Django 4.1.7 on 2024-02-01 21:05

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('interest', models.CharField(max_length=50)),
                ('countries', django_countries.fields.CountryField(max_length=2)),
                ('langChosen', models.CharField(choices=[('En', 'English'), ('Sp', 'Spanish'), ('Ger', 'German'), ('Flip', 'Filipino'), ('Jap', 'Japanese')], default='English', max_length=4)),
            ],
        ),
    ]
