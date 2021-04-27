from django.urls import path
from .views import HomeView,AddKategoriView, CreateKomentView, DeletePostView, UpdatePostView, LikeView, PostDetailView, CreatePostView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('add_post/', CreatePostView.as_view(), name='add_post'),
    path('update_post/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('delete_post/<int:pk>', DeletePostView.as_view(), name='delete_post'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('koment/<int:pk>', CreateKomentView, name='add_koment'),
    path('add_kategori', AddKategoriView.as_view(), name='add_kategori'),


]