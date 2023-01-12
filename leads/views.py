from django.shortcuts import render,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DetailView,FormView
from .forms import *
from .models import *
from agents.mixins import OrganizerRequiredMixin


# Create your views here.

class SignupView(CreateView):
    template_name="registration/signup.html"
    form_class=CustomedUserCreationForm

    def get_success_url(self):
        return reverse("login")

class LeadsListView(LoginRequiredMixin,ListView):
    template_name="leads/list_leads.html"
    context_object_name="leads"

    def get_queryset(self):
        user=self.request.user      
        if user.is_organizer:
            return Lead.objects.filter(organizer=user.organizer,agent__isnull=False)
        else:
            organizer=user.agent.organizer
            queryset=Lead.objects.filter(organizer=organizer)
            return queryset.filter(agent__user=self.request.user)

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        user=self.request.user
        if user.is_organizer:
            unsigned_leads=Lead.objects.filter(organizer=user.organizer,agent__isnull=True)
            context.update({
                "unsigned_leads":unsigned_leads
            })
        return context


class LeadDetailView(DetailView):
    template_name="leads/lead_detail.html"
    context_object_name="lead"

    def get_queryset(self):
        user=self.request.user      
        if user.is_organizer:
            return Lead.objects.filter(organizer=user.organizer)
        else:
            organizer=user.agent.organizer
            queryset=Lead.objects.filter(organizer=organizer)
            return queryset.filter(agent__user=self.request.user)

class LeadCreateView(OrganizerRequiredMixin,CreateView):
    template_name="leads/lead_create.html"
    form_class=LeadForm

    def get_success_url(self):
        return reverse("leads:list_leads")
    
    def form_valid(self, form):
        lead=form.save(commit=False)
        lead.organizer=self.request.user.organizer
        new_cat=Category.objects.get(name="new")
        lead.category=new_cat
        lead.save()
        return super().form_valid(form)

class LeadUpdateView(UpdateView):
    template_name="leads/lead_update.html"
    form_class=LeadForm

    def get_success_url(self):
        print(self.request.POST)
        return reverse("leads:detail_lead",kwargs={'pk':self.get_object().id})

    def get_queryset(self):
        user=self.request.user      
        if user.is_organizer:
            return Lead.objects.filter(organizer=user.organizer)
        else:
            organizer=user.agent.organizer
            queryset=Lead.objects.filter(organizer=organizer)
            return queryset.filter(agent__user=self.request.user)

class LeadAssignView(LoginRequiredMixin,OrganizerRequiredMixin,FormView):
    template_name="leads/assign_agent.html"
    form_class=AssignAgentForm

    def get_form_kwargs(self,**kwargs):
        kwargs=super().get_form_kwargs(**kwargs)
        kwargs.update({
            "request":self.request
        })
        return kwargs

    def get_success_url(self):
        return reverse("leads:list_leads")
    
    def form_valid(self,form):
        agent=form.cleaned_data["agent"]
        lead=Lead.objects.get(id=self.kwargs["pk"])
        lead.agent=agent
        lead.save()
        return super().form_valid(form)

class CategoryListView(LoginRequiredMixin,ListView):
    template_name="leads/category_list.html"

    context_object_name="category_list"

    def get_queryset(self):
        queryset=Category.objects.all()
        return queryset

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        user=self.request.user
        if user.is_organizer:
            queryset= Lead.objects.filter(organizer=user.organizer).filter(category__isnull=True)
        else:
            queryset=Lead.objects.filter(organizer=user.agent.organizer).filter(agent__user=user).filter(category__isnull=True)

        context.update({
            "unsigned":queryset.count(),
        })

        return context

class CategoryDetailView(LoginRequiredMixin,DetailView):
    template_name="leads/category_detail.html"

    context_object_name="category"

    def get_queryset(self):
        queryset=Category.objects.all()
        return queryset

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        user=self.request.user

        category=self.get_object()
        print("**********",category)
        if user.is_organizer:
            leads=category.lead_set.filter(organizer=user.organizer)
        else:
            leads=category.lead_set.filter(agent__user=user)

        context.update({
            "leads":leads
        })

        return context


