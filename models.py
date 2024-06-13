from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Interaction(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    interaction_date = models.DateTimeField()
    attachments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.interaction_type} with {self.client}'

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order_name = models.CharField(max_length=200)
    order_description = models.TextField(blank=True, null=True)
    order_status = models.CharField(max_length=20, choices=[('in progress', 'In Progress'), ('completed', 'Completed')], default='in progress')
    due_date = models.DateField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_name

class Note(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    note_content = models.TextField()
    note_creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Note for {self.client}'


class MarketingCampaign(models.Model):
    campaign_name = models.CharField(max_length=200)
    campaign_description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    campaign_status = models.CharField(max_length=20, choices=[('active', 'Active'), ('completed', 'Completed')], default='active')

    def __str__(self):
        return self.campaign_name

class Ticket(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    ticket_subject = models.CharField(max_length=200)
    ticket_content = models.TextField(blank=True, null=True)
    ticket_priority = models.CharField(max_length=20, blank=True, null=True)
    ticket_status = models.CharField(max_length=20, choices=[('open', 'Open'), ('in progress', 'In Progress'), ('closed', 'Closed')], default='open')
    ticket_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ticket_subject

class PotentialClient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('new lead', 'New Lead'), ('in negotiation', 'In Negotiation'), ('lost', 'Lost')], default='new lead')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'