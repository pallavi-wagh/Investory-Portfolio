# Generated by Django 5.0.3 on 2024-05-05 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_alter_investment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='image',
            field=models.ImageField(upload_to='statc/images'),
        ),
    ]
