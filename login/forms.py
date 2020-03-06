from django import forms


class LoginForm(forms.Form):
    email_field = forms.EmailField(label="email", max_length=100,
                                   widget=forms.EmailInput(
                                       attrs={'class': "input100", 'placeholder': "Email"}))
    pass_field = forms.CharField(label='pass', max_length=100,
                                 widget=forms.PasswordInput(attrs={'class': 'input100',  'placeholder': "Enter Password"}))

    #  <input class="input100" type="text" name="email" placeholder="Email">

    # widget=forms.TextInput(attrs={'placeholder': "Enter Username"}))

# < input class ="input100" type="password" name="pass" placeholder="Password" >
