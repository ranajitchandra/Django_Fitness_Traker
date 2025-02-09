# Generated by Django 5.0.6 on 2024-06-23 23:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calorieApp', '0005_alter_custom_user_gender_alter_custom_user_height_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='foods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('consume', models.CharField(max_length=100, null=True)),
                ('date', models.DateField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
