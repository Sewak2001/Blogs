from .models import blog,contactus,profile,leavecomment
from django import forms 

class blogfrom(forms.ModelForm):
    class Meta:
        model = blog
        fields = '__all__'

class contactfrom(forms.ModelForm):
    class Meta:
        model = contactus
        fields = '__all__'

class profilefrom(forms.ModelForm):
    class Meta:
        model = profile
        fields = '__all__'







