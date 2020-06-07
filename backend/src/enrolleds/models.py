from djongo import models
from django import forms
from HallOfFame.settings import AUTH_USER_MODEL
from marks.models import Mark
from inattendances.models import Inattendance
from users.models import User


class Enrolled(models.Model):
    student = models.ForeignKey(AUTH_USER_MODEL, models.PROTECT, blank=False, null=False)
    inattendances_list = models.ArrayField(model_container=Inattendance, default=[], blank=False, null=False)
    marks_list = models.ArrayField(model_container=Mark, default=[], blank=False, null=False)
    final_grade = models.FloatField(blank=True, null=True)
    objects = models.DjongoManager()

    # class Meta:
    #     abstract = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class EnrolledForm(forms.ModelForm):
    class Meta:
        model = Enrolled
        fields = ('student', 'inattendances_list', 'marks_list', 'final_grade')
