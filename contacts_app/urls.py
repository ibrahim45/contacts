from django.conf.urls import patterns, url

from contacts_app import views

urlpatterns = patterns('',
    url(r'^view_all$',views.view_all),            
    url(r'^create_contact$', views.create_contact, name='create_contact'),
    url(r'^index$',views.index),
    url(r'^update/(?P<Contact_id>\d+)/$',views.update),
    url(r'^delete/(?P<Contact_id>\d+)$',views.delete),
    url(r'^all_c$',views.all_c),            
    url(r'^all_u$',views.all_u),            
    url(r'^del_all$',views.delete_all),            
    
  
    )
   


