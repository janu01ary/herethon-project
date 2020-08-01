# Generated by Django 3.0.8 on 2020-08-01 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hereapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('score', models.IntegerField()),
                ('division', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='email',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
