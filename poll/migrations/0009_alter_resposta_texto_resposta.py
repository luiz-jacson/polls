# Generated by Django 4.0.6 on 2022-08-12 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0008_alter_resposta_texto_resposta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resposta',
            name='texto_resposta',
            field=models.CharField(default='', max_length=50, verbose_name='Answers'),
        ),
    ]
