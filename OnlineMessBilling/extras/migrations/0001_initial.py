# Generated by Django 2.0.3 on 2018-08-21 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
            ],
        ),
    ]