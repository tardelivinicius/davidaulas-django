from django.db import models
from student.models import Student
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


DEFAULT_STATUS = (
    (1, _('Ativo')),
    (2, _('Inativo')),
    (3, _('Deletado')),
)


DEFAULT_PAY_STATUS = (
    (1, _('Pago')),
    (2, _('Pendente')),
    (3, _('Cancelado')),
)


DEFAULT_RECEIPT_STATUS = (
    (1, _('Gerado')),
    (2, _('Não Gerado')),
    (3, _('Deletado')),
)


class PayMethods(models.Model):

    name = models.CharField(max_length=250, blank=False)
    status = models.IntegerField(_('Status'), choices=DEFAULT_STATUS, default=1)

    class Meta:
        verbose_name = _('PayMethod')
        verbose_name_plural = _('paymethods')
        db_table = 'finances_paymethods'

class Finance(models.Model):

    student = models.ForeignKey(Student, related_name="finance_student", on_delete=models.CASCADE)
    dtInc = models.DateTimeField(default=timezone.now)
    protocol = models.CharField(max_length=250, blank=False)
    pay_method = models.ForeignKey(PayMethods, related_name="finance_paymethods", on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    status = models.IntegerField(_('Status'), choices=DEFAULT_PAY_STATUS, default=2)

    class Meta:
        verbose_name = _('finance')
        verbose_name_plural = _('finance')
        db_table = 'finances'

class FinanceControl(models.Model):

    finance = models.ForeignKey(Finance, related_name="control_finance", on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.IntegerField(_('Status'), choices=DEFAULT_PAY_STATUS, default=2)

    class Meta:
        verbose_name = _('financecontrol')
        verbose_name_plural = _('financescontrol')
        db_table = 'finances_control'


class FinanceReceipt(models.Model):

    finance = models.ForeignKey(Finance, related_name="receipt_finance", on_delete=models.CASCADE)
    dtGenerate = models.DateTimeField()
    status = models.IntegerField(_('Status'), choices=DEFAULT_RECEIPT_STATUS, default=1)