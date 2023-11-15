# Generated by Django 4.2.7 on 2023-11-15 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServicePassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('password', models.TextField()),
            ],
        ),
    ]