# Generated by Django 3.1.6 on 2021-02-09 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import metas.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('VEL', 'Vocal Ejecutivo de Junta Local'), ('VSL', 'Vocal Secretario de Junta Local'), ('VRL', 'Vocal del RFE de Junta Local'), ('VCL', 'Vocal de Capacitación de Junta Local'), ('VOL', 'Vocal de Organización de Junta Local'), ('VED', 'Vocal Ejecutivo de Junta Distrital'), ('VSD', 'Vocal Secretario de Junta Distrital'), ('VRD', 'Vocal del RFE de Junta Distrital'), ('VCD', 'Vocal de Capacitación de Junta Distrital'), ('VOD', 'Vocal de Organización de Junta Distrital'), ('JOSA', 'JOSA'), ('JOSAD', 'JOSAD'), ('JMM', 'Jefe de Monitoreo a Módulos'), ('JOCE', 'Jefe de Cartografía'), ('RA', 'Rama Administrativa')], max_length=6, verbose_name='Cargo')),
                ('key', models.CharField(max_length=6, verbose_name='Clave de la Meta')),
                ('short_name', models.CharField(max_length=50, verbose_name='Identificación')),
                ('year', models.PositiveIntegerField(verbose_name='Año')),
                ('cycles', models.PositiveSmallIntegerField(verbose_name='Repeticiones')),
                ('description', models.TextField(verbose_name='Descripción de la Meta')),
                ('support', models.FileField(blank=True, null=True, upload_to=metas.models.support_file, verbose_name='Soporte')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='goal_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Meta',
                'verbose_name_plural': 'Control de Metas del SPE',
                'permissions': (('review_goal', 'Revisar Meta'),),
            },
        ),
    ]