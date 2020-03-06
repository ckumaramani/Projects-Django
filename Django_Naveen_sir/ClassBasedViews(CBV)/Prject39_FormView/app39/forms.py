from django import forms

class arjun(forms.Form):
    id=forms.IntegerField(label= "idno")
    na=forms.CharField(label= "Name")
    sal=forms.DecimalField(label= "Salary")
    un=forms.CharField(label= "UserName")
    pas=forms.CharField(label= "Password", widget=forms.PasswordInput)