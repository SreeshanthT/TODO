from django.shortcuts import get_object_or_404

def get_object_or_none(model,**kwargs):
    try:
        return get_object_or_404(model,**kwargs)
    except:
        return None