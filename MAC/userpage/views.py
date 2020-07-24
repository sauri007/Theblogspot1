from django.shortcuts import render,HttpResponse,redirect
from .models import Post,Profile,Like,Following
from django.contrib import messages
from django.contrib.auth.models import User
import json
from django.views.generic import ListView
from django.core.paginator import Paginator



# Create your views here.
def userhome(request):
    user= Following.objects.get(user=request.user)
    followed_users = [i for i in user.followed.all()]
    followed_users.append(request.user)
    posts = Post.objects.filter(user__in=followed_users).order_by('-pk')

    liked_ =[i for i in posts if Like.objects.filter(post=i,user=request.user)]
    data = {
        "posts": posts,
        "liked_post":liked_,
    }
    return render(request,"userpage/postfeed.html",data)


def post(request):
    if request.method == 'POST':
        image_ = request.FILES['image']
        user_ = request.user
        caption_= request.POST.get('captions','')

        post_obj = Post(user=user_,caption=caption_,image=image_)
        post_obj.save()
        messages.success(request,'post successful')
        return redirect('/userpage')
    else:
        messages.error(request,'sorry !! somethimg went wrong')
        return redirect('/userpage')


def delpost(request,ID):
    post_= Post.objects.filter(pk=ID)
    image_path = post_[0].image.url
    post_.delete()
    messages.info(request,'post deleted successfully')
    return redirect('/userpage')


def userprofile(request,username):#if user exist
    user= User.objects.filter(username=username)# filter list return krta h
    if user:
        user=user[0]
        profile = Profile.objects.get(user=user)
        bio = profile.bio
        post_ = getPost(user)
        conn= profile.connection
        is_following = Following.objects.filter(user=request.user,followed=user)
        user_img =profile.user_Image
        following_obj = Following.objects.get(user = user)
        follower, following = following_obj.follower.count(), following_obj.followed.count()
        data={'username':username,
              'bio':bio,
              'conn':conn,
              'follower':follower,
              'following':following,
              'userimg':user_img,
              'posts':post_,
              'connection' : is_following,}
    else : return HttpResponse("No such User")
    return render(request,"userpage/userprofile.html",data)


def getPost(user):
    post_obj=Post.objects.filter(user=user)
    imgList = [post_obj[i:i+3] for i in range (0,len(post_obj),3)]
    return imgList


def likePost(request):
    post_id = request.GET.get("likeId","")

    post = Post.objects.get(id=post_id)
    user = request.user
    like = Like.objects.filter(post=post,user=user)
    liked = False

    if like:
        Like.dislike(post,user)
    else:
        liked = True
        Like.like(post,user)
    resp = {
        'liked':liked
    }
    response = json.dumps(resp)
    return HttpResponse(response,content_type="application/json")



def comment(request):
    comment_ = request.GET.get('comment_text', '')
    print(comment_)
    return render(request, "userpage/comment.html")


def follow(request,username):
    main_user = request.user
    to_follow = User.objects.get(username=username)

    # if already followed
    following = Following.objects.filter(user = main_user,followed = to_follow)
    is_followed = True if following else False

    if is_followed:
        #if already followed
        Following.unfollow(main_user,to_follow)
        is_followed = False
    else:
        # if not followed
        Following.follow(main_user,to_follow)
        is_followed = True

    resp = {
        "following" : is_followed
    }

    response= json.dumps(resp)
    return HttpResponse(response,content_type="application/json")


class Search_User(ListView):
    model =User
    template_name="userpage/searchuser.html"
    paginate_by = 2
    def get_queryset(self):
        username = self.request.GET.get("username","")
        queryset = User.objects.filter(username__icontains = username)
        return queryset
