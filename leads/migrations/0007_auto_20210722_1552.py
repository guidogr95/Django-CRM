# Generated by Django 3.1.4 on 2021-07-22 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0006_category_organisation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leads.userprofile'),
        ),
    ]
