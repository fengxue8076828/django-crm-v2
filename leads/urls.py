from django.urls import path
from django.contrib.auth.views import (PasswordResetCompleteView,
                                    PasswordResetConfirmView,
                                    PasswordResetView,
                                    PasswordResetDoneView)
from .views import *

app_name='leads'
urlpatterns=[
    path('',LeadsListView.as_view(),name="list_leads"),
    path('create_lead/',LeadCreateView.as_view(),name="create_lead"),
    path('detail_lead/<int:pk>',LeadDetailView.as_view(),name="detail_lead"),
    path('update_lead/<int:pk>',LeadUpdateView.as_view(),name="update_lead"),
    path('assign_agent/<int:pk>',LeadAssignView.as_view(),name="assign_agent"),
    path('category_list/',CategoryListView.as_view(),name="category_list"),
    path('category_detail/<int:pk>',CategoryDetailView.as_view(),name="category_detail")

]