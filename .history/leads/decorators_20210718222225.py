from .models import Lead

def get_role_based_leads(func):
  def wrapper(request, *args, **kwargs):
    print(request.__dict__)
    return func(request, *args, **kwargs)
  return wrapper