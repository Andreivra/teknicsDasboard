import django_filters
from agent.models import Agent


class AgentFilters(django_filters.FilterSet):
    get_agents = [(agent.first_name, agent.first_name.upper()) for agent in Agent.objects.filter(active=True)]
    first_name = django_filters.ChoiceFilter(choices=list(set(get_agents)))
    last_name = django_filters.CharFilter(lookup_expr='icontains', label='Last name')
    course = django_filters.CharFilter(lookup_expr='exact', label='Course')

    #    department =

    class Meta:
        model = Agent
        fields = ['first_name', 'last_name', 'course']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['first_name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter first name'})
        self.filters['last_name'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter last name'})
        self.filters['course'].field.widget.attrs.update({'class': 'form-control',
                                                          'placeholder': 'Please enter course'})
