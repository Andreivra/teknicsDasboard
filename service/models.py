from django.db import models
from agent.views import Agent


class Service(models.Model):
    select_status_options = [('garantie', 'Garantie'), ('post_garantie', 'Post Garantie'), ('extern', 'Extern')]
    select_delivery_options = [('Curier', 'Curier'), ('Predat Client ', 'predare'), ('Ridicat Dantex', 'dtx')]

    company_name = models.CharField(max_length=30)
    contact_name = models.CharField(max_length=30)
    agent_name = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True)
    phone = models.IntegerField()
    email = models.EmailField(max_length=50)
    machine_class = models.CharField(max_length=50)
    machine_serial = models.CharField(max_length=50)
    task_name = models.CharField(max_length=50)
    task_description = models.TextField(max_length=600)
    task_asses = models.TextField(max_length=600)
    task_resolve = models.TextField(max_length=1000)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)
    select_delivery = models.CharField(choices=select_delivery_options, max_length=14)
    select_status = models.CharField(choices=select_status_options, max_length=14)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  # auto-now_add salveaza data si ora de creere
    updated_at = models.DateTimeField(auto_now=True)  # auto_now salveaza data ora cand se modifica intrarea

    def __str__(self):
        return f"{self.company_name} {self.task_description}"

    class Meta:
        ordering = ['complete']
