from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.timezone import now


class TimeWizardInlineMixin(models.Model):
    """
    Mixin for the inline support of PeriodModel.
    """
    periods = GenericRelation(
        'time_wizard.PeriodModel',
    )

    class Meta:
        abstract = True

    def __str__(self):
        prefix = str(self.pk) + ' - '
        ct = ContentType.objects.get_for_model(self)
        return prefix + ' - '.join(
            [str(s) for s in self.periods.model.objects.filter(
             content_type=ct, object_id=self.id)])

    @property
    def is_published(self):
        dt = now()
        for p in self.periods.all():
            if p.contains(dt):
                return True
        return False


class TimeWizardMixin(models.Model):
    """
    Mixin to let models have a foreign-key-relation to the TimeWizard. Property
    `is_published` is used to indicate if a TimeWizard is set wether or not
    to show the contents/children.
    """
    time_wizard = models.ForeignKey(
        'time_wizard.TimeWizardModel',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.time_wizard)

    @property
    def is_published(self):
        if self.time_wizard_id:
            return self.time_wizard.is_published
        else:
            return False
