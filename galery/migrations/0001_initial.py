# Generated by Django 5.0.6 on 2024-05-22 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fotografia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('legenda', models.CharField(blank=True, max_length=150, null=True)),
                ('descricao', models.TextField()),
                ('foto', models.CharField(max_length=100)),
            ],
        ),
    ]
