# Generated by Django 3.2.5 on 2021-07-06 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('years', models.IntegerField()),
                ('wage', models.FloatField()),
                ('office', models.CharField(choices=[('Gerente', 'Gerente'), ('Dev Back-End', 'Dev Back-End'), ('Dev Front-End', 'Dev Front-End'), ('Estagiario', 'Estagiario')], default='Estagiario', max_length=50)),
            ],
        ),
    ]