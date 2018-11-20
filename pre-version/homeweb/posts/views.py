from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.forms import modelformset_factory
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import *
from .models import *

from haystack.generic_views import SearchView
from haystack.query import SearchQuerySet

#--View class
# Post
class PostListView(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
         return Post.objects.order_by('-pub_date')
"""
# Search Post List
class JSONResponseMixin:
    def render_to_json_response(self, context, **response_kwargs):
        return JsonResponse(
            self.get_data(context),
            **response_kwargs
        )

    def get_data(self, context):
        context = {'query': context['query']}
        return context

class ContentSearch(SearchView, JSONResponseMixin):
    def render_to_response(self, context, **response_kwargs):

        if self.request.is_ajax():
            sqs = SearchQuerySet().autocomplete(content_auto=self.request.GET.get('q', ''))[:5]
            suggestions = [result.username for result in sqs]

            # 기본 목록이 아닌 JSON 객체를 반환해야 한다.
            # 그렇지 않으면 XSS 공격에 취약할 수 있다.
            context = {'results': suggestions}

            return JsonResponse(context, safe=False)
         return render(self.request, 'search/search.html')

"""

#--View def
# Post
@login_required
def post_add(request): #변경
    ImageFormSet = modelformset_factory(Image, fields=('image', ), max_num=10, extra=5)    # 같은 페이지에서 여러 양식으로 작업하는 추상화 계층, extra=n n개의 공백 양식을 표시, 

    if request.method == 'POST':
        # PostForm은 파일을 처리하므로 request.FILES도 함께 바인딩
        # request.POST는 키로 전송된 자료에 접근할 수 있도록 해주는 사전과 같은 역할
        postForm = PostForm(request.POST, request.FILES)
        # formset은 여러 이미지 FormSet
        formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())    

        # post와 image 모두 값이 있으면
        if postForm.is_valid() and formset.is_valid():
            # user 필드를 채우기 위해 인스턴스만 생성   
            post_form = postForm.save(commit=False)
            # user 필드를 채운 후 DB에 저장
            post_form.user = request.user
            post_form.save()

            for form in formset.cleaned_date:
                image = form['image']
                photo = Image(post=post_form, image=image)
                photo.save()

            # 성공 알림을 messages에 추가 후 index.html로 이동
            messages.success(request, "홈페이지에서 확인하세요.")
            return HttpResponseRedirect(reverse('posts:index'))    # /으로 돌아감

        # post가 없거나 image가 없으면
        else:
            print(postForm.errors, formset.errors)    # error
    else:    # request != POST
        postForm = PostForm()
        formset = ImageFormSet(queryset=Image.objects.none())

    context = {'postForm': postForm, 'formset': formset}
    return render(request, 'posts/post_add.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    images = Image.objects.filter(post_id=pk)

    comments = Comment.objects.filter(post_id=pk)
    comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'images': images,
        'comment_form': comment_form,
    }

    return render(request, 'posts/post_detail.html', context)


# Comment
@login_required
def comment_form(request, pk):
    # 요청 메서드가 POST 방식일 때만 처리
    if request.method == 'POST':
        # Post 인스턴스를 가져오거나 404 Response를 돌려줌
        post = get_object_or_404(Post, pk=pk)
        # request.POST에서 'content' 키의 값을 가져옴
        form = CommentForm(request.POST)

        if form.is_valid():
            # 유효성 검사에 통과하면 ModelForm의 save()호출로 인스턴스 생성
            # DB에 저장하지 않고 인스턴스만 생성하기 위해 commit=False옵션 지정
            comment = form.save(commit=False)
            # CommentForm에 지정되지 않았으나 필수요소인 author와 post속성을 지정
            comment.post = post
            comment.user = request.user
            # DB에 저장
            comment.save()

            # 성공 메시지를 다음 request의 결과로 전달하도록 지정
            messages.success(request, '댓글이 등록되었습니다.')

        else:
            # 유효성 검사에 실패한 경우
            # 에러 목록을 순회하며 에러메시지를 작성, messages의 error 레벨로 추가
            error_msg = '댓글 등록에 실패했습니다\n{}'.format (
                '\n'.join (
                    ['-{error}'
                    for key, vlaue in form.errors.items()
                    for error in value]))
            messages.error(request, error_msg)

        return HttpResponseRedirect(reverse('posts:post_detail', args=(post.id,)))
