from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = Account
        fields = ['id','first_name', 'last_name', 'phone_number', 'email', 'password']

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Password does not match!")
        
        input_first_name = cleaned_data['first_name']
        if len(input_first_name)<3:
            raise forms.ValidationError("First name should be > 3 character")
        
        input_last_name = cleaned_data['last_name']
        if len(input_last_name)<3:
            raise forms.ValidationError("Last name should be > 3 character")
        
        input_phone_number = cleaned_data['phone_number']
        if len(input_phone_number)==10:
            for i in range(len(input_phone_number)):
                if ord(str(i))>=48 and ord(str(i))<=57:
                    continue
                else:
                    raise forms.ValidationError("Phone number should be Numbers") 
        else:
            raise forms.ValidationError("Phone number should be 10 Numbers")
                    
        # input_first_name = cleaned_data['first_name']
        

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter last Name'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    