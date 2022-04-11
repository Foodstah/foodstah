from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import NewPostForm
from .models import Post
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa


def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

def recipe_to_pdf(request, pk):
    recipe = Post.objects.get(pk=pk)

    context={}
    context['post'] = recipe
    pdf = render_to_pdf('post/pdf_template.html', context_dict=context)

    response = HttpResponse(pdf, content_type='application/pdf')
    filename = f'Foodstah - {recipe.title}.pdf'
    content = f"attachment; filename={filename}"
    response['Content-Disposition'] = content
    return response

# Create your views here.

def post(request):
    posts = Post.objects.all().order_by('-date_created')
    return render(request, 'post/food-feed.html', {'posts':posts})

def add_post(request):
    if request.method == "POST":
        form = NewPostForm(request.POST, request.FILES)

        if form.is_valid():
            form.instance.author = request.user
            form.save()
            messages.success(request, "Your post was added successfully.")
            return redirect("food-feed")

        messages.info(request, "If you're adding a recipe you must include the ingredients, instructions and cooking time.")

    form = NewPostForm()
    return render(request, "post/add_post.html", {"addpost_form": form})

def give_like(request,pk):
    post = get_object_or_404(Post,id=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user.id)
    if request.META['HTTP_ACCEPT'] == "application/json":
        return JsonResponse({"reactions": post.likes.count()})
    return redirect("/food-feed")

def give_love(request,pk):
    post = get_object_or_404(Post,id=pk)
    if request.user in post.loves.all():
        post.loves.remove(request.user)
    else:
        post.loves.add(request.user.id)
    if request.META['HTTP_ACCEPT'] == "application/json":
        return JsonResponse({"reactions": post.loves.count()})
    return redirect("/food-feed")

def give_drooling_face(request,pk):
    post = get_object_or_404(Post,id=pk)
    if request.user in post.drooling_faces.all():
        post.drooling_faces.remove(request.user)
    else:
        post.drooling_faces.add(request.user.id)
    if request.META['HTTP_ACCEPT'] == "application/json":
        return JsonResponse({"reactions": post.drooling_faces.count()})
    return redirect("/food-feed")

def save_post(request,pk):
    post = get_object_or_404(Post,id=pk)
    if post.favorite_posts.filter(id=request.user.id).exists():
        post.favorite_posts.remove(request.user)
    else:
        post.favorite_posts.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def saved_post(request,username):
    user_saved_post = Post.objects.filter(favorite_posts=request.user)
    return render(request, "post/saved_post.html", {'user_saved_post':user_saved_post})








class PostDetailsView(DetailView):
    model = Post
    context_object_name = 'post'

class PostUpdateView(UpdateView):
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
    template_name = 'post/post-update.html'
    context_object_name = 'post'

class PostDeleteView(DeleteView):
    model = Post
    context_object_name = 'post'
    success_url = reverse_lazy('food-feed')