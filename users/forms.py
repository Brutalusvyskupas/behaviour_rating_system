from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User, UserWorkOffice


class RegistrationForm(forms.ModelForm):

    first_name = forms.CharField(
        label='First name', max_length=50, help_text='Required', error_messages={
            'required': 'Sorry, you will need to enter your first name'})
    last_name = forms.CharField(
        label="Last name", max_length=50, help_text='Required', error_messages={
            'required': 'Sorry, you will need to enter your last name'})
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={
        'required': 'Sorry, you will need an email'})
    work_office = forms.ModelChoiceField(
        queryset=UserWorkOffice.objects.all(), required=True)
    title = forms.CharField(max_length=100, label="Title")
    phone_number = forms.CharField(max_length=20, label="Phone number")
    profile_image = forms.ImageField(required=False, widget=forms.FileInput)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput)
    gpdr_field = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "profile_image", "work_office",
                  "title", "phone_number", "password", "password2")

    # def clean_username(self):
    #     user_name = self.cleaned_data['user_name'].lower()
    #     r = UserBase.objects.filter(user_name=user_name)
    #     if r.count():
    #         raise forms.ValidationError("Username already exists")
    #     return user_name

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, that is already taken')
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if User.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError(
                'Please use another phone number, that is already taken')
        return phone_number

    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded-full py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white', 'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update(
            {'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded-full py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500', 'placeholder': 'Last Name'})
        self.fields['email'].widget.attrs.update(
            {'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded-full py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500', 'placeholder': 'you@example.com', 'name': 'email', 'id': 'id_email'})
        self.fields['work_office'].widget.attrs.update(
            {'class': 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded-full leading-tight focus:outline-none focus:bg-white focus:border-gray-500', 'placeholder': 'Office', 'name': 'email'})
        self.fields['title'].widget.attrs.update(
            {'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded-full py-3 px-4 leading-tight focus:outline-none focus:bg-white focus:border-gray-500', 'placeholder': 'title'})
        self.fields['phone_number'].widget.attrs.update(
            {'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded-full py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500', 'placeholder': 'Phone number'})
        self.fields['password'].widget.attrs.update(
            {'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded-full py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-gray-200 rounded-full py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-gray-500', 'placeholder': 'Repeat Password'})


class EditUserForm(forms.ModelForm):

    last_name = forms.CharField(
        label="Last name", max_length=50)
    email = forms.EmailField(max_length=100)
    work_office = forms.ModelChoiceField(
        queryset=UserWorkOffice.objects.all())
    title = forms.CharField(max_length=100, label="Title")
    phone_number = forms.CharField(max_length=20, label="Phone number")
    profile_image = forms.ImageField(required=False, widget=forms.FileInput)

    class Meta:
        model = User
        fields = ("last_name", "email", "work_office", "title", "phone_number", "profile_image")


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Email",
        widget=forms.TextInput(
            attrs={"class": "block w-full p-3 rounded bg-gray-200 border border-transparent focus:outline-none",
                   "placeholder": "Email", "id": "login-email"}
        ),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "block w-full p-3 rounded bg-gray-200 border border-transparent focus:outline-none", "placeholder": "Password", "id": "login-pwd"}),
    )
