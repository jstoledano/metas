from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

# TODO: Create the base template
# TODO: Create a form class to show a form based in json field.
# TODO: Create a page to show a proof record using json field.