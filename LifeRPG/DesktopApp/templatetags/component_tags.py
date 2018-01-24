from django import template

register = template.Library()


@register.inclusion_tag('components/help_box.html')
def help_box(title, content):
    return{
        'title': title,
        'content': content,
    }


@register.inclusion_tag('components/level_bar.html', takes_context=True)
def level_bar(context):
    return context


@register.inclusion_tag('components/hearts.html', takes_context=True)
def hearts(context):
    profile = context['profile']
    heart_range = range(profile.hearts)
    empty_range = range(3-profile.hearts)
    return{'heart_range': heart_range, 'empty_range': empty_range}


@register.inclusion_tag('components/stats.html', takes_context=True)
def stats(context):
    return context


@register.inclusion_tag('components/focus.html', takes_context=True)
def focus(context):
    return context


@register.inclusion_tag('components/levelup_form.html', takes_context=True)
def levelup_form(context):
    return context
