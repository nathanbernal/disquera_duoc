# Generated by Django 2.2.7 on 2019-11-28 18:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('audiodog', '0003_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paisId', models.IntegerField()),
                ('pais', models.CharField(max_length=100)),
                ('gentilicio', models.TextField(max_length=100)),
                ('registro_fecha', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regionId', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('registro_fecha', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='cancion',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audiodog.Pais'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audiodog.Region'),
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudadId', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('registro_fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audiodog.Region')),
            ],
        ),
    ]