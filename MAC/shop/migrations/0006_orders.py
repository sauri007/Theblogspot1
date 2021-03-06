# Generated by Django 3.0.7 on 2020-07-08 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200705_0106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_JSON', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=70)),
                ('email', models.CharField(default='', max_length=70)),
                ('address', models.CharField(max_length=70)),
                ('city', models.CharField(default='', max_length=500)),
                ('state', models.CharField(default='', max_length=500)),
                ('phone', models.IntegerField(default=91)),
                ('zip_code', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
