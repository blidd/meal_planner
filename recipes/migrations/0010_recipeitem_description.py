# Generated by Django 2.2.1 on 2019-07-07 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_auto_20190707_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeitem',
            name='description',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]