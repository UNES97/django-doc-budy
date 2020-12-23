from django.shortcuts import render , redirect , get_object_or_404
from django.views.generic import TemplateView , ListView , DetailView , CreateView , UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from doc_budy.models import Patient , Consulation , Ordonance , Certificat , Rv
from doc_budy.forms import PatientForm , ConsulationForm , OrdonanceForm , CertificatForm , RvForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime , timedelta
from dal import autocomplete


# Create your views here.

class PatientAutocomp(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Patient.objects.none()
        qs = Patient.objects.all()
        if self.q:
            qs = qs.filter(nom_complet__istartswith=self.q)
        return qs

class dashboard(LoginRequiredMixin,TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self,*args,**kwargs):
        context = super(dashboard,self).get_context_data(*args,**kwargs)
        patients = Patient.objects.count()
        ordonances = Ordonance.objects.count()
        consultation = Consulation.objects.count()
        certificats = Certificat.objects.count()  
        rvs = Rv.objects.filter(dte_rv=datetime.now())
        rvs_tomo = Rv.objects.filter(dte_rv=datetime.now()+timedelta(days=1))      
        context.update({
            'patients':patients,
            'ordonances' : ordonances,
            'consultation':consultation,
            'certificats':certificats,
            'rvs':rvs,
            'rvs_tomo':rvs_tomo,
        })
        return context
        


class indexview(TemplateView):
    template_name = 'index.html'

########################################################################### Patients

class patientlist(LoginRequiredMixin,ListView):
    paginate_by = 6
    model = Patient

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(nom_complet__icontains=query)
        else:
            return Patient.objects.filter()
        return object_list



class pateintdetail(LoginRequiredMixin,DetailView):
    model = Patient

class create_patient(LoginRequiredMixin,CreateView):
    model = Patient
    form_class = PatientForm

class update_patient(LoginRequiredMixin,UpdateView):
    model = Patient
    form_class = PatientForm
    
@login_required
def patient_remove(request,pk):
    patient = get_object_or_404(Patient,pk=pk)
    patient.delete()
    return redirect('patient')

################################################################################# Consultaions

class consultationlist(LoginRequiredMixin,ListView):
    paginate_by = 6
    model = Consulation

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(patient__nom_complet__icontains=query)
        else:
            return Consulation.objects.filter()
        return object_list
    
class consultationdetail(LoginRequiredMixin,DetailView):
    model = Consulation
    
class create_consultation(LoginRequiredMixin,CreateView):
    model = Consulation
    form_class = ConsulationForm

class update_consultation(LoginRequiredMixin,UpdateView):
    model = Consulation
    form_class = ConsulationForm

@login_required
def consultation_remove(request,pk):
    consultation = get_object_or_404(Consulation,pk=pk)
    consultation.delete()
    return redirect('consultation')

############################################################################## Ordonance

class ordonancelist(LoginRequiredMixin,ListView):
    paginate_by = 6
    model = Ordonance

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(patient__nom_complet__icontains=query)
        else:
            return Ordonance.objects.filter()
        return object_list
    
class ordonancedetail(LoginRequiredMixin,DetailView):
    model = Ordonance
    
class create_ordonance(LoginRequiredMixin,CreateView):
    model = Ordonance
    form_class = OrdonanceForm

class update_ordonance(LoginRequiredMixin,UpdateView):
    model = Ordonance
    form_class = OrdonanceForm

@login_required
def ordonance_remove(request,pk):
    ordonance = get_object_or_404(Ordonance,pk=pk)
    ordonance.delete()
    return redirect('ordonance')

################################################################ Certificat

class certificatlist(LoginRequiredMixin,ListView):
    paginate_by = 6
    model = Certificat

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(patient__nom_complet__icontains=query)
        else:
            return Certificat.objects.filter()
        return object_list
    
class certificatdetail(LoginRequiredMixin,DetailView):
    model = Certificat
    
class create_certificat(LoginRequiredMixin,CreateView):
    model = Certificat
    form_class = CertificatForm

class update_certificat(LoginRequiredMixin,UpdateView):
    model = Certificat
    form_class = CertificatForm

@login_required
def certificat_remove(request,pk):
    certificat = get_object_or_404(Certificat,pk=pk)
    certificat.delete()
    return redirect('certificat')


################################################################ Rv

class rvlist(LoginRequiredMixin,ListView):
    paginate_by = 6
    model = Rv

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(patient__nom_complet__icontains=query)
        else:
            return Rv.objects.filter()
        return object_list
    
class rvdetail(LoginRequiredMixin,DetailView):
    model = Rv
    
class create_rv(LoginRequiredMixin,CreateView):
    model = Rv
    form_class = RvForm

class update_rv(LoginRequiredMixin,UpdateView):
    model = Rv
    form_class = RvForm

@login_required
def rv_remove(request,pk):
    rv = get_object_or_404(Rv,pk=pk)
    rv.delete()
    return redirect('rv')
