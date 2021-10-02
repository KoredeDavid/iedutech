from django import forms

from sayches.models import Pop


class PopForm(forms.ModelForm):
    class Meta:
        model = Pop
        exclude = ('user',)

    text = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        max_length=200
    )
    image = forms.FileField(
        widget=forms.FileInput(attrs={'accept': 'image/*', 'class': 'custom-file-input'})
    )
