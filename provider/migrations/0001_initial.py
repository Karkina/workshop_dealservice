# Generated by Django 2.1.7 on 2021-10-28 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('montant', models.CharField(max_length=100000000)),
                ('zone', models.CharField(max_length=10)),
                ('devise', models.CharField(max_length=20)),
                ('brower', models.CharField(max_length=100)),
                ('lender', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
