import datetime
from haystack import indexes
from tagging.fields import TagField
from .models import Post

class PostIndex(indexes.SearchIndex, indexes.Indexable):
    # document=True: 검색할 때, text 필드를 최우선 순위로 사용하겠다는 뜻
    text = indexes.CharField(document=True, use_template=True, template_name='search/post_text.txt')
    # model_attr: 반드시 model에 있는 column을 지정해야 함
    user = indexes.CharField(model_attr='user')
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    # 어떤 model을 변환시킬지 지정하는 것
    def get_model(self):
        return Post
    # 인덱싱할 객체들을 거를 수 있음
    def index_queryset(self, using=None):
        return self.get_model().objects.all()

