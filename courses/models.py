from django.db import models
from django.utils.translation import ugettext_lazy as _


DEFAULT_STATUS = (
    (1, _('Ativo')),
    (2, _('Inativo')),
    (3, _('Deletado')),
)

class CourseDate(models.Model):
    day = models.CharField(max_length=20, blank=False)
    hour = models.CharField(max_length=20, blank=False)

    class Meta:
        verbose_name = _('coursedate')
        verbose_name_plural = _('coursedates')
        db_table = 'CourseDates'
    
class Course(models.Model):
    name = models.CharField(max_length=250, blank=False)
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    date_course = models.ManyToManyField(CourseDate, related_name="date_course")
    status = models.IntegerField(_('Status'), choices=DEFAULT_STATUS, default=1)
    
    class Meta:
        verbose_name = _('course')
        verbose_name_plural = _('courses')
        db_table = 'Courses'