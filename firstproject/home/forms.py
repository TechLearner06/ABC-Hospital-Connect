from django import forms

from .models import Booking

from .models import Contactus


class DateInput(forms.DateInput):
    input_type='date'

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'

        widgets = {
            'booking_date':DateInput()
        }

        labels={

            'p_name':'Patient Name',
            'p_phone':'Patient Phone',
            'p_email':'patient E-Mail',
            'doc_name':'Doctor Name',
            'booking_date':'Booking Date'
        }


class ContactusForm(forms.ModelForm):
    class Meta:
        model=Contactus
        fields='__all__'
    
        labels={

            'name':'Name',
            'email':'E-Mail',
            'message':'Message',
        }
