# Generated by Django 4.2.1 on 2023-05-25 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0008_alter_filter_price_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('subject', models.CharField(max_length=300)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='filter_price',
            name='price',
            field=models.CharField(choices=[('15000 to 20000', '15000 to 20000'), ('10000 to 15000', '10000 to 15000'), ('5000 to 10000', '5000 to 10000'), ('20000 to 30000', '20000 to 30000'), ('100 to 5000', '100 to 5000')], max_length=60),
        ),
    ]
