from django import forms
#from django.contrib.auth.models import User
from . import models
from django.core.validators import RegexValidator
import re
from django.core.exceptions import ValidationError

Character_validator = RegexValidator(r'^[a-zA-Z]+$')
number_validator = RegexValidator(r'^\+?1?\d{9,13}$')
alphanumeric_validator = RegexValidator(r'^[a-zA-Z0-9]+$')
alphanumeric_wildcharacter_validators = RegexValidator(r'^(?!\d+$)\w+\S+')
email_validator = RegexValidator(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')


class AdminSignupForm(forms.Form):
    first_name= forms.CharField(label='First Name', max_length=50, required=True,validators=[Character_validator],widget=forms.TextInput(attrs={'placeholder':'Enter Your First Name','class':'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=50, required=True, validators=[Character_validator],widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Your Last Name'}))
    username = forms.CharField(label='Username', max_length=20, required=True,validators=[alphanumeric_validator],widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Username'}))
    password = forms.CharField(label='Password', max_length=30, required=True,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Your Password'}))
    
    class Meta:
        model = models.CustomUser
        fields = ['__all__']
    
    def clean_first_name(self):
        f_name = self.cleaned_data.get('first_name')
        if not re.match('^[a-zA-Z]+$',f_name):
            raise forms.ValidationError('Character Field Only!')
        if (f_name)<3:
            raise forms.ValidationError('Enter value must contain more then Three characters')
    
    def clean_last_name(self):
        l_name = self.cleaned_data.get('last_name')
        if not re.match('^[a-zA-Z0-9]+$', l_name):
            raise forms.ValidationError('Character Field Only!')
        if (l_name)<3:
            raise forms.ValidationError('Enter value must contain more then Three Character')
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not re.match('^[a-zA-Z0-9]+$', username):
            raise forms.ValidationError('Character must be Alphanumeric')
        if (username)<3:
            raise forms.ValidationError('Enter value must be more then Three Character')

class TeachersignupForm(forms.Form):
    first_name= forms.CharField(label='First Name', max_length=50, required=True,validators=[Character_validator],widget=forms.TextInput(attrs={'placeholder':'Enter Your First Name','class':'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=50, required=True, validators=[Character_validator],widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Your Last Name'}))
    username = forms.CharField(label='Username', max_length=20, required=True,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Username'}))
    password = forms.CharField(label='Password', max_length=30, required=True,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Your Password'}))
    email = forms.CharField(label='Email', max_length=50, required=True,validators=[email_validator],widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Email'}))
    mobile = forms.CharField(label='Phone No', max_length=12, required=True,validators=[number_validator],widget=forms.NumberInput(attrs={'placeholder':'Enter Contact No','class':'form-control'}))
    salary = forms.CharField(label='Salary', max_length=20, required=True,widget=forms.NumberInput(attrs={'class':'form-control','placeholder' :'Enter Your Salary'}))
    
    class Meta:
        model = models.CustomUser
        fields = ['__all__']

    def clean_first_name(self):
        f_name = self.cleaned_data.get('first_name')
        if not re.match('^[a-zA-Z]+$',f_name):
            raise forms.ValidationError('Character Field Only!')
        if len(f_name) <3:
            raise forms.ValidationError('Enter value must contain more then Three characters')
        return f_name
    
    def clean_last_name(self):
        l_name = self.cleaned_data.get('last_name')
        if not re.match('^[a-zA-Z0-9]+$', l_name):
            raise forms.ValidationError('Character Field Only!')
        if len(l_name)<3:
            raise forms.ValidationError('Enter value must contain more then Three Character')
        return l_name
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        # if not re.match('^[a-zA-Z0-9]+$', username):
        #     raise forms.ValidationError('Character must be Alphanumeric')
        if len(username)<3:
            raise forms.ValidationError('Enter value must be more then Three Character')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # if not re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',email):
        #     raise forms.ValidationError('Alphanumeric Field Only!')
        if len(email)<3:
            raise forms.ValidationError('Enter value must contain more then Three characters')
        return email
    
    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not re.match('^\+?1?\d{9,13}$',mobile):
            raise forms.ValidationError('Charater must be Numeric')
        if len(mobile)<10:
            raise forms.ValidationError('Enter value must be more then Three Character')
        return mobile 
        


class edit_TeacherForm(forms.Form):
    first_name= forms.CharField(label='First Name', max_length=50, required=True,widget=forms.TextInput(attrs={'placeholder':'Enter Your First Name','class':'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Your Last Name'}))
    mobile = forms.CharField(label='Phone No', max_length=12, required=True,widget=forms.NumberInput(attrs={'placeholder':'Enter Contact No','class':'form-control'}))
    salary = forms.CharField(label='Salary', max_length=20, required=True,widget=forms.NumberInput(attrs={'class':'form-control','placeholder' :'Enter Your Salary'}))
    
    class Meta:
        model = models.CustomUser
        fields = ['__all__']

    
    def clean_first_name(self):
        f_name = self.cleaned_data.get('first_name')
        if not re.match('^[a-zA-Z]+$',f_name):
            raise forms.ValidationError('Character Field Only!')
        if len(f_name) <3:
            raise forms.ValidationError('Enter value must contain more then Three characters')
    
    def clean_last_name(self):
        l_name = self.cleaned_data.get('last_name')
        if not re.match('^[a-zA-Z0-9]+$', l_name):
            raise forms.ValidationError('Character Field Only!')
        if len(l_name)<3:
            raise forms.ValidationError('Enter value must contain more then Three Character')
    
    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not re.match('^\+?1?\d{9,13}$',mobile):
            raise forms.ValidationError('Charater must be Numeric')
        if len(mobile)<10:
            raise forms.ValidationError('Enter value must be more then Three Character')

class StudentSignupForm(forms.Form):
    classes=[('one','one'),('two','two'),('three','three'),
    ('four','four'),('five','five'),('six','six'),('seven','seven'),('eight','eight'),('nine','nine'),('ten','ten')]
    
    first_name= forms.CharField(label='First Name', max_length=50, required=True,validators=[Character_validator],widget=forms.TextInput(attrs={'placeholder':'Enter Your First Name','class':'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=50, required=True, validators=[Character_validator],widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Your Last Name'}))
    username = forms.CharField(label='Username', max_length=20, required=True,validators=[alphanumeric_validator],widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Username'}))
    password = forms.CharField(label='Password', max_length=30, required=True,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Your Password'}))
    email = forms.CharField(label='Email', max_length=50, required=True,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Email'}))
    mobile = forms.CharField(label='Mobile', max_length=12, required=True,validators=[number_validator],widget=forms.TextInput(attrs={'placeholder':'Enter Contact No','class':'form-control'}))
    class1 =  forms.ChoiceField(label='Class', choices=classes, required=True,widget=forms.Select(attrs={'class':'form-control'}))
    roll = forms.CharField(label='Roll', max_length=12, required=True, widget=forms.TextInput(attrs={'placeholder':'Enter Your Roll No','class':'form-control'}))
    fee = forms.CharField(label='Fee', max_length=7, required=True, widget=forms.TextInput(attrs={'placeholder':'Enter your Fees','class':'form-control'}))
                       
    class Meta:
        model = models.CustomUser
        fields=['__all__']
    
    def clean_first_name(self):
        f_name = self.cleaned_data.get('first_name')
        if not re.match('^[a-zA-Z]+$',f_name):
            raise forms.ValidationError('Character Field Only!')
        if len(f_name) <3:
            raise forms.ValidationError('Enter value must contain more then Three characters')
        return f_name
    
    def clean_last_name(self):
        l_name = self.cleaned_data.get('last_name')
        if not re.match('^[a-zA-Z0-9]+$', l_name):
            raise forms.ValidationError('Character Field Only!')
        if len(l_name)<3:
            raise forms.ValidationError('Enter value must contain more then Three Character')
        return l_name
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not re.match('^[a-zA-Z0-9]+$', username):
            raise forms.ValidationError('Character must be Alphanumeric')
        if len(username)<3:
            raise forms.ValidationError('Enter value must be more then Three Character')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',email):
            raise forms.ValidationError('Alphanumeric Field Only!')
        if len(email)<3:
            raise forms.ValidationError('Enter value must contain more then Three characters')
        return email
    
    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not re.match('^\+?1?\d{9,13}$',mobile):
            raise forms.ValidationError('Charater must be Numeric')
        if len(mobile)<10:
            raise forms.ValidationError('Enter value must be Ten Digits')
        return mobile
    
    def clean_roll(self):
        roll = self.cleaned_data.get('roll')
        if not re.match('^[\d]+$',roll):
            raise forms.ValidationError('Only Numeric Value')
        return roll

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

    def clean_first_name(self):
        f_name = self.cleaned_data.get('first_name')
        if not re.match('^[a-zA-Z]+$',f_name):
            raise forms.ValidationError('Character Field Only!')
        if len(f_name) <3:
            raise forms.ValidationError('Enter value must contain more then Three characters')
        return f_name
    
    def clean_last_name(self):
        l_name = self.cleaned_data.get('last_name')
        if not re.match('^[a-zA-Z0-9]+$', l_name):
            raise forms.ValidationError('Character Field Only!')
        if len(l_name)<3:
            raise forms.ValidationError('Enter value must contain more then Three Character')
        return l_name
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not re.match('^[a-zA-Z0-9]+$', username):
            raise forms.ValidationError('Character must be Alphanumeric')
        if len(username)<3:
            raise forms.ValidationError('Enter value must be more then Three Character')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',email):
            raise forms.ValidationError('Alphanumeric Field Only!')
        if len(email)<3:
            raise forms.ValidationError('Enter value must contain more then Three characters')
        return email
    
    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not re.match('^\+?1?\d{9,13}$',mobile):
            raise forms.ValidationError('Charater must be Numeric')
        if len(mobile)<10:
            raise forms.ValidationError('Enter value must be more then Three Character')
        return mobile
    
    def clean_roll(self):
        roll = self.cleaned_data.get('roll')
        if not re.match('^\d+$'):
            raise forms.ValidationError('Only Numeric Value')
        return roll
    
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


class ForgotPassForm(forms.Form):
    #email = forms.CharField(max_length=30,required=True,widget=forms.TextInput(attrs={'placeholder': 'Enter your Email', 'class':'form-control'}))
    email = forms.EmailField(max_length=30,required=True,widget=forms.TextInput(attrs={'placeholder': 'Enter your Email', 'class':'form-control'}))
class ChangePassForm(forms.Form):
    username = forms.CharField(max_length=30,required=True,widget=forms.TextInput(attrs={'placeholder': 'Username', 'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Password'}))
    repassword = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re-enter Password'}))

    def clean(self):
        cleaned_data= super().clean()
        password=self.cleaned_data['password']
        repassword = self.cleaned_data['repassword']
        if password != repassword:
            raise forms.forms.ValidationError('password does not match')