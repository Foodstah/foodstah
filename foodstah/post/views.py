from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import NewPostForm, NewCommentForm
from .models import Post
from user.models import User
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa

from django.conf import settings
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
from django.template.loader import render_to_string


def recipe_to_pdf(request, slug):
    font_config = FontConfiguration()
    recipe = Post.objects.get(slug=slug)
    title = recipe.title
    context = {}
    context["post"] = recipe

    html_template = render_to_string('post/pdf_template.html', context=context)
    html = HTML(string=html_template)
    css = CSS(
        string="""
        @font-face {
	font-family: Poppins;
	src: url(https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,200;0,400;0,700;0,800;1,200;1,400;1,900);
}


@page {
	size: A4; /* Change from the default size of A4 */
	margin: 40px; /* Set margin on each page */
}

body {
	font-family: Poppins
}
h1 {
	font-weight: 800;
	font-size: 44px;
	text-align: center;
	margin-bottom: 0;
	padding-bottom: 0;
    font-family: Poppins
}
h3 {
	margin-top: 10px;
	padding-left: 80px;
    text-align: right;
    display:block;
	font-weight: 800;
	font-size: 28px;
    color: #4B3FD8;
    font-family: Poppins
}

img {
	display: block;
	margin: auto;
	max-width: 350px;
	max-height: auto;
    border: 4px solid #4B3FD8;
    border-radius: 10px;
}

.inline {
	display: inline-block;
	margin: 0;
}

footer {
	display: block;
	position: fixed;
	bottom: 0px;
	left: 400px;
    color: #4B3FD8;
    border: 2px solid #4B3FD8;
    padding: 5px;
    border-radius: 10px;
}
.center{
    display: block;
    text-align: center;
    color: #4B3FD8;
}
""",
        font_config=font_config,
    )
    pdf_file = html.write_pdf(stylesheets=[css],
        font_config=font_config)

    
    response = HttpResponse(pdf_file, content_type='application/pdf')
    filename = f"Foodstah - {title}.pdf"
    content = f"attachment; filename={filename}"
    response['Content-Disposition'] = content
    return response

# def render_to_pdf(template_src, context_dict={}):
#     template = get_template(template_src)
#     html = template.render(context_dict)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type="application/pdf")
#     return None


# def recipe_to_pdf(request, pk):
#     recipe = Post.objects.get(pk=pk)

#     context = {}
#     context["post"] = recipe
#     pdf = render_to_pdf("post/pdf_template.html", context_dict=context)

#     response = HttpResponse(pdf, content_type="application/pdf")
#     filename = f"Foodstah - {recipe.title}.pdf"
#     content = f"attachment; filename={filename}"
#     response["Content-Disposition"] = content
#     return response


# Create your views here.


def post(request):
    posts = []
    for post in Post.objects.all().order_by("-date_created"):
        posts.append({
            'post': post,
            'is_favorite': post.favorite_posts.filter(id=request.user.id).exists()
        })
    return render(request, "post/food-feed.html", {"posts": posts})


def add_post(request):
    if request.method == "POST":
        form = NewPostForm(request.POST, request.FILES)

        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(request, "Your post was added successfully.")
            return redirect("food-feed")

        messages.info(
            request,
            "If you're adding a recipe you must include the ingredients, instructions and cooking time.",
        )

    form = NewPostForm()
    return render(request, "post/add_post.html", {"addpost_form": form})


def give_like(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user.id)
    if request.META["HTTP_ACCEPT"] == "application/json":
        return JsonResponse({"reactions": post.likes.count()})
    return redirect("/food-feed")


def give_love(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.user in post.loves.all():
        post.loves.remove(request.user)
    else:
        post.loves.add(request.user.id)
    if request.META["HTTP_ACCEPT"] == "application/json":
        return JsonResponse({"reactions": post.loves.count()})
    return redirect("/food-feed")


def give_drooling_face(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.user in post.drooling_faces.all():
        post.drooling_faces.remove(request.user)
    else:
        post.drooling_faces.add(request.user.id)
    if request.META["HTTP_ACCEPT"] == "application/json":
        return JsonResponse({"reactions": post.drooling_faces.count()})
    return redirect("/food-feed")


def save_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    if post.favorite_posts.filter(id=request.user.id).exists():
        post.favorite_posts.remove(request.user)
    else:
        post.favorite_posts.add(request.user)
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


def saved_post(request,username):
    user_saved_post = Post.objects.filter(favorite_posts=request.user)
    return render(request, "post/saved_post.html", {"user_saved_post": user_saved_post})


class PostDetailsView(DetailView):
    model = Post
    context_object_name = "post"


class PostUpdateView(SuccessMessageMixin , UpdateView):
    model = Post
    fields = [
        "title",
        "post_description",
        "main_image",
        "is_recipe",
        "ingredients",
        "recipe_description",
        "cooking_time",
    ]
    template_name = "post/post-update.html"
    context_object_name = "post"
    success_message = "Your post has successfully updated."

class PostDeleteView(DeleteView):
    model = Post
    context_object_name = "post"

    def get_success_url(self):
        messages.info(self.request, f"Your post was deleted successfully.")
        return reverse("food-feed")


def add_comment(request,slug):
    if request.method == "POST":
        form = NewCommentForm(request.POST)
        if form.is_valid():
            form.instance.username = User.objects.get(username=request.user)
            post = Post.objects.get(slug=slug)
            form.instance.post = post
            form.save()
            messages.success(request, "Your comment was added successfully.")
            return redirect("food-feed")
        messages.info(
            request,
            "There was an problem trying to add your comment.",
        )
    form = NewCommentForm()
    return render(request, "post/new_comment.html", {"new_comment_form": form})