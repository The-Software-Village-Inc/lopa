# Generated by Django 3.2.9 on 2021-11-28 19:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cause',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=1000)),
                ('initial_frequency', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Consequence',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=1000)),
                ('target_frequency', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UUIDModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=1000)),
                ('target_frequency', models.FloatField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lopa.project')),
            ],
        ),
        migrations.CreateModel(
            name='Consequence_Barrier',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=1000)),
                ('pfd', models.FloatField()),
                ('cause', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lopa.consequence')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lopa.project')),
            ],
        ),
        migrations.AddField(
            model_name='consequence',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lopa.event'),
        ),
        migrations.AddField(
            model_name='consequence',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lopa.project'),
        ),
        migrations.CreateModel(
            name='Cause_Barrier',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=1000)),
                ('pfd', models.FloatField()),
                ('cause', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lopa.cause')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lopa.project')),
            ],
        ),
        migrations.AddField(
            model_name='cause',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lopa.event'),
        ),
        migrations.AddField(
            model_name='cause',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lopa.project'),
        ),
    ]