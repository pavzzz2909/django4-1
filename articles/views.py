from django.shortcuts import render

from articles.models import Article, Scope, ArticleScopes


def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.all()
    object_list = []
    for article in articles:
        tags = article.scopeart.all().order_by('-is_main', 'scope__name')
        object_list.append({'article': article, 'tag': tags})
    context = {'object_list' : object_list}
    return render(request, template, context)
