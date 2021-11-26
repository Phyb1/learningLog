from django.shortcuts import render, redirect
# the render function renders the response as provided by views
# redirect provides a way yo deal with form submission events

from .models import Topic, Entry #retrieving data from the database and sending it to the template


from .forms import TopicForm, EntryForm # these are the form models

from django.contrib.auth.decorators import login_required
#restricting access to specific pages

from django.http import Http404


def check_topic_owner(topc,req):
     if topc.owner != req.user:
         raise Http404

# Create your views here.

def index(request): # this is called when a request macthes a urlpattern
    """the homepage for learning_logs"""
    context = {'index':index}
    return render(request, 'learning_logs/index.html',context) # the first attribute is the original request and the second is a template to build the page

@login_required # using the decorator to prevent access to topics for users not logged in u should also modify the seettings.py file 
def topics(request): # the filter restricts access to the owner
    topics = Topic.objects.filter(owner=request.user).order_by('date')
     # querying the databaase and storing the queryset in topics
    context = {'topics':topics} # defining a contect we will send to the template, which is a dictionary in whc the keys are names we'll use in the template to access data
    return render(request, 'learning_logs/topics.html',context) # when building a pag that uses data we alsp pass the context variable , the path to the template and the request to render'''

@login_required # restricting access to logged in users
def topic(request, topic_id):
    """ show a single topic and all its entries"""
    topic = Topic.objects.get(id=topic_id)
    '''if topic.owner != request.user:  # restricting acces to topic owner
        raise Http404'''
    check_topic_owner(topic, request) # refactoring using a function to restrict access to owner
    entries = topic.entry_set.order_by('-date_added') #the minus sign is for sorting in reverse order recent first
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required 
def new_topic(request):
    '''adding a new topic'''
    if request.method != 'POST':
        # no data was submitted create a blank from
        form = TopicForm()
    else:
        # POST data submitted ; process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    # displaying a blank or invalid form
    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html',context)

@login_required 
def entries(request):
    entries = Entry.objects.order_by('date_added')
    context = {'entries':entries}
    render(request, 'learning_logs/entries.html', context)

@login_required 
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(topic, request)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topics')# , topic_id=topic_id
    context = {'topic': topic, 'form':form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required 
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # initial request: pre fill form with current entry
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry,  data=request.POST) #creating the form prefilled with info from the existing entry
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic',topic_id=topic.id)
    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.html', context)

