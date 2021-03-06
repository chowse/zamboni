from django.shortcuts import get_object_or_404

import jingo

import amo.utils
from addons.models import Addon
from versions.models import Version

from .models import Review


def review_list(request, addon_id):
    addon = get_object_or_404(Addon, id=addon_id)

    versions = Version.objects.filter(addon=addon)
    q = Review.objects.filter(version__in=versions).order_by('-created')
    reviews = amo.utils.paginate(request, q)
    return jingo.render(request, 'reviews/review_list.html',
                        {'addon': addon, 'reviews': reviews})
