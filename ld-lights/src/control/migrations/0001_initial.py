# Generated by Django 2.0.1 on 2018-01-17 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Light',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.GenericIPAddressField(default='192.168.178.42')),
                ('port', models.PositiveSmallIntegerField(default=8899)),
                ('red', models.PositiveSmallIntegerField(default=255)),
                ('green', models.PositiveSmallIntegerField(default=255)),
                ('blue', models.PositiveSmallIntegerField(default=255)),
                ('is_on', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='light',
            unique_together={('address', 'port')},
        ),
    ]
