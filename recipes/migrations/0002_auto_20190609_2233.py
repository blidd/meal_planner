# Generated by Django 2.2.1 on 2019-06-09 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instruction',
            name='step_num',
            field=models.IntegerField(),
        ),
    ]