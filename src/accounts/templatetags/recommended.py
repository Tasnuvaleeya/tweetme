from django import template
from django.contrib.auth import get_user_model
from accounts.models import UserProfile
from django.template.loader import get_template
from django.utils.safestring import mark_safe
register = template.Library()

User = get_user_model()


@register.inclusion_tag("accounts/snippets/recommend.html")
def recommended(user):
    if isinstance(user, User):
        qs = UserProfile.objects.recommended(user)
        return {"recommended": qs}


# @register.simple_tag()
# def recommended(user):
#     if isinstance(user, User):
#         template = get_template("accounts/snippets/recommeded.html")
#         context = {"recommended": UserProfile.objects.recommended(user)}
#         data = template.render(context=context)
#         content = mark_safe(data) # or @register.filter(is_safe=True)
#         return content
#     return ""