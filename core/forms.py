from django import forms

from core import models

from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm



class UserForm(forms.ModelForm):

    class Meta:
        model = models.User
        fields = '__all__'

# ************************************************************************

class BranchForm(forms.ModelForm):

    class Meta:
        model = models.Branch
        fields = '__all__'

# ************************************************************************

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = models.Employee
        fields = '__all__'

# ************************************************************************

class EmployeeEducationForm(forms.ModelForm):

    class Meta:
        model = models.EmployeeEducation
        fields = '__all__'

# ************************************************************************

class EmployeeLanguageForm(forms.ModelForm):

    class Meta:
        model = models.EmployeeLanguage
        fields = '__all__'

# ************************************************************************

class EmployeeExperienceForm(forms.ModelForm):

    class Meta:
        model = models.EmployeeExperience
        fields = '__all__'

# ************************************************************************

class MessageForm(forms.ModelForm):

    class Meta:
        model = models.Message
        fields = '__all__'

# ************************************************************************

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    # email = models.Employee.objects.values('email')

    class Meta:
        model = models.User
        fields = ('username', 'email', 'password1', 'password2', )

# ************************************************************************

class PasswordForm(PasswordChangeForm):

    class Meta:
        model = models.User
        fields = '__all__'

# ************************************************************************