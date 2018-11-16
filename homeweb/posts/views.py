from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.forms import formset_factory
from django.views.generic import TemplateView
from .forms import PostForm, ImageForm
from .models import Image


#--BaseView
class PostListView(TemplateView):
    template_name = 'posts/index.html'


#--View def
"""
class PostFormView():

    def post(request):
        ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=5)    # 같은 페이지에서 여러 양식으로 작업하는 추상화 계층, extra=n n개의 공백 양식을 표

        if request.method == 'POST':
            postForm = PostForm(request.POST)    # PostForm을 postForm으로
            formset = ImageFormSet(request.POST, request.FILES, queryset=Images.objects.none())    # formset은 여러 이미지 FormSet

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
            formset = ImageFormSet(queryset=Images.objects.none())
        return render(request, 'index.html',
                      {'postForm': postForm, 'formset': formset},
                      context_instance=RequestContext(requust))

"""
def post(request):
    ImageFormSet = formset_factory(ImageForm, extra=5, max_num=1)    # 같은 페이지에서 여러 양식으로 작업하는 추상화 계층, extra=n n개의 공백 양식을 표시, 

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

