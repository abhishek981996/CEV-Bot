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
# class UserForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(UserForm, self).__init__(*args, **kwargs)
#         self.fields['first_name'].required = True
#         self.fields['last_name'].required = True
#         self.fields['email'].required = True

#     class Meta:
#         model = User
#         exclude = ['username', 'password', 'date_joined']

class UsersForm(forms.ModelForm):
	class Meta:
		model = Users
		fields = '__all__'
		labels = {
			'UserName':_("Name of student"),
			"Year":_("Year of study"),
			"Rollno":_("Rollno"),
			"Email":_("Email"),
			"Phone":_("Phone no")
		}

class UploadFileForm(forms.Form):
    file = forms.FileField(required=True)


    