# Generated by Django 5.0.6 on 2024-06-23 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calorieApp', '0004_alter_custom_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='gender',
            field=models.CharField(choices=[('female', 'Female'), ('male', 'Male')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='custom_user',
            name='height',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='custom_user',
            name='weight',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
