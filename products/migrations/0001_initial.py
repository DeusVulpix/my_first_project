# Generated by Django 3.1.4 on 2021-01-03 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=3, max_digits=300)),
                ('show', models.BooleanField(default=False)),
                ('summary', models.TextField()),
            ],
        ),
    ]
