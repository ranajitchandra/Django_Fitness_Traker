# Generated by Django 5.0.6 on 2024-06-23 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calorieApp', '0007_alter_custom_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='gender',
            field=models.CharField(choices=[('female', 'Female'), ('male', 'Male')], max_length=100, null=True),
        ),
    ]
