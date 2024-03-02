from django.shortcuts import render
from django.views.generic import TemplateView

class EditorView(TemplateView):
    template_name = 'text_editor/editor.html'