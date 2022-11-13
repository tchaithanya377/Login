from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms

class loginform(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets ={          
                    'username': forms.TextInput(attrs={
                        'class':'form-control',  
                        'placeholder':'User Name'
                    }),
                    'password': forms.PasswordInput(attrs={
                        'class': 'form-control',  
                    }),
                
                }


class signupform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email', 'is_staff','is_active']
        widgets ={          
                    'username': forms.TextInput(attrs={
                        'class':'form-control',  
                        'placeholder':'User Name'
                    }),

                    'first_name': forms.TextInput(attrs={
                        'class':'form-control',  
                        'placeholder':'User Name'
                    }),
                    'last_name': forms.TextInput(attrs={
                        'class':'form-control',  
                        'placeholder':'User Name'
                    }),
                    'email': forms.TextInput(attrs={
                        'class':'form-control',  
                        'placeholder':'example@exapmle.com'
                    }),
                
                }