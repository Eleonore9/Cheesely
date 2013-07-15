from django.db import models

# Create your models here.

class Cheese(models.Model):
    FIRMNESS_UNSPECIFIED = 1
    FIRMNESS_SOFT = 2
    FIRMNESS_HARD = 3

    FIRMNESS_CHOICES = (
        (FIRMNESS_UNSPECIFIED, 'unspecified'),
        (FIRMNESS_SOFT, 'soft'),
        (FIRMNESS_HARD, 'hard'),
    )

    name = models.CharField("Name of Cheese", max_length=255)
    description = models.TextField("Description", blank=True,
                null=True)
    firmness = models.IntegerField("Firmness", max_length=20,
                choices=FIRMNESS_CHOICES, null=True, blank=True)
    country_of_origin = models.CharField("Country of Origin",
                            max_length=255, blank=True, null=True)
    region_of_origin = models.CharField("Region of Origin",
                            max_length=255, blank=True, null=True)
    photo = models.ImageField("Photo", upload_to="cheeses",
                                        blank=True, default="")
    photo_attribution = models.URLField("Photo Attribution",
                        max_length=255, blank=True, default="")

    def __unicode__(self): 
        # To display the actual name 
        # and not "Cheese object"
        return self.name