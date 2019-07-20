from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.first_view, name='first_view'),
    url(r'^uimage/$', views.uimage, name='uimage'), # 유이미지라는 주소를 넣으면 유미지라는 함수의 내용을 전달하겠다는 뜻임.
]
# ㅇㅕ기서 HTMl PAGE로 넘어감

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # 이미지파일을 넣어주겠다는 뜻임

