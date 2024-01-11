from django import forms
#from django.contrib.auth.models import User
from . import models

class AdminSignupForm(forms.Form):
    first_name= forms.CharField(label='First Name', max_length=50, required=True,widget=forms.TextInput(attrs={'placeholder':'Enter Your First Name','class':'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Your Last Name'}))
    username = forms.CharField(label='Username', max_length=20, required=True,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Username'}))
    password = forms.CharField(label='Password', max_length=30, required=True,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Your Password'}))
    
    class Meta:
        model = models.CustomUser
        fields = ['__all__']
    
        
        
class TeachersignupForm(forms.Form):
    first_name= forms.CharField(label='First Name', max_length=50, required=True,widget=forms.TextInput(attrs={'placeholder':'Enter Your First Name','class':'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Your Last Name'}))
    username = forms.CharField(label='Username', max_length=20, required=True,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Username'}))
    password = forms.CharField(label='Password', max_length=30, required=True,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Your Password'}))
    mobile = forms.CharField(label='Phone No', max_length=12, required=True,widget=forms.NumberInput(attrs={'placeholder':'Enter Contact No','class':'form-control'}))
    salary = forms.CharField(label='Salary', max_length=20, required=True,widget=forms.NumberInput(attrs={'class':'form-control','placeholder' :'Enter Your Salary'}))
    
    class Meta:
        model = models.CustomUser
        fields = ['__all__']

class edit_TeacherForm(forms.Form):
    first_name= forms.CharField(label='First Name', max_length=50, required=True,widget=forms.TextInput(attrs={'placeholder':'Enter Your First Name','class':'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Your Last Name'}))
    mobile = forms.CharField(label='Phone No', max_length=12, required=True,widget=forms.NumberInput(attrs={'placeholder':'Enter Contact No','class':'form-control'}))
    salary = forms.CharField(label='Salary', max_length=20, required=True,widget=forms.NumberInput(attrs={'class':'form-control','placeholder' :'Enter Your Salary'}))
    
    class Meta:
        model = models.CustomUser
        fields = ['__all__']

class StudentSignupForm(forms.Form):
    classes=[('one','one'),('two','two'),('three','three'),
    ('four','four'),('five','five'),('six','six'),('seven','seven'),('eight','eight'),('nine','nine'),('ten','ten')]
    
    first_name= forms.CharField(label='First Name', max_length=50, required=True,widget=forms.TextInput(attrs={'placeholder':'Enter Your First Name','class':'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Your Last Name'}))
    username = forms.CharField(label='Username', max_length=20, required=True,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Username'}))
    password = forms.CharField(label='Password', max_length=30, required=True,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Your Password'}))
    mobile = forms.CharField(label='Mobile', max_length=12, required=True,widget=forms.TextInput(attrs={'placeholder':'Enter Contact No','class':'form-control'}))
    class1 =  forms.ChoiceField(label='Class1', choices=classes, required=True,widget=forms.Select(attrs={'class':'form-control'}))
    roll = forms.CharField(label='Roll', max_length=12, required=True, widget=forms.TextInput(attrs={'placeholder':'Enter Your Roll No','class':'form-control'}))
    fee = forms.CharField(label='Fee', max_length=7, required=True, widget=forms.TextInput(attrs={'placeholder':'Enter your Fees','class':'form-control'}))
                       
    class Meta:
        model = models.CustomUser
        fields=['__all__']

class edit_StudentForm(forms.Form):
    classes=[('one','one'),('two','two'),('three','three'),
    ('four','four'),('five','five'),('six','six'),('seven','seven'),('eight','eight'),('nine','nine'),('ten','ten')]
    
    first_name= forms.CharField(label='First Name', max_length=50, required=True,widget=forms.TextInput(attrs={'placeholder':'Enter Your First Name','class':'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Your Last Name'}))
    mobile = forms.CharField(label='Mobile', max_length=12, required=True,widget=forms.TextInput(attrs={'placeholder':'Enter Contact No','class':'form-control'}))
    class1 =  forms.ChoiceField(label='Class1', choices=classes, required=True,widget=forms.Select(attrs={'class':'form-control'}))
    roll = forms.CharField(label='Roll', max_length=12, required=True, widget=forms.TextInput(attrs={'placeholder':'Enter Your Roll No','class':'form-control'}))
    fee = forms.CharField(label='Fee', max_length=7, required=True, widget=forms.TextInput(attrs={'placeholder':'Enter your Fees','class':'form-control'}))
                       
    class Meta:
        model = models.CustomUser
        fields=['__all__']
    
class NoticeForm(forms.ModelForm):
    class Meta:
        model=models.Notice
        fields='__all__'
        widgets = {
            'by': forms.HiddenInput(),
        }

class DateInput(forms.DateInput):
    input_type = 'date'

class AttendenceForm(forms.Form):
    presence_choices=(('Present','Present'),('Absent','Absent'))
    present_status = forms.ChoiceField(choices=presence_choices, widget=forms.Select(attrs={'class':'form-control'}))
    date = forms.DateField(widget=DateInput)


class AskDateForm(forms.Form):
    date=forms.DateField(widget=DateInput)

class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))