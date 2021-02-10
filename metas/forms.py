# coding: utf-8
#         app: metas 2021
#      module: forms
#        date: jueves, 14 de junio de 2018 - 08:56
# description: ...
# pylint: disable=W0613,R0201,R0903

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, HTML, Field, Button
from crispy_forms.bootstrap import FormActions
from django import forms

from metas.models import DEA2


class DEA2Form(forms.ModelForm):
    class Meta:
        model = DEA2
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DEA2Form, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Field('goal', wrapper_class='col-md-2'),
                Field('role', wrapper_class='col-md-2'),
                Field('date', wrapper_class='col-md-2'),
                css_class='row'
            ),
            Div(
                Field('oficio', wrapper_class='col-md-8'),
                Field('notificacion', wrapper_class='col-md-8'),
                css_class='row'
            ),
            Div(
                HTML('<hr>'),
                FormActions(
                    Submit('save', 'Guardar cambios'),
                    Button('cancel', 'Cancelar')
                )
            )
        )
