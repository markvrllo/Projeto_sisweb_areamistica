# Generated by Django 3.1.3 on 2020-11-30 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysticareaapp', '0003_cartomante_desc_cartomante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartomante',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]