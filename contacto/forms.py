from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class ContactoForm(forms.Form):
    asunto = forms.CharField(label="Asunto", required=True, widget=forms.TextInput(
        attrs={'class':'form-control'}
    ))
    mensaje = forms.CharField(label="Contenido del mensaje", required=True, widget=forms.Textarea(
        attrs={'class':'form-control'}
    ))
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox,
        public_key='6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI',
        private_key='6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe',
    )