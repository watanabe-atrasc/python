# Generated by Django 2.1.5 on 2019-03-05 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workdata',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
