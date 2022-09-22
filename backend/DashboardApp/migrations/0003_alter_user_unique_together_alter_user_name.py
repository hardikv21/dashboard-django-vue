# Generated by Django 4.1.1 on 2022-09-21 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashboardApp', '0002_alter_user_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]