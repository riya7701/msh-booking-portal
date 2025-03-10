# Generated by Django 3.2.5 on 2021-08-06 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hab_portal', '0011_habmodel_fee_to_be_paid'),
    ]

    operations = [
        migrations.CreateModel(
            name='date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_arrival', models.DateField(verbose_name='Date of Arrival')),
            ],
        ),
        migrations.AlterField(
            model_name='habmodel',
            name='fee_to_be_paid',
            field=models.IntegerField(default=-150, verbose_name='Fee to be Paid'),
        ),
    ]
