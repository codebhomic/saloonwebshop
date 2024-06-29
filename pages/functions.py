from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def paginate(content,page,howmany):
    paginator = Paginator(content, howmany)  # Show 10 contents per page
    try:
        contents = paginator.page(page)
    except PageNotAnInteger:
        contents = paginator.page(1)
    except EmptyPage:
        contents = paginator.page(paginator.num_pages)
    return contents