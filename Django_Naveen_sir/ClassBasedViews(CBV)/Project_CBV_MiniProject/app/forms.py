from django import forms

class Arjun(forms.Form):
    UserName=forms.CharField()
    Password=forms.CharField()

class Feedback(forms.Form):
    Name=forms.CharField()
    ContactNo=forms.IntegerField()
    EmailId=forms.CharField()
    state=forms.CharField()
    Feedback=forms.CharField()
   # Feedback=forms.TextField()


class Register(forms.Form):
    Idno=forms.IntegerField()
    Name=forms.CharField()
    Designation=forms.CharField()
    Salary=forms.IntegerField()
    ContactNo= forms.IntegerField()
    State=forms.CharField()
    Pincode=forms.IntegerField()