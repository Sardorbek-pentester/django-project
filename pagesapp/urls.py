from django.urls import path
from .views import HomePageView, DatailView, FreeAudit, EditInfo, AboutPageView, BlogPageView, ContentCreation,ContentStrategy

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('about_us/',AboutPageView.as_view(),name='about_us'),
    path('blog/',BlogPageView.as_view(),name='blog'),
    path('content_creation/',ContentCreation.as_view(),name='content_creation'),
    path('content_strategy/',ContentStrategy.as_view(),name='content_strategy'),

    path("datail/<int:pk>/", DatailView.as_view(), name="datail"),
    path("new", FreeAudit.as_view(), name="free_audit"),
    path("projects/<int:pk>/edit/", EditInfo.as_view(), name="edit")
]
