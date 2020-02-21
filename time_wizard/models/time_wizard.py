from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _

from time_wizard.mixins import TimeWizardInlineMixin


class TimeWizardModel(TimeWizardInlineMixin, models.Model):
    """
    Model for the TimeWizard.
    """
    name = models.CharField(
        blank=True,
        help_text=_('Optional name to identify the given TimeWizard.'),
        max_length=255,
    )

    def __str__(self):
        if self.name:
            return self.name
        else:
            ct = ContentType.objects.get_for_model(self)
            return ' - '.join(
                [str(s) for s in self.periods.model.objects.filter(
                 content_type=ct, object_id=self.id)])
