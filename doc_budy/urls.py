from doc_budy import views
from django.conf.urls import url 


urlpatterns = [
    url(r'^$',views.indexview.as_view(),name='index'),
    
    url(r'^dashboard/$',views.dashboard.as_view(),name='tableau du bord'),
    url(r'^patient-autocomp/$', views.PatientAutocomp.as_view(), name='patient-autocomp'),
    url(r'^patient/$',views.patientlist.as_view(),name='patient'),
    url(r'^pateint_detail/(?P<pk>\d+)/$',views.pateintdetail.as_view(),name='patient detail'),
    url(r'^patient/new/$',views.create_patient.as_view(),name='new patient'),
    url(r'^patient/(?P<pk>\d+)/edit/$',views.update_patient.as_view(),name='edit patient'),
    url(r'^patient/(?P<pk>\d+)/remove/$',views.patient_remove,name='remove_patient'),
    ##########################################################################################
    url(r'^consultation/$',views.consultationlist.as_view(),name='consultation'),
    url(r'^consultation_detail/(?P<pk>\d+)/$',views.consultationdetail.as_view(),name='consultation detail'),
    url(r'^consultation/new/$',views.create_consultation.as_view(),name='new consultation'),
    url(r'^consultation/(?P<pk>\d+)/edit/$',views.update_consultation.as_view(),name='edit consultation'),
    url(r'^consultation/(?P<pk>\d+)/remove/$',views.consultation_remove,name='remove_consultation'),
    ##########################################################################################
    url(r'^ordonance/$',views.ordonancelist.as_view(),name='ordonance'),
    url(r'^ordonance_detail/(?P<pk>\d+)/$',views.ordonancedetail.as_view(),name='ordonance detail'),
    url(r'^ordonance/new/$',views.create_ordonance.as_view(),name='new ordonance'),
    url(r'^ordonance/(?P<pk>\d+)/edit/$',views.update_ordonance.as_view(),name='edit ordonance'),
    url(r'^ordonance/(?P<pk>\d+)/remove/$',views.ordonance_remove,name='remove_ordonance'),
    ############################################################################################
    url(r'^certificat/$',views.certificatlist.as_view(),name='certificat'),
    url(r'^certificat_detail/(?P<pk>\d+)/$',views.certificatdetail.as_view(),name='certificat detail'),
    url(r'^certificat/new/$',views.create_certificat.as_view(),name='new certificat'),
    url(r'^certificat/(?P<pk>\d+)/edit/$',views.update_certificat.as_view(),name='edit certificat'),
    url(r'^certificat/(?P<pk>\d+)/remove/$',views.certificat_remove,name='remove_certificat'),
    ############################################################################################
    url(r'^rv/$',views.rvlist.as_view(),name='rv'),
    url(r'^rv_detail/(?P<pk>\d+)/$',views.rvdetail.as_view(),name='rv detail'),
    url(r'^rv/new/$',views.create_rv.as_view(),name='new rv'),
    url(r'^rv/(?P<pk>\d+)/edit/$',views.update_rv.as_view(),name='edit rv'),
    url(r'^rv/(?P<pk>\d+)/remove/$',views.rv_remove,name='remove_rv'),




]