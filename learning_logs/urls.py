"""defines url patterns for learning_logs"""
from django.urls import path # the path function is needed for mapping views to urls
from .import views # the . tells python to import the vies from the same directory
app_name = 'learning_logs' # these distinguish this urls.py from other files with the same name from different apps in the same project
urlpatterns = [ # this is a list of pages that can be requested from learning_logs
    #homepage
    path('', views.index , name='index'), # this is the actual url pattern
    # the first argument is the string after the base url, the second argument is a function to call in views,the third is a name that we can use to acces a certain view,
    #anytime we want to create a link we simplr provide the name rather than an url
    #page that shows all topics
    path('topics/', views.topics, name='topics'),# adding 'topics/' to the string used for the homepage u can include or omit the /

    # detailed page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #the first argument of path means
    #look for the urls with the topic after the base url then identfiy the integer variable topic_id
    #when this pattern matches django calls the views.topic function with topic_id as an argument

    # page for adding new topic
    path('new_topic/', views.new_topic, name='new_topic' ),

    # page for viewing all entries
    path('entries/', views.entries, name='entries'),

    # page for adding new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # page for editing entries
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry')
]