from django.db import models

from cpf_field.models import CPFField

import uuid


class Cause_Options(models.TextChoices):
    EXCESSIVE_RAIN = "Chuva excessiva"
    FROST = "Geada"
    HAIL = "Granizo"
    DRY = "Seca"
    WINDLE = "Vendaval"
    LIGHTNING = "Raio"


class Registration(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    farmer_name = models.CharField(max_length=128)
    farmer_email = models.EmailField(unique=False)
    farmer_cpf = CPFField("cpf")
    location = ""
    tillage_type = models.CharField(max_length=50)
    harvest_date = models.DateField()
    cause = models.CharField(max_length=15, choices=Cause_Options.choices)
    last_modified = models.DateField(auto_now=True)

    analyst = models.ForeignKey(
        "analysts.Analyst", on_delete=models.CASCADE, related_name="registrations"
    )

