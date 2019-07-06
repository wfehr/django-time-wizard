from django.contrib.contenttypes.fields import GenericRelation
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

    @property
    def is_published(self):
        return self.time_wizard.is_published
