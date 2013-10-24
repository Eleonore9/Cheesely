from django.db import models
from django.utils.translation import ugettext_lazy as _

class Cheese(models.Model):

    FIRMNESS_UNSPECIFIED = 1
    FIRMNESS_SOFT = 2
    FIRMNESS_SEMISOFT = 3
    FIRMNESS_SEMIHARD = 4
    FIRMNESS_HARD = 5
    FIRMNESS_CHOICES = (
        (FIRMNESS_UNSPECIFIED, _("unspecified")),
	(FIRMNESS_SOFT, _("soft")),
	(FIRMNESS_SEMISOFT, _("semi-soft")),
	(FIRMNESS_SEMIHARD, _("semi-hard")),
	(FIRMNESS_HARD, _("hard")),
	)
    name = models.CharField(_("Name of Cheese", max_length=255))
    description = models.TextField(_("Description", blank=True))
    firmness = models.IntegerField(_("Firmness", max_length=20,
		choices=FIRMNESS_CHOICES, null=True, blank=True))
    country_of_origin = models.CharField(_("Country of Origin",
                            max_length=255, blank=True, null=True))
    region_of_origin = models.CharField(_("Region of Origin",
                            max_length=255, blank=True, null=True))
    photo = models.ImageField(_("Photo", upload_to="cheeses",
                                        blank=True, null=True, default="")) 
    photo_attribution = models.URLField(_("Photo Attribution",
		    max_length=255, blank=True, null=True, default=""))

    def __unicode__(self): 
        # To display the actual name 
        # and not "Cheese object"
        return self.name
