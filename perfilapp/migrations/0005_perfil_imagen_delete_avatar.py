# Generated by Django 4.1.1 on 2022-09-28 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfilapp', '0004_rename_user_avatar_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
        migrations.DeleteModel(
            name='Avatar',
        ),
    ]
