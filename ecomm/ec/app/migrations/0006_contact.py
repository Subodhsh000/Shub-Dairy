# Generated by Django 5.0.1 on 2024-03-19 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('Msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]
