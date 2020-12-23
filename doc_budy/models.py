from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Patient(models.Model):
    
    cin = models.CharField(max_length=12)
    nom_complet = models.CharField(max_length=256)
    sexe = models.CharField(max_length=1)
    adresse = models.CharField(max_length=256)
    tel = models.CharField(max_length=20)
    mail = models.EmailField(blank=True , null=True)
    dte_naissance = models.DateField()

    def __str__(self):
        return self.nom_complet

    def get_absolute_url(self):
        return reverse('patient detail',kwargs={'pk':self.pk})

class Rv(models.Model):
    patient = models.ForeignKey('Patient',related_name='rvs',on_delete=models.CASCADE)
    dte_rv = models.DateField()
    heure_rv = models.TimeField()

    def __str__(self):
        return str(self.patient)

    def get_absolute_url(self):
        return reverse('rv detail',kwargs={'pk':self.pk})

class Consulation(models.Model):
    patient = models.ForeignKey('Patient',related_name='consultations',on_delete=models.CASCADE)
    dte_consultation = models.DateField()
    heure_consultation = models.TimeField()
    type_consultation = models.CharField(max_length=50)
    prix = models.FloatField()
    symptome = models.CharField(max_length=256)
    observation = models.TextField()

    def __str__(self):
        return str(self.patient)

    def get_absolute_url(self):
        return reverse('consultation detail',kwargs={'pk':self.pk})

class Ordonance(models.Model):
    patient =  models.ForeignKey('Patient',related_name='ordonances',on_delete=models.CASCADE)
    dte_ord = models.DateField()
    heure_ord = models.TimeField()
    prescription = models.TextField()

    def __str__(self):
        return str(self.patient)

    def get_absolute_url(self):
        return reverse('ordonance detail',kwargs={'pk':self.pk})

class Certificat(models.Model):
    patient =  models.ForeignKey('Patient',related_name='certificats',on_delete=models.CASCADE)
    dte_certf = models.DateField()
    heure_certf = models.TimeField()
    observation = models.TextField()

    def __str__(self):
        return str(self.patient)

    def get_absolute_url(self):
        return reverse('certificat detail',kwargs={'pk':self.pk})






