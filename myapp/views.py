from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from myapp.models import MyUser, PendingBeforeCourt, PendingUnderInvestigation, PBCLog
from myapp.forms import AddUserForm, EditUserForm, AddPBCForm, AddPUIForm, PBCCaseLogAddForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib import messages

class Home(TemplateView):
    template_name = 'home.html'


class UserView(ListView):
    queryset = MyUser.objects.order_by("first_name")
    template_name = 'users.html'
    context_object_name = 'users'


class AddUserView(SuccessMessageMixin, CreateView):
    model = MyUser
    form_class = AddUserForm
    template_name = 'adduser.html'
    success_url = reverse_lazy('adduser')
    success_message = 'User has been created successfully'


class EditUserView(SuccessMessageMixin, UpdateView):
    model = MyUser
    form_class = EditUserForm
    template_name = 'edituser.html'
    success_url = reverse_lazy('users')
    success_message = 'User has been updated successfully'


class DeleteUserView(SuccessMessageMixin, DeleteView):
    model = MyUser
    template_name = 'deleteuser.html'
    context_object_name = 'usr'
    success_url = reverse_lazy('users')
    success_message = 'User has been deleted successfully'


class PBCView(ListView):
    queryset = PendingBeforeCourt.objects.order_by("-created_at")
    template_name = 'pbc.html'
    context_object_name = 'pbcs'


class AddPBCView(SuccessMessageMixin, CreateView):
    model = PendingBeforeCourt
    form_class = AddPBCForm
    template_name = 'addpbc.html'
    success_url = reverse_lazy('pbc')
    success_message = 'Case has been added successfully'


class DetailPBCView(View):
    form_class = PBCCaseLogAddForm
    initial = {"key": "value"}
    template_name = 'pbcdetails.html'

    def get(self, request, pk, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        cassee = PendingBeforeCourt.objects.get(id = pk)
        logs = PBCLog.objects.filter(kase=pk).order_by('-created_at')
        return render(request, self.template_name, {"form": form, "cassee":cassee, "logs":logs})
    
    def post(self, request, *args, **kwargs):
        caseID = request.POST.get('caseId')
        cs = PendingBeforeCourt.objects.get(id = caseID)
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            comment = form.cleaned_data.get('comment')
            hearing = form.cleaned_data.get('hearing')
            mention = form.cleaned_data.get('mention')
            hearing_mention_date = form.cleaned_data.get('hearing_mention_date')
            file_upload = request.FILES['file_upload']

            pbcLog = PBCLog.objects.create(kase=cs, title=title, comment=comment, hearing=hearing, mention=mention, hearing_mention_date=hearing_mention_date, file_upload=file_upload)
            pbcLog.save()
            messages.success(request, 'Case details have been added successfully')
            return redirect(to=f'/details-pbc/{caseID}')

class EditPBCView(SuccessMessageMixin, UpdateView):
    model = PendingBeforeCourt
    form_class = AddPBCForm
    template_name = 'editpbc.html'
    success_url = reverse_lazy('pbc')
    success_message = 'Case has been updated successfully'


class DeletePBCView(SuccessMessageMixin, DeleteView):
    model = PendingBeforeCourt
    template_name = 'deletepbc.html'
    context_object_name = 'cs'
    success_url = reverse_lazy('pbc')
    success_message = 'Case has been deleted successfully'


class PUIView(ListView):
    queryset = PendingUnderInvestigation.objects.order_by("-created_at")
    template_name = 'pui.html'
    context_object_name = 'puis'


class AddPUIView(SuccessMessageMixin, CreateView):
    model = PendingUnderInvestigation
    form_class = AddPUIForm
    template_name = 'addpui.html'
    success_url = reverse_lazy('pui')
    success_message = 'Case has been added successfully'


class EditPUIView(SuccessMessageMixin, UpdateView):
    model = PendingUnderInvestigation
    form_class = AddPUIForm
    template_name = 'editpui.html'
    success_url = reverse_lazy('pui')
    success_message = 'Case has been updated successfully'


class DeletePUIView(SuccessMessageMixin, DeleteView):
    model = PendingUnderInvestigation
    template_name = 'deletepui.html'
    context_object_name = 'csui'
    success_url = reverse_lazy('pui')
    success_message = 'Case has been deleted successfully'

