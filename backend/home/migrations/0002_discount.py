# Generated by Django 2.2.24 on 2021-12-13 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medical', models.BooleanField()),
                ('military', models.BooleanField()),
                ('educational', models.BooleanField()),
            ],
        ),
    ]
