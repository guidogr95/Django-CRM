from .models import Lead

def get_role_based_leads():
  def decorator(func):
    def wrapper(self, *args, **kwargs):
      user = self.request.user
      if user.is_organisor:
        queryset = Lead.objects.filter(organisation=user.userprofile)
      else:
        queryset = Lead.objects.filter(organisation=user.agent.organisation)
        # filte for the agent that is logged in
        queryset = queryset.filter(agent__user=user)
      return func(self, queryset=queryset, *args, **kwargs)
    return wrapper
  return decorator