# Generated by Django 2.1.2 on 2018-10-03 23:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikesToUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Likes')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='likes',
            name='userRef',
            field=models.ManyToManyField(through='home.LikesToUsers', to=settings.AUTH_USER_MODEL),
        ),
    ]
