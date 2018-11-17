from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.forms import formset_factory
from django.views.generic import ListView
from .forms import PostForm, ImageForm, CommentForm
from .models import Post, Image, Comment


#--BaseView
class PostListView(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
         return Post.objects.order_by('-pub_date')

#--View def
def post_form(request):
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

def comment_form(request, pk):
    # 요청 메서드가 POST 방식일 때만 처리
    if request.method == 'POST':
        # Post 인스턴스를 가져오거나 404 Response를 돌려줌
        post = get_object_or_404(Post, pk=pk)
        # request.POST에서 'content' 키의 값을 가져옴
        form = CommentForm(request.POST)

        if form.is_valid():
            Comment.objects.create (
                post = post,
                user = request.user,
                content=form.cleaned_data['content']
            )

        return HttpResponseRedirect('/')
