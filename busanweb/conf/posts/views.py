from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList

from .models import *
from .forms import *

# Create your views here.

# Post
"""
class PostListView(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')
"""
def post_list(request):
    latest_post_list = Post.objects.order_by('-pub_date')
    categorys = Categ.objects.all()

    context = {
        'latest_post_list': latest_post_list,
        'categorys': categorys,
    }

    return render(request, 'posts/index.html', context)


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

# Category
"""
class CategoryListView(ListView):
    model = Categ
    template_name = 'category_list.html'
    context_object_name = 'latest_category_list'

    def get_queryset(self):
        return Category.objects.order_by('-pub_date')

def category_detail(request, pk):
    # tag를 가진 post list를 나열한다.
    category = get_object_or_404(Categ, pk=pk)
    tags = category.tags
    tagManager = models.TaggedItemManager

    queryset = tagManager.get_by_model(Post, tags)

    context = {
        'posts': queryset,
        'category': category,
    }

    return render(request, 'posts/category_detail.html', context)
"""

class CategoryDetailView(TaggedObjectList):
    model = Post
    template_name = 'posts/category_detail.html'

