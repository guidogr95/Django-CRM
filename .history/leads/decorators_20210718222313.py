from .models import Lead

def get_role_based_leads(func):
  def wrapper(view, *args, **kwargs):
    print(view.request)
    return func(view, *args, **kwargs)
  return wrapper