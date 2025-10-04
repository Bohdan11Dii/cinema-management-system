from django.urls import path

from admin_panel.views import hello_world, SeoBlockListView, SeoBlockCreateView, SeoBlockUpdateView, SeoBlockDeleteView, \
    MainPageListView, MainPageCreateView, MainPageUpdateView, MainPageDeleteView, ContactPageListView, \
    ContactPageCreateView, ContactPageUpdateView, ContactPageDeleteView, NewsListView, NewsCreateView, NewsDeleteView, \
    NewsUpdateView, FilmListView, FilmCreateView, FilmDetailView, FilmUpdateView, FilmDeleteView, CinemaListView, \
    CinemaCreateView, CinemaUpdateView, CinemaDeleteView, HallListView, HallCreateView, HallUpdateView, HallDeleteView, \
    SeanceListView, SeanceCreateView, SeanceUpdateView, SeanceDeleteView, BackgroundListView, BackgroundCreateView, \
    BackgroundUpdateView, BackgroundDeleteView, BannerListView, BannerCreateView, BannerUpdateView, BannerDeleteView

urlpatterns = [
    path("", hello_world, name="hello-world"),

    path("seo_block/", SeoBlockListView.as_view(), name="seo-block-list"),
    path("seo_block/create/", SeoBlockCreateView.as_view(), name="seo-block-create"),
    path("seo_block/update/<int:pk>/", SeoBlockUpdateView.as_view(), name="seo-block-update"),
    path("seo_block/delete/<int:pk>/", SeoBlockDeleteView.as_view(), name="seo-block-delete"),

    path("main/", MainPageListView.as_view(), name="main-page-list"),
    path("main/create/", MainPageCreateView.as_view(), name="main-page-create"),
    path("main/update/<int:pk>/", MainPageUpdateView.as_view(), name="main-page-update"),
    path("main/delete/<int:pk>/", MainPageDeleteView.as_view(), name="main-page-delete"),

    path("contact_page/", ContactPageListView.as_view(), name="contact-page-list"),
    path("contact_page/create/", ContactPageCreateView.as_view(), name="contact-page-create"),
    path("contact_page/update/<int:pk>/", ContactPageUpdateView.as_view(), name="contact-page-update"),
    path("contact_page/delete/<int:pk>/", ContactPageDeleteView.as_view(), name="contact-page-delete"),

    path("news/", NewsListView.as_view(), name="news-list"),
    path("news/create/", NewsCreateView.as_view(), name="news-create"),

    path("news/delete/<int:pk>/", NewsDeleteView.as_view(), name="news-delete"),
    path("news/update/<int:pk>/", NewsUpdateView.as_view(), name="news-update"),

    path("films/", FilmListView.as_view(), name="film-list"),
    path("films/create/", FilmCreateView.as_view(), name="film-create"),
    path("films/detail/<int:pk>/", FilmDetailView.as_view(), name="film-detail"),
    path("films/update/<int:pk>/", FilmUpdateView.as_view(), name="film-update"),
    path("films/delete/<int:pk>/", FilmDeleteView.as_view(), name="film-delete"),

    path("cinemas/", CinemaListView.as_view(), name="cinema-list"),
    path("cinemas/create/", CinemaCreateView.as_view(), name="cinema-create"),
    path("cinemas/update/<int:pk>/", CinemaUpdateView.as_view(), name="cinema-update"),
    path("cinemas/delete/<int:pk>/", CinemaDeleteView.as_view(), name="cinema-delete"),

    path("halls/", HallListView.as_view(), name="hall-list"),
    path("halls/create/", HallCreateView.as_view(), name="hall-create"),
    path("halls/update/<int:pk>/", HallUpdateView.as_view(), name="hall-update"),
    path("halls/delete/<int:pk>/", HallDeleteView.as_view(), name="hall-delete"),

    path("seances/", SeanceListView.as_view(), name="seance-list"),
    path("seances/create/", SeanceCreateView.as_view(), name="seance-create"),
    path("seances/update/<int:pk>/", SeanceUpdateView.as_view(), name="seance-update"),
    path("seances/delete/<int:pk>/", SeanceDeleteView.as_view(), name="seance-delete"),

    path("backgoundbanners/", BackgroundListView.as_view(), name="back-list"),
    path("backgoundbanners/create/", BackgroundCreateView.as_view(), name="back-create"),
    path("backgoundbanners/update/<int:pk>/", BackgroundUpdateView.as_view(), name="back-update"),
    path("backgoundbanners/delete/<int:pk>/", BackgroundDeleteView.as_view(), name="back-delete"),
    path("banners/", BannerListView.as_view(), name="banner-list"),
    path("banners/create/", BannerCreateView.as_view(), name="banner-create"),
    path("banners/update/<int:pk>/", BannerUpdateView.as_view(), name="banner-update"),
    path("banners/delete/<int:pk>/", BannerDeleteView.as_view(), name="banner-delete"),

]

app_name = "admin_panel"
