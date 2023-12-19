from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from blog.forms import EmailSendForm, CustomSignUpForm
from blog.models import Post
from django.core.mail import send_mail
from blog.forms import EmailSendForm, CommentForm
from taggit.models import Tag
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def post_list_view(request, tag_slug=None):
    post_list = Post.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page')  # page is available in paginator module
    try:
        post_list = paginator.page(page_number)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, 'blog/post_list.html', {'post_list': post_list, 'tag': tag})

@login_required
def post_detail_view(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status='published',
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    comments = post.comments.filter(active=True)
    csubmit = False
    form = CommentForm()  # Initialize form outside the condition

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            csubmit = True
    else:
        form = CommentForm()  # You might not need this 'else' block

    return render(
        request,
        'blog/post_detail.html',
        {'post': post, 'form': form, 'comments': comments, 'csubmit': csubmit}
    )

@login_required
def mail_send_view(request, id):
    post = get_object_or_404(Post, id=id, status='published')
    sent = False
    form = None  # Initialize the form variable outside the conditional blocks

    if request.method == 'POST':
        form = EmailSendForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you to read "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read Post At: \n{}\n\n{}\'s Comments:\n{}'.format(post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'durga@blog.com', [cd['to']])
            sent = True
    else:
        form = EmailSendForm()  # For GET requests or if form is not valid, create a new form instance

    return render(request, 'blog/sharebymail.html', {'post': post, 'form': form, 'sent': sent})


# signup functionality
def signup_view(request):
    if request.method == 'POST':
        form = CustomSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)  # make password encrypted
            user.save()  # save to database
            login(request, user)
            return redirect('/accounts/login')  # Redirect to the home page or any other desired page

    else:
        form = CustomSignUpForm()
    return render(request, 'blog/signup.html', {'form': form})


# logout functionality
def logout_view(request):
    return render(request, 'registration/logout.html')

@login_required
def about_us_view(request):
    return render(request, 'blog/aboutus.html')

@login_required
def home_view(request):
    return render(request, 'blog/home.html')



