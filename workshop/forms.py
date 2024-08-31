from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
# Database models:
from .models import cuts, sizes, colors, lines, jobs


# Custom user creation form
class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=30, label='', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری'}))
    password1 = forms.CharField(max_length=30, label='', required=True, widget=forms.PasswordInput(attrs={'class': 'form-control mt-2', 'placeholder': 'گذرواژه'}))
    password2 = forms.CharField(max_length=30, label='', required=True, widget=forms.PasswordInput(attrs={'class': 'form-control mt-2', 'placeholder': 'تکرار گذرواژه'}))
    first_name = forms.CharField(max_length=30,label='', required=True, widget=forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'نام'}))
    last_name = forms.CharField(max_length=30, label='', required=True, widget=forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'نام خانوادگی'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class': 'form-control mt-2', 'placeholder': 'ایمیل'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']


# Custom login form
class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=30, label='', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری'}))
    password = forms.CharField(max_length=30, label='', required=True, widget=forms.PasswordInput(attrs={'class': 'form-control mt-2', 'placeholder': 'گذرواژه'}))

    class Meta:
        model = AuthenticationForm
        fields = ['username', 'password']


# Newcut Form
class cutsForm(forms.ModelForm):
    class Meta:
        model = cuts
        fields = ('cut', 'customcode', 'weight', 'colortype', 'sizetype', 'description')

        labels = {
            'cut': '',
            'customcode': '',
            'weight': '',
            'colortype': '',
            'sizetype': '',
            'description': '',
        }

        widgets = {
            
            'cut': forms.TextInput(attrs={'id': 'cutname',
                                           'class': 'form-control',
                                           'placeholder': 'برای مثال: تیشرت، تاپ، شلوار و...',
                                           'aria-describedby': 'نوع برش',}),

            'customcode': forms.NumberInput(attrs={'id': 'customcode',
                                                   'class': 'form-control',
                                                   'placeholder': '.اگر گزینه‌ی «کد دلخواه» غیرفعال باشد، کد برش بصورت خودکار وارد می‌شود',
                                                   'aria-describedby': 'کد برش',
                                                   'disabled': '',
                                                   'min': '1',
                                                   'step': '1'}),

            'weight': forms.NumberInput(attrs={'id': "weight",
                                               'class': 'form-control',
                                               'aria-describedby': 'وزن کل',
                                               'placeholder': 'بر حسب کیلوگرم',
                                               'step': '0.001',
                                               'min': '0.001',
                                               'required': ''}),

            'colortype': forms.RadioSelect(choices= (('سفید', 'سفید'),
                                                     ('رنگی', 'رنگی'),
                                                     ('چاپی', 'چاپی')),
                                                     attrs={'class': 'form-check-input ms-3'}),
            
            'sizetype': forms.RadioSelect(choices= (('بزرگسال', 'بزرگسال'),
                                                    ('خردسال', 'خردسال')),
                                                    attrs={'class': 'form-check-input ms-3'}),

            'description': forms.Textarea(attrs={'class': 'form-control',
                                                  'placeholder': 'توضیحات دلخواه...',
                                                  'aria-describedby': '"توضیحات"',
                                                  'rows': '3'}),
        }



# Colors form
class colorsForm(forms.ModelForm):
    class Meta:
        model = colors
        fields = ('color', 'amount')

        labels = {
            'color': '',
            'amount': ''
        }

        widgets = {
            'color': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),

            'amount': forms.NumberInput(attrs={'class': 'form-control form-control-sm',
                                               'min': '0',
                                               'step': '1'}),
        }

colorsFormSet = forms.formset_factory(
    colorsForm, extra=0
    )



# Sizes form
class sizesForm(forms.ModelForm):
    class Meta:
        model = sizes
        fields = ('size', 'amount')

        labels = {
            'size': '',
            'amount': ''
        }

        widgets = {
            'size': forms.TextInput(attrs={'hidden': ''}),

            'amount': forms.NumberInput(attrs={'class': 'form-control form-control-sm',
                                               'min': '0',
                                               'step': '1'}),
        }


sizesFormSet = forms.formset_factory(
    sizesForm, extra=0
    )



# lines form
class linesForm(forms.ModelForm):
    class Meta:
        model = lines
        fields = ('line',)

        labels = {
            'line': ''
        }

        widgets = {
            'line': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        }


linesFormSet = forms.formset_factory(
    linesForm, extra=0
    )

# NewJob cut option select
class jobsForm(forms.ModelForm):
    #cut = forms.ModelChoiceField(queryset=cuts.objects.filter(completed=0))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cut'].queryset = cuts.objects.filter(completed = False)
        self.fields['size'].choices = [('', '---------')]
        self.fields['color'].choices = [('', '---------')]
        self.fields['line'].choices = [('', '---------')]
        self.fields['user'].label_from_instance = lambda obj: f"{obj.first_name} {obj.last_name}"




    class Meta:
        model = jobs
        fields = ('cut', 'size', 'color', 'line', 'user')
        
        labels = {
            'cut': '',
            'size': '',
            'color': '',
            'line': '',
            'user': ''
        }

        widgets = {
            'cut': forms.Select(attrs={'class': 'form-select'}),
            'size': forms.Select(attrs={'class': 'form-select'}),
            'color': forms.Select(attrs={'class': 'form-select'}),
            'line': forms.Select(attrs={'class': 'form-select'}),
            'user': forms.Select(attrs={'class': 'form-select'}),
        }

