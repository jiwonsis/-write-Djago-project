from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail
from .models import Post, Comment
from .forms import EmailPostForm, CommentForm


def post_list(request, category=None  ):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # 만약 페이지 넘버가 정수형 타입이 아닌경우, 맨처음 페이지로 이동
        posts = paginator.page(1)
    except EmptyPage:
        # 만약 요청페이지가 검색결과 범위를 초과할경우, 마지막 페이지 호출
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html',
                  {'posts': posts, 'page': page})


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published',
                             publish__year=year, publish__month=month, publish__day=day)
    # 해당 포스트의 코멘트가 활성화(Active)된 리스트만 조회한다.
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        # 코멘트 폼 데이터 연동
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            # 선 노출, 후 DB 저장 방식은 낙관적 업데이트 롤백 방식을 차용하여 사용함
            # 댓글에 대한 객체는 만들지만, DB에 아직 저장하지 않는다.
            new_comment = comment_form.save(commit=False)
            # 현재 Post에 신규 댓글을 연동시킨다
            new_comment.post = post
            # 댓글을 DB에 저장한다.
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post/detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    })


def post_share(request, post_id):
    # post 의 id로 객체조회
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        # 이메일 폼을 수신 받을 경우,
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # 폼 검증한 값 검증
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "()" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comment'])
            send_mail(subject, message, 'interactord@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {
        'post': post, 'form': form, 'send': sent
    })
