from django import forms
from userauths.models import Profile

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Fale'),
    ('O', 'Other'),
)

JOB_CITY_CHOICES = (
    ('Lahore', 'Lahore'),
    ('karachi', 'karachi'),
    ('Multan', 'Multan'),
    ('Peshawar', 'Peshawar'),
    ('Queta', 'Queta'),
    ('Islamabad', 'Islamabad'),
)


class ProfileForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    job_city=forms.MultipleChoiceField(choices=JOB_CITY_CHOICES, widget=forms.CheckboxSelectMultiple,help_text='Select one or more cities where you preffered to work',label='Preffered Job Cities')
    class Meta:
        model = Profile
        fields = [
            'name', 'dob', 'gender', 'locality', 'city', 'pin',
            'state', 'mobile', 'email', 'job_city', 'profile_image',
            'my_file'
        ]

        labels={
            'name':'Full Name',
            'dob':'Date of Birth',
            'pin':'Pin Code',
            'mobile':'Mobile Number'
        }
        help_texts={
            'profile_image':'Optional: Upload a profile image',
            'my_file':'Optional: Attach any additional document (PDF, DOCX, etc.)',
        }

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your area name.'}),
            'city':forms.TextInput(attrs={'class':'form-control','placeholder':'City'}),
            'pin':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter 6-digit PIN code'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'mobile':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter 11-digit mobile number'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email Address'}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker','type':'date'})
        }