from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import *
from .models import Review
from django import forms

from crispy_forms.bootstrap import Field
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Div, Fieldset, Layout


class ReviewForm(forms.ModelForm):
    """Enable users to leave comments for products"""
    class Meta:
        model = Review
        fields = ('rating', 'review')

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        # create form structure using crispy forms
        self.helper = FormHelper()
        self.helper.form_id = 'product-review-form'
        self.helper.form_method = 'post'
        self.helper.form_class = 'mt-4'
        self.helper.add_input(
            Submit('submit', 'Add Review', css_class='btn btn-primary \
            float-right'))
        self.helper.layout = Layout(
            Fieldset('Add a product review',
                     Div(
                         Field('rating', wrapper_class='col-12 col-md-2'),
                         Field(
                             'review', wrapper_class='col-12 col-md-10',
                             rows=5, placeholder="Add your review here"),
                         css_class='row')
                     )
        )


class UserUpdateForm(ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = '__all__'



class DeliveryForm(forms.ModelForm):
    class Meta:
        model = delivery
        fields = ['hostel','phoneNumber','delivered_at']



class ContactForm(forms.ModelForm):
    class Meta:
            model = contact
            fields = [ 'name', 'email', 'subject', 'message' ]