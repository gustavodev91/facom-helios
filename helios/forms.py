"""
Forms for Helios
"""

from django import forms
from models import Election
from widgets import *
from fields import *
from django.conf import settings


class ElectionForm(forms.Form):
  short_name = forms.SlugField(max_length=40,label="Nome curto:",help_text='Sem espacos, este nome sera parte da URL para sua eleicao, ex: minha-eleicao-2017')
  name = forms.CharField(max_length=100, label="Nome:",widget=forms.TextInput(attrs={'size':60}), help_text='Nome para a eleicao, ex: Minha Eleicao 2017')
  description = forms.CharField(max_length=4000,label="Descricao:", widget=forms.Textarea(attrs={'cols': 70, 'wrap': 'soft'}), required=False)
  election_type = forms.ChoiceField(label="Tipo de eleicao:", choices = Election.ELECTION_TYPES)
  use_voter_aliases = forms.BooleanField(required=False,label="Pseudonimo:", initial=False, help_text='Se selecionado, a indentidade do eleitor sera substituida por um pseudonimo, ex:"V12", este pseudonimo estara presente na cedula')
  #use_advanced_audit_features = forms.BooleanField(required=False, initial=True, help_text='disable this only if you want a simple election with reduced security but a simpler user interface')
  randomize_answer_order = forms.BooleanField(label="Randomizar Candidatos:",required=False, initial=False, help_text='Ative para os candidatos aparecerem em ordem aleatoria para cada eleitor.')
  private_p = forms.BooleanField(required=False, initial=False, label="Privada:", help_text='Selecione para a eleicao se tornar visivel apenas aos eleitores autorizados.')
  help_email = forms.CharField(required=False, initial="", label="Email para ajuda:", help_text='Email para contato.')
  peso = forms.CharField(required=True, initial="", label="Peso:", help_text='Insira um peso para eleicao')
  
  if settings.ALLOW_ELECTION_INFO_URL:
    election_info_url = forms.CharField(required=False, initial="", label="Election Info Download URL", help_text="the URL of a PDF document that contains extra election information, e.g. candidate bios and statements")
  
  # times
  voting_starts_at = SplitDateTimeField(label="Inicio",help_text = 'Data e horario para o inicio da eleicao',
                                   widget=SplitSelectDateTimeWidget, required=False)
  voting_ends_at = SplitDateTimeField(label="Termino",help_text = 'Data e horario para o termino da eleicao',
                                   widget=SplitSelectDateTimeWidget, required=False)

class ElectionTimeExtensionForm(forms.Form):
  voting_extended_until = SplitDateTimeField(label="Extender:",help_text = 'Data e horario para extender a eleicao',
                                   widget=SplitSelectDateTimeWidget, required=False)
  
class EmailVotersForm(forms.Form):
  subject = forms.CharField(max_length=80)
  body = forms.CharField(max_length=4000, widget=forms.Textarea)
  send_to = forms.ChoiceField(label="Send To", initial="all", choices= [('all', 'all voters'), ('voted', 'voters who have cast a ballot'), ('not-voted', 'voters who have not yet cast a ballot')])

class TallyNotificationEmailForm(forms.Form):
  subject = forms.CharField(max_length=80)
  body = forms.CharField(max_length=2000, widget=forms.Textarea, required=False)
  send_to = forms.ChoiceField(label="Send To", choices= [('all', 'all voters'), ('voted', 'only voters who cast a ballot'), ('none', 'no one -- are you sure about this?')])

class VoterPasswordForm(forms.Form):
  voter_id = forms.CharField(max_length=50, label="Voter ID")
  password = forms.CharField(widget=forms.PasswordInput(), max_length=100)

