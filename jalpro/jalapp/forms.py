from django import forms
from multiselectfield import MultiSelectFormField

class FeedbackForm(forms.Form):
    name=forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder':'Enter Your Name'
            }
        )
    )
    rating=forms.IntegerField(
        label="Enter Your Rating",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder':'Enter Your Rating'
            }
        )
    )
    feedback=forms.CharField(
        label="Enter Your Feedback",
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder':'Enter Your Feedback'
            }

        )
    )

class EnquiryForm(forms.Form):
    name=forms.CharField(
        label='Enter Your Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    mobile=forms.IntegerField(
        label="Enter Your Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Mobile Number'
            }
        )
    )
    email=forms.EmailField(
        label="Enter Your Email ID",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Email ID'
            }
        )
    )
    Gender_Choices=(
        ('F','Female'),
        ('M','Male')
    )
    gender=forms.ChoiceField(
        widget=forms.RadioSelect(),choices=Gender_Choices
    )
    COURSE_CHOICES=(
        ('py','Python'),
        ('dj','Django'),
        ('st','Software Testing'),
        ('sql','SQL'),
        ('ui','UI')
    )
    course=MultiSelectFormField(choices=COURSE_CHOICES)
    SHIFTE_CHOICES=(
        ('Morning','Morning Shift'),
        ('Ahternoon','Afternoon Shift'),
        ('Evening','Evening Shift'),
        ('Night','Night Shift')
    )
    shifts=MultiSelectFormField(choices=SHIFTE_CHOICES)
    start_date=forms.DateTimeField(
        widget=forms.SelectDateWidget(

        )
    )