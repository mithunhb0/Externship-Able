# Generated by Django 3.2 on 2022-02-24 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('user_type', models.CharField(choices=[('sales representative', 'Sales representative'), ('sales admin', 'Sales admin')], default='sales representative', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superadmin', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=False)),
                ('manager_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.account')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]