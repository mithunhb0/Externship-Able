from django import forms
from dashboard.models import Lead, Remark

class LeadForm(forms.ModelForm):
    # STATUS_CHOICES  = (('newlead','New Lead'),('hotlead','Hot Lead'),('medlead','Med Lead'),('greylead','Grey Lead'),('success','Success'))
    
    # status          = forms.CharField(widget=forms.Select(choices=STATUS_CHOICES))
    
    class Meta:
       model = Lead
       fields = ('__all__')
   
    # def __init__(self, *args, **kwargs):
    #     super(LeadForm, self).__init__(*args, **kwargs)
    #     self.fields["status"].widget.attrs['class'] = 'dropdown-menu'
        
class RemarkForm(forms.ModelForm):

    class Meta:
       model = Remark
       fields = ('__all__')