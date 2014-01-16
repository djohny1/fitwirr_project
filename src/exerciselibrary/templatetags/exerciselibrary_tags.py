
import re, hashlib
from decimal import Decimal

from django import template
#from django.utils.safestring import mark_safe
#from django.utils.html import escape
#from django.conf import settings
#from django.contrib.humanize.templatetags.humanize import intcomma
#from django.utils.formats import number_format
from django.utils.translation import ungettext, ugettext as _

register = template.Library()

from exerciselibrary.models import UserLikeExerciseImage


@register.filter
def like_or_dislike_image(image, user):
    try:
	if image.userlikeexerciseimage_set.filter(user=user).count() > 0:
            return _("Dislike")
	else:
	    return _("Like")
    except:
        pass
    
    return _("Like")

