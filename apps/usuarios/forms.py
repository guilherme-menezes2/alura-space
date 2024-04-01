from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(label='Nome do Login', required=True, max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ex.:João Silva'}))
    senha = forms.CharField(label='Senha', required=True, max_length=70, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Digite sua senha'}))

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(label='Nome de Cadastro', required=True, max_length=150, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ex.:João Silva'}))
    email = forms.EmailField(label='Email', required=True, max_length=150, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ex.:joaosilva@gmail.com'}))
    password1 = forms.CharField(label='Senha', required=True, max_length=70, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Digite sua senha'}))
    password2 = forms.CharField(label='Confirmação de senha', required=True, max_length=70, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Digite sua senha mais uma vez'}))

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Espaços não são permitidos nesse campo')
            else:
                return nome
            
    def clean_password2(self):
        senha1 = self.cleaned_data.get('password1')
        senha2 = self.cleaned_data.get('password2')

        if senha1 and senha2:
            if senha1 != senha2:
                raise forms.ValidationError('As senhas não coincidem')
            else:
                return senha2