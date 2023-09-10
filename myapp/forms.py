from django import forms
from myapp.models import MyUser, PendingBeforeCourt, PendingUnderInvestigation
from phonenumber_field.formfields import PhoneNumberField
import re


class AddUserForm(forms.ModelForm):
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your username ...'}))
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your first name ...'}))
    middle_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your middle name ...'}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your last name ...'}))
    force_number = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your force number ...'}))
    phone_number = PhoneNumberField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter phone number eg +254712345678 ...'}))
    password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter your password ...'}))
    password2 = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm your password ...'}))


    class Meta:
        model = MyUser
        fields = ('username', 'first_name', 'middle_name', 'last_name', 'force_number', 'phone_number', 'password')


    def clean(self):
        super(AddUserForm, self).clean()
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        uppercase_error = re.search(r"[A-Z]", password) is None
        lowercase_error = re.search(r"[a-z]", password) is None
        if len(password) < 6:
            self._errors['password'] = self.error_class([
                'Minimum 6 characters required!'])
        elif uppercase_error or lowercase_error:
            self._errors['password'] = self.error_class([
                'Password must contain uppercase and lowercase characters!'])
        elif password != password2:
            self._errors['password'] = self.error_class([
                'The two passwords did not match!'])
        return self.cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
        

class EditUserForm(forms.ModelForm):
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your username ...'}))
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your first name ...'}))
    middle_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your middle name ...'}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your last name ...'}))
    force_number = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your force number ...'}))
    phone_number = PhoneNumberField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter phone number eg +254712345678 ...'}))
    is_admin = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input'}), required=False)

    class Meta:
        model = MyUser
        fields = ('username', 'first_name', 'middle_name', 'last_name', 'force_number', 'phone_number', 'is_admin')

class AddPBCForm(forms.ModelForm):
    sno = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter station number ...'}))
    occurence_book_no = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter occurence book number ...'}))
    police_station = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter police station ...'}))
    complainant_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter complainant name ...'}))
    offence = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter offence ...'}))
    remarks = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter remarks ...'}))
    results = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter results ...'}))
    charge_registry_no = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter charge registry number ...'}))
    court_file_number = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter court file number ...'}))
    accused_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter court accused name ...'}))
    court = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter court name ...'}))

    class Meta:
        model = PendingBeforeCourt
        # fields = ('sno', 'occurence_book_no', 'police_station', 'complainant_name', 'offence', 'remarks', 'results', 'charge_registry_no', 'court_file_number', 'accused_name', 'court', 'case_file')
        fields = '__all__'


        widgets = {
                'investigating_officer':forms.Select(attrs={'class':'form-select'}),
                'hearing_mention_date':  forms.DateTimeInput(format=('%Y-%m-%dT%H:%M'), attrs={'type': 'datetime-local', 'class': 'form-control'})
        }


class AddPUIForm(forms.ModelForm):
    sno = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter station number ...'}))
    occurence_book_no = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter occurence book number ...'}))
    police_station = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter police station ...'}))
    complainant_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter complainant name ...'}))
    offence = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter offence ...'}))
    remarks = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter remarks ...'}))
    results = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter results ...'}))
    suspect_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter suspect name ...'}))

    class Meta:
        model = PendingUnderInvestigation
        # fields = ('sno', 'occurence_book_no', 'police_station', 'complainant_name', 'offence', 'remarks', 'results', 'charge_registry_no', 'court_file_number', 'accused_name', 'court', 'case_file')
        fields = '__all__'


        widgets = {
                'investigating_officer':forms.Select(attrs={'class':'form-select'}),
                'hearing_mention_date':  forms.DateTimeInput(format=('%Y-%m-%dT%H:%M'), attrs={'type': 'datetime-local', 'class': 'form-control'}),
                'actual_date':  forms.DateTimeInput(attrs={'type': 'date', 'class': 'form-control'})
        }