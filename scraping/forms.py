from django import forms

from scraping.models import City, Language, Vacancy


class FindForm(forms.Form):
    city = forms.ModelChoiceField(
        queryset=City.objects.all(), to_field_name='slug', required=False,
        widget=forms.Select(
            attrs={'class': 'form-control'}
        ),
        label='City'
    )
    language = forms.ModelChoiceField(
        queryset=Language.objects.all(), to_field_name='slug', required=False,
        widget=forms.Select(
            attrs={'class': 'form-control'}
        ),
        label='Vacancy'
    )


class VForm(forms.ModelForm):
    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        ),
        label='City'
    )
    language = forms.ModelChoiceField(
        queryset=Language.objects.all(),
        widget=forms.Select(
            attrs={'class': 'form-control'}
        ),
        label='Vacancy'
    )

    url = forms.CharField(label='URL', widget=forms.URLInput(
        attrs={'class': 'form-control'}))
    title = forms.CharField(label='Vacancy title', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    company = forms.CharField(label='Company', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    description = forms.CharField(label='Vacancy description',
                                  widget=forms.Textarea(
                                      attrs={'class': 'form-control'}))

    class Meta:
        model = Vacancy
        fields = '__all__'

