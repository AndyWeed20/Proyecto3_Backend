# Generated by Django 4.2.4 on 2023-12-17 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminario_app', '0007_alter_inscrito_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscrito',
            name='telefono',
            field=models.CharField(max_length=9),
        ),
    ]