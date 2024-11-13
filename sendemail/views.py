from django.core.mail import send_mail
from django.http import JsonResponse
from rest_framework.views import APIView
import json

class sendFeedbackClass(APIView):
    def post(self,request):
    
        try:
            data = json.loads(request.body)
            
            message = data.get('msg')  
            from_email = data.get('email')
            first_name = data.get('fname')
            second_name = data.get('sname')
            if not message or not from_email:
                return JsonResponse({"error": "Missing message or email."}, status=400)
            
            subject = f"Feedback from {first_name} {second_name} {from_email}"

            recipient = ['athulbalaneb@gmail.com']
            
            send_mail(subject, message, from_email, recipient)
            
            return JsonResponse({"success": "Feedback sent successfully!"}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)