
from django import forms


class GameForm(forms.Form):

    amount = forms.IntegerField(initial=100)

    def __init__(self, *args, **kwargs):
        """
        Add some HTML5 attributes to form fields.
        """
        super(GameForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if isinstance(field, forms.IntegerField):
                self.fields[name].widget.input_type = "number"
            if field.required:
                self.fields[name].widget.attrs["required"] = ""
