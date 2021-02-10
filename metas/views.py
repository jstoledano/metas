from django.shortcuts import render
from django.views.generic import View
from django import forms
import json

from .forms import DEA2Form


meta = '''
[
  {
    "nombre": "Oficio",
    "requerido": true
  },
  {
    "nombre": "Correo electrónico",
    "requerido": true
  },
  {
    "nombre": "Acta",
    "requerido": false
  }
]
'''
campos = json.loads(meta)


class IndexView(View):
    form_class = DEA2Form
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {
            'name': 'Javier',
            'campos': campos,
            'form': form
        })

# TODO: Create the base template
# TODO: Create a form class to show a form based in json field.
# TODO: Create a page to show a proof record using json field.
