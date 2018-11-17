from django import forms
from .models import *

#--ModelForm
# Post
class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=50, label='제목')
    img = forms.ImageField(label='썸네일')
    content = forms.CharField(max_length=80, label='내용')

    class Meta:
        model = Post
        fields = ['title', 'img', 'content', 'user']

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='사진')

    class Meta:
        model = Image
        fields = ['image', ]

# Comment
class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'content',
                'placeholder': '댓글',
            }
        )
    )

    class Meta:
        model = Comment
        exclude = ['user', 'pub_date', 'post', ]

    def clean_content(self):
        data = self.cleaned_data['content']
        errors = []
        if data == '':
            errors.append(forms.ValidationError('댓글 내용을 입력해주세요.'))
        elif len(data) > 50:
            errors.append(forms.ValidationError('댓글 내용은 50자 이하로 입력해주세요.'))
        if errors:
            raise forms.ValidationError(errors)
        return data


#--def Form
# Post
def post_form(request):
    ImageFormSet = formset_factory(ImageForm, extra=5)    # 같은 페이지에서 여러 양식으로 작업하는 추상화 계층, extra=n n개의 공백 양식을 표시, 

    if request.method == 'POST':
        postForm = PostForm(request.POST)    # request.POST는 키로 전송된 자료에 접근할 수 있도록 해주는 사전과 같은 역할
        formset = ImageFormSet(request.POST, request.FILES)#, queryset=Image.objects.none())    # formset은 여러 이미지 FormSet

        if postForm.is_valid() and formset.is_valid():    # post와 image 모두 값이 있으면
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()

            for form in formset.cleaned_date:
                image = form['image']
                photo = Image(post=post_form, image=image)
                photo.save()
            messages.success(request, "홈페이지에서 확인하세요.")

            return HttpResponseRedirect("/")    # /으로 돌아감

        else:    # post가 없거나 image가 없으면
            print(postForm.errors, formset.errors)    # error
    else:    # request != POST
        postForm = PostForm()
        formset = ImageFormSet(Image.objects.none())

    context = {'postForm': postForm, 'formset': formset}
    return render(request, 'posts/post_form.html', context)

