from django.http import HttpResponse

class WebhookHandler:
    '''
    A class to handle webhooks from the payment gateway
    '''
    def __init__(self, request):
        self.request = request
        
    def handle_event(self):
        '''
        Handle the webhook
        '''
        return HttpResponse(
            content=f'Webhook received: {self["type"]}',
            status=200)