# Generated by Django 3.0 on 2019-12-09 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(default='', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
