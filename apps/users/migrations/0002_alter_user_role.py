# Generated by Django 5.1 on 2024-09-04 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('SA', 'Super Admin'), ('A', 'Admin'), ('DB', 'Delivery Boy'), ('ST', 'Staff')], default='ST', max_length=2),
        ),
    ]
