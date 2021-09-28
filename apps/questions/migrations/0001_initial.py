# Generated by Django 2.2.6 on 2019-10-24 12:20

import adhocracy4.categories.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('a4modules', '0004_description_maxlength_512'),
        ('a4categories', '0002_category_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(blank=True, editable=False, null=True)),
                ('text', models.TextField(max_length=1000, verbose_name='Question')),
                ('is_answered', models.BooleanField(default=False)),
                ('is_on_shortlist', models.BooleanField(default=False)),
                ('is_hidden', models.BooleanField(default=False)),
                ('is_live', models.BooleanField(default=False)),
                ('category', adhocracy4.categories.fields.CategoryField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='a4categories.Category', verbose_name='Characteristic')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a4modules.Module')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]