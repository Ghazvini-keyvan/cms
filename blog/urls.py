from django.urls import path
from blog.views import SharePost, category_view, BlogListView, BlogDetailView

urlpatterns = [
    # path('', list_view),
    path('', BlogListView.as_view()),
    # path(
    #     '<int:year>/<int:month>/<int:day>/<str:slug>',
    #     detail_view,
    #     name="blog-item"
    #     ),
    path(
        '<int:year>/<int:month>/<int:day>/<str:slug>',
        BlogDetailView.as_view(),
        name="blog-item"
        ),
    path('categories', category_view),
    path('share/<int:pk>', SharePost.as_view(), name='share-post')
]
