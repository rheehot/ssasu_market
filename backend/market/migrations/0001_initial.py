# Generated by Django 3.0.8 on 2020-07-18 08:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('cityid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('road_address', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('latitude', models.FloatField(default=0)),
                ('longitude', models.FloatField(default=0)),
                ('phone', models.CharField(max_length=49, null=True)),
                ('url', models.TextField(null=True)),
                ('image', models.TextField(null=True)),
                ('avg_score', models.FloatField(default=0)),
                ('store_num', models.IntegerField(default=0)),
                ('parking', models.IntegerField(default=0, null=True)),
                ('toilet', models.IntegerField(default=0, null=True)),
                ('cluster_key', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VisitoRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('markets', models.ManyToManyField(related_name='visitors', to='market.Market')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitors', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VisitDatabase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitdatabase', to='market.Market')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('score', models.IntegerField(default=0)),
                ('image', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='market.Market')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Openhour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mon', models.CharField(max_length=50)),
                ('tue', models.CharField(max_length=50)),
                ('wed', models.CharField(max_length=50)),
                ('thu', models.CharField(max_length=50)),
                ('fri', models.CharField(max_length=50)),
                ('sat', models.CharField(max_length=50)),
                ('sun', models.CharField(max_length=50)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='openhour', to='market.Market')),
            ],
        ),
    ]
