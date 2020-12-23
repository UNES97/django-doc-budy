from django import forms
from doc_budy.models import Patient , Consulation , Ordonance , Certificat , Rv
from dal import autocomplete

class PatientForm(forms.ModelForm):
    
    class Meta():
        model = Patient
        fields = ('cin','nom_complet','sexe','adresse','tel','mail','dte_naissance')
        CHOICES = [
        ('M','M'),
        ('F','F'),
        ]
        widgets = {
            'cin':forms.TextInput(attrs={'class':'form-control'}),
            'nom_complet':forms.TextInput(attrs={'class':'form-control'}),
            'sexe':forms.Select(choices=CHOICES,attrs={'class':'form-control'}),
            'adresse':forms.TextInput(attrs={'class':'form-control'}),
            'tel':forms.TextInput(attrs={'class':'form-control'}),
            'mail':forms.TextInput(attrs={'class':'form-control'}),
            'dte_naissance':forms.DateInput(attrs={'class':'form-control' , 'type':'date'}),
        }

class ConsulationForm(forms.ModelForm):
    class Meta():
        model = Consulation
        fields = ('patient','dte_consultation','heure_consultation','type_consultation','prix','symptome','observation')
        CHOICES = [
        ('Consultation','Consultation'),
        ('Controlle','Controlle'),
        ]
        widgets = {
            'patient':autocomplete.ModelSelect2(url='patient-autocomp',
            attrs={
                'class': 'form-control'
            }),
            'dte_consultation':forms.TextInput(attrs={'class':'form-control' , 'type':'date'}),
            'heure_consultation':forms.TextInput(attrs={'class':'form-control' , 'type':'time'}),
            'type_consultation':forms.Select(choices=CHOICES,attrs={'class':'form-control'}),
            'prix':forms.NumberInput(attrs={'class':'form-control'}),
            'symptome':forms.TextInput(attrs={'class':'form-control'}),
            'observation':forms.Textarea(attrs={'class':'form-control'}),
        }
    
class OrdonanceForm(forms.ModelForm):
    class Meta():
        model = Ordonance
        fields = ('patient','dte_ord','heure_ord','prescription')
        widgets = {
            'patient':autocomplete.ModelSelect2(url='patient-autocomp',
            attrs={
                'class': 'form-control'
            }),
            'dte_ord':forms.TextInput(attrs={'class':'form-control' , 'type':'date'}),
            'heure_ord':forms.TextInput(attrs={'class':'form-control' , 'type':'time'}),
            'prescription':forms.Textarea(attrs={'class':'form-control'}),
        }

class CertificatForm(forms.ModelForm):
    class Meta():
        model = Certificat
        fields = ('patient','dte_certf','heure_certf','observation')
        widgets = {
            'patient':autocomplete.ModelSelect2(url='patient-autocomp',
            attrs={
                'class': 'form-control'
            }),
            'dte_certf':forms.TextInput(attrs={'class':'form-control' , 'type':'date'}),
            'heure_certf':forms.TextInput(attrs={'class':'form-control' , 'type':'time'}),
            'observation':forms.Textarea(attrs={'class':'form-control'}),
        }

class RvForm(forms.ModelForm):
    class Meta():
        model = Rv
        fields = ('patient','dte_rv','heure_rv')
        widgets = {
            'patient':autocomplete.ModelSelect2(url='patient-autocomp',
            attrs={
                'class': 'form-control'
            }),
            'dte_rv':forms.TextInput(attrs={'class':'form-control' , 'type':'date'}),
            'heure_rv':forms.TextInput(attrs={'class':'form-control' , 'type':'time'}),
        }
