from urllib.parse import parse_qs, urlencode, urlparse, urlunparse

from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def url_for_page(context, page_number):
    url = urlparse(context['request'].get_full_path())
    url_query = parse_qs(url.query)
    if page_number == 1:
        del url_query['page']
    else:
        url_query['page'] = page_number
    return urlunparse(url._replace(query=urlencode(url_query, doseq=True)))
