# Generated by Django 2.2.17 on 2021-02-09 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a4_candy_cms_contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customformsubmission',
            options={'verbose_name': 'form submission', 'verbose_name_plural': 'form submissions'},
        ),
        migrations.AddField(
            model_name='formfield',
            name='clean_name',
            field=models.CharField(blank=True, default='', help_text='Safe name of the form field, the label converted to ascii_snake_case', max_length=255, verbose_name='name'),
        ),
    ]