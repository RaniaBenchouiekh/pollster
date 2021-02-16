from django.urls import path
from . import views

''' - Step 2 : This is basically a route, coming from the urls.py file
    in the pollster folder, we access the '' path which
    means '/polls' ( if we had 'result' instead of '' we would be
    redirected to '/polls/result'), then it accesses the index function
    in the views.py file

    - The detail method of views.py needs a question id, this id is gonna
    be passed throw the url like so <int:question_id> (a url parameter)
'''

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]
