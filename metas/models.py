from django.db import models
from django.contrib.auth.models import User
from profiles.models import ROLE


# upload support file, utility function
def support_file(instance, file):
    import os.path
    ext = file.split('.')[-1]
    orig = 'metas'
    model = instance.model
    file = '%s_soporte.%s' % (model, ext)
    goal = "%s-%s" % (instance.role.lower(), instance.key)
    path = os.path.join(orig, instance.role.lower(), goal, file)
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

    # def progress(self, miembro):
    #     return (self.evidenciaFK_meta.filter(miembro=miembro).count() * 1. / self.cycles) * 100.

    class Meta:
        verbose_name = "Meta"
        verbose_name_plural = "Control de Metas del SPE"
        app_label = 'metas'
        permissions = (('review_goal', 'Revisar Meta'),)


# TODO: Create a proof model, with json field
