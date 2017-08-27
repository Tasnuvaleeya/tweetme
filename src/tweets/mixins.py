from django import forms
from django.forms.utils import ErrorList
# from .views import TweetCreateView

class FormUserNeededMixin(object):
    def form_valid(self, form):
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
            return super(FormUserNeededMixin,self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS]=ErrorList(["User Must be logged in to continue"])
            return self.form_invalid(form)


class UserOwnerMixin(object):
    def form_valid(self,form):
        if form.instance.user == self.request.user:
            return super(UserOwnerMixin,self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS]=ErrorList(["This User is not allowed to change this data"])
            return self.form_invalid(form)
