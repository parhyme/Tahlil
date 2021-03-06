# Generated by Django 2.2.7 on 2019-12-02 23:44

from django.db import migrations, models
import django.utils.timezone
import questions.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', questions.models.AutoDateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
