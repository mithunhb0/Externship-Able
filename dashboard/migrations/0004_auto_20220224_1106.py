# Generated by Django 3.2 on 2022-02-24 05:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0003_lead_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[('newlead', 'New Lead'), ('hotlead', 'Hot Lead'), ('medlead', 'Med Lead'), ('greylead', 'Grey Lead'), ('success', 'Success')], default='newlead', max_length=50),
        ),
        migrations.CreateModel(
            name='Remark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('remark_area', models.CharField(max_length=100)),
                ('lead_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.lead')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]