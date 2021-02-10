from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from profiles.models import ROLE


# upload support file, utility function
def support_file(instance, file):
    import os.path
    ext = file.split('.')[-1]
    root = 'metas'
    model = instance.model
    file = '%s_soporte.%s' % (model, ext)
    goal = "%s-%s" % (instance.role.lower(), instance.key)
    path = os.path.join(root, instance.role.lower(), goal, file)
    return path


def upload_proof(instancia, file):
    import os.path
    ext = file.split('.')[-1]
    root = 'metas'
    role = instancia.miembro.puesto.lower()
    key = "%02d" % int(instancia.meta.clave)
    site = slugify(instancia.miembro.get_sitio())
    date = instancia.fecha.strftime('%y%m%d')
    goal = "%s-%s" % (role, key)
    file = '%s_%s_%s.%s' % (goal, site, date, ext)
    path = os.path.join(root, role, goal, file)
    return path


# Metadata about goals
class Goal(models.Model):
    # Goal identification
    role = models.CharField("Cargo", max_length=6, choices=ROLE)
    key = models.CharField("Clave de la Meta", max_length=6)
    short_name = models.CharField('Identificación', max_length=50)
    year = models.PositiveIntegerField("Año")
    cycles = models.PositiveSmallIntegerField('Repeticiones')

    # Goal description
    description = models.TextField('Descripción de la Meta')
    support = models.FileField('Soporte', upload_to=support_file, blank=True, null=True)

    # Tracking & identification
    user = models.ForeignKey(User, related_name='goal_user', editable=False, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s-%s' % (self.role, self.key)

    @property
    def model(self):
        return u'%s%s' % (self.role.lower(), self.key)

    # TODO Correct UNICODE name

    # def progress(self, role):
    #     return (self.evidenciaFK_meta.filter(role=role).count() * 1. / self.cycles) * 100.

    class Meta:
        verbose_name = "Meta"
        verbose_name_plural = "Control de Metas del SPE"
        app_label = 'metas'
        permissions = (('review_goal', 'Revisar Meta'),)


class Proof(models.Model):
    # Goal metadata
    goal = models.ForeignKey(Goal,
                             related_name="proofFK_goal",
                             on_delete=models.CASCADE)
    role = models.ForeignKey(User,
                             verbose_name='Miembro del SPE',
                             related_name='proofFK_role', on_delete=models.CASCADE)
    date = models.DateField()

    # Tracking data
    user = models.ForeignKey(User,
                             related_name='proofFK_user',
                             editable=False,
                             on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s - %s - %s" % (self.goal, self.user.get_site(), self.date)

    class Meta:
        abstract = True
        verbose_name = 'Evidencia'
        verbose_name_plural = 'Evidencias'


class DEA2(Proof):
    oficio = models.FileField('Oficio de comportamiento presupuestal', upload_to=upload_proof, )
    notificacion = models.FileField('Oficio  mediante el cual se  notifican los saldos negativos',
                                    upload_to=upload_proof, )

    class Meta:
        app_label = 'metas'
