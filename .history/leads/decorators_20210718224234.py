from .models import Lead

def get_role_based_leads(func):
  def wrapper(view, *args, **kwargs):
    print(view.__annotations__)
    user = view.request.user
    if user.is_organisor:
      queryset = Lead.objects.filter(organisation=user.userprofile)
    else:
      queryset = Lead.objects.filter(organisation=user.agent.organisation)
      # filte for the agent that is logged in
      queryset = queryset.filter(agent__user=user)
    view.queryset = queryset
    return func(view, *args, **kwargs)
  return wrapper