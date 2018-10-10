# workarounds.py contains workarounds and monkey-patches for external issues.


# TODO: Remove on release with bugfix
# Problem: problems with polymorphic and on_delete=CASCADE
# Issue: https://github.com/django-polymorphic/django-polymorphic/issues/
#        229#issuecomment-398434412
def NON_POLYMORPHIC_CASCADE(collector, field, sub_objs, using):
    from django.db.models import CASCADE
    sub_objs = sub_objs.non_polymorphic() \
        if hasattr(sub_objs, 'non_polymorphic') else sub_objs
    return CASCADE(collector, field, sub_objs, using)
