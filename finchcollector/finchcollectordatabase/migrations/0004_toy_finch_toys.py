# Generated by Django 4.0.6 on 2022-07-20 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finchcollectordatabase', '0003_alter_feeding_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='finch',
            name='toys',
            field=models.ManyToManyField(to='finchcollectordatabase.toy'),
        ),
    ]
