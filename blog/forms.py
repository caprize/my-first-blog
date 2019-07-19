from django import forms

from .models import Post,Order

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text','maintext','image')
class OrderForm(forms.ModelForm):
	"""docstring for OrderForm"""
	class Meta:
		model=Order
		fields=('tgid','dops')
