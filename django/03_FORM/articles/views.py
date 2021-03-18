from django.shortcuts import render

# Create your views here.
def explained_new(request):
    if request.method == 'GET':
        form = ArticleForm()
        context = {'form': form}
        return render(request '', context)

    elif request.method == "POST"




def new(request):
    if request.method == "POST":
        form = get_some()
        if form.is_valid():
            article = form.save()
            return redirect(article)
    elif request.method == "GET:
        form = get_some2()

    cxt = { 'form':form}

    return render( req, cxt) 


def new(request):
    if request.method == "GET:
        form = get_some2()
    elif request.method == "POST":
        form = get_some()
        if form.is_valid():
            article = form.save()
            return redirect(article)

    cxt = { 'form':form}

    return render( req, cxt) 