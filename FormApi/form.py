from django import forms
from FormApi.models import Users , Context_for_year
from django.utils.translation import ugettext_lazy as _


class SendEmailForm(forms.Form):
    subject = forms.CharField(max_length=100,required=True)
    body =forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}),required=True)
    sorting = forms.MultipleChoiceField(
        required=True,
        choices=Context_for_year
    )
    class meta:
    	# widget = {
     #        'body': forms.Textarea(),
     #    }
 
        labels = {
        	'subject':_("Subject for mail"),
        	'body':_("Body"),
        	"sorting":_("Send_Email_To")
        }

class UsersForm(forms.ModelForm):
	class meta:
		model = Users
		fields = '__all__'
		labels = {
			'UserName':_("Name of student"),
			"Year":_("Year of study"),
			"Rollno":_("Rollno"),
			"Email":_("Email"),
			"Phone":_("Phone no")
		}


    