from django import forms

class NoteForm(forms.Form):
    note_txt = forms.CharField(label='Note:', max_length=4096, required=True)
    paper_id = forms.CharField(widget = forms.HiddenInput(), required=True)

    def is_valid(self):
        super(forms.Form, self).is_valid()

        return self.cleaned_data.get('note_txt') != None