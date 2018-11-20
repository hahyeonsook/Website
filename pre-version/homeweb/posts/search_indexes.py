import datetime
from haystack import indexes
from .models import Post
# from accounts.models import User

class PostIndex(indexes.SearchIndex, indexes.Indexable):
    # document=True: 검색할 때, text 필드를 최우선 순위로 사용하겠다는 뜻
    text = indexes.CharField(document=True, use_template=True, template_name='search/post_test.txt')
    # model_attr: 반드시 model에 있는 column을 지정해야 함
    user = indexes.CharField(model_attr='user')
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    # 어떤 model을 변환시킬지 지정하는 것
    def get_model(self):
        return Post
    # 인덱싱할 객체들을 거를 수 있음
    def index_queryset(self, using=None):
        return self.get_model().objects.all()

"""
class MyUserIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name="search/myuser_text")
    # context_auto 추가
    # Haystack의 자동완성 기능을 사용하기 위해 사용해야 한다(공식문서).
    # username을 자동완성시키기 위해 model_attr 부분에 username으로 씀
    context_auto = indexes.EdgeNgramField(model_attr='username')

    def get_model(self):
        return MyUser

    def index_queryset(self, using=None):
       # 모델의 전체 색인이 업데이트 될 때 사용된다.
       return self.get_model().objects.all()
"""
