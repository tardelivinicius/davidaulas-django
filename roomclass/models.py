from django.db import models
from student.models import Student
from courses.models import Course
from django.utils.translation import ugettext_lazy as _


DEFAULT_STATUS = (
    (1, _('Ativo')),
    (2, _('Inativo')),
    (3, _('Deletado')),
)


class RoomClass(models.Model):
    student = models.ForeignKey(Student, related_name="class_student", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name="class_course", on_delete=models.CASCADE)
    date_joined = models.DateTimeField(_('Data de criação'), auto_now_add=True)
    status = models.IntegerField(_('Status'), choices=DEFAULT_STATUS, default=1)

    class Meta:
        verbose_name = _('roomclass')
        verbose_name_plural = _('roomclass')
        db_table = 'classes'


class Observation(models.Model):
    classroom = models.ForeignKey(RoomClass, related_name="observation_class", on_delete=models.CASCADE)
    observation = models.TextField(max_length=3000, blank=True)

    class Meta:
        verbose_name = _('observation')
        verbose_name_plural = _('observations')
        db_table = 'observation_classes'


