from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


DEFAULT_STATUS = (
    (1, _('Adimplente')),
    (2, _('Inadimplente')),
    (3, _('Deletado')),
)

class Student(models.Model):

    email = models.CharField(max_length=250, blank=False)
    name = models.CharField(max_length=250, blank=False)
    name_responsible = models.CharField(max_length=250, blank=True)
    dtInc = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(_('Status'), choices=DEFAULT_STATUS, default=1)

    class Meta:
        verbose_name = _('student')
        verbose_name_plural = _('students')
        db_table = 'students'

class Address(models.Model):

    address = models.CharField(max_length=250, blank=True)
    number = models.CharField(max_length=250, blank=True)
    student = models.ForeignKey(Student, related_name="address_student", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('address')
        verbose_name_plural = _('adresses')
        db_table = 'adresses'

class Phone(models.Model):

    telephone_residential = models.CharField(max_length=50, blank=True)
    telephone_mobile = models.CharField(max_length=50, blank=True)
    student = models.ForeignKey(Student, related_name="phone_student", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('phone')
        verbose_name_plural = _('phones')
        db_table = 'phones'
