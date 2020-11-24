# Generated by Django 3.1.2 on 2020-10-27 20:44

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('learning_graph', '0002_auto_20201011_0828'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('telephone', models.CharField(max_length=10)),
                ('residence', models.CharField(max_length=50)),
                ('level_education', models.CharField(max_length=50)),
                ('college', models.CharField(max_length=50)),
                ('college_career', models.CharField(max_length=50)),
                ('subjects', models.ManyToManyField(max_length=5, to='learning_graph.Subject')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]