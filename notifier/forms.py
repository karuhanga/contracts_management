from django import forms
from core.utils.StringUtils import CLASS, INPUT
from notifier.models import NotificationPoint


class NotificationPointForm(forms.ModelForm):
    class Meta:
        model = NotificationPoint
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(NotificationPointForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({CLASS: INPUT})
        self.fields['when_time_left'].widget.attrs.update({CLASS: INPUT})
