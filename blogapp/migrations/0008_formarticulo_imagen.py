# Generated by Django 4.1.1 on 2022-09-28 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_remove_formarticulo_imagen_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='formarticulo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
