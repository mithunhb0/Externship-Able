# Generated by Django 3.2 on 2022-02-24 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone_number', models.IntegerField()),
                ('state', models.CharField(max_length=50)),
                ('assigned_to', models.CharField(max_length=50)),
                ('add_remark', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('newlead', 'New Lead'), ('hotlead', 'Hot Lead'), ('medlead', 'Med Lead'), ('greylead', 'Grey Lead'), ('success', 'Success')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]