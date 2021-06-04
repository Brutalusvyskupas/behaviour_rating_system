from django import forms
from django.db import models
from django.db.models import fields
from .models import Review


class RateForm(forms.ModelForm):
    text = forms.CharField(min_length=50, widget=forms.Textarea(attrs={"class": "block w-full p-3 rounded bg-gray-200 border border-transparent focus:outline-none",
                                                                       "placeholder": "Review"}), required=True)
    rate_professionalism = forms.IntegerField(
        min_value=1, max_value=5,  widget=forms.NumberInput(attrs={"class": "block p-3 rounded bg-gray-200 border border-transparent focus:outline-none", "placeholder": "0"}), required=True)
    rate_teamwork = forms.IntegerField(min_value=1, max_value=5,
                                       widget=forms.NumberInput(attrs={"class": "block p-3 rounded bg-gray-200 border border-transparent focus:outline-none", "placeholder": "0"}), required=True)
    rate_communication = forms.IntegerField(min_value=1, max_value=5,
                                            widget=forms.NumberInput(attrs={"class": "block p-3 rounded bg-gray-200 border border-transparent focus:outline-none", "placeholder": "0"}), required=True)
    rate_organize = forms.IntegerField(min_value=1, max_value=5,
                                       widget=forms.NumberInput(attrs={"class": "block p-3 rounded bg-gray-200 border border-transparent focus:outline-none", "placeholder": "0"}), required=True)
    rate_problem_solving = forms.IntegerField(min_value=1, max_value=5,
                                              widget=forms.NumberInput(attrs={"class": "block p-3 rounded bg-gray-200 border border-transparent focus:outline-none", "placeholder": "0"}), required=True)
    rate_personality = forms.IntegerField(min_value=1, max_value=5,
                                          widget=forms.NumberInput(attrs={"class": "block p-3 rounded bg-gray-200 border border-transparent focus:outline-none", "placeholder": "0"}), required=True)
    rate_reliability = forms.IntegerField(min_value=1, max_value=5,
                                          widget=forms.NumberInput(attrs={"class": "block p-3 rounded bg-gray-200 border border-transparent focus:outline-none", "placeholder": "0"}), required=True)

    class Meta:
        model = Review
        fields = (
            'text',
            'rate_professionalism',
            'rate_teamwork',
            'rate_communication',
            'rate_organize',
            'rate_problem_solving',
            'rate_personality',
            'rate_reliability',
        )
