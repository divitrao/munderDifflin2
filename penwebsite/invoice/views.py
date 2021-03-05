from django.shortcuts import render
from django.core.mail import  send_mail,EmailMessage
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter



def home(request):
    # if request.method == 'POST':
    #     to_email = request.POST.get('to_email')
    #     messages = request.POST.get('text_boxes')
    #     send_mail(
    #         'TEST SUBJECT 001',  # subject
    #         messages,
    #         'divitrao97d@gmail.com',  # from_email
    #         [to_email]  # to email
    #
    #     )
    #
    #     return render(request, 'home.html')

    return  render(request,'home.html')
# def orderPage(request):
#     return render(request,'order_page.html')

def orderPage(request):
    if request.method == 'POST':
        # action = request.POST.get('submission')
        # if action == 'only_submit':
        #     global form1, form2, form3
        #     form1 = request.POST['inkPens']
        #     form2 = request.POST['ballpoint-pen']
        #     form3 = request.POST['pilot-pen']
        #     # print(form1)
        #     # print(form2)
        #     # print(form3)
        # if request.method=='POST':
            context = {}
            system = request.POST.get('quatity_ink', None)
            system1 = request.POST.get('costing_ink', None)
            context['system'] = system
            context['system1'] = system1
            def form(path):
                my_canvas = canvas.Canvas(path,pagesize=letter)
                my_canvas.drawString(30,750,system)
                my_canvas.save()
            form('invoices.pdf')
            # print(context[0])
            # print(type(context))
            # print(context.keys())
            # print(context.values())
            # print( context.get('system'))
            # print(len(context))
            return render(request, 'payments.html', context)
            # return render(request, 'payments.html')




    else:
        return render(request,'order_page.html')
def payments(request):
    if request.method == 'POST':
        to_email = request.POST.get('to_email')
        messages = request.POST.get('text_boxes')
        file_path = r"C:\Users\divit\PycharmProjects\dunder_difllin\penwebsite\invoices.pdf"
        # file = open(file_path,"r")
        file2 = open(file_path,"r")


        # send_mail(
        #     'TEST SUBJECT 001',# subject
        #     messages,
        #     'divitrao97d@gmail.com', #from_email
        #     [to_email] #to email
        #
        # )

        emails = EmailMessage('Test attchments 001',
                              messages,
                              'divitrao97d@gmail.com',
                              [to_email])
        # emails.attach(file_path,file.read(),'application/pdf')
        emails.attach(file_path,file2.read(),'application/pdf')
        emails.send()
    # if request.method=='POST':
    #     context = {}
    #     system = request.POST.get('selele', None)
    #     context['system'] = system
    #     print(context)
        return render(request, 'home.html')



    else:
        # if request.method=='POST':
        #     context = {}
        #     system = request.POST.get('selele', None)
        #     context['system'] = system
        #     print(context)
        #     return render(request, 'payments.html', context)

        return render(request,'payments.html')


