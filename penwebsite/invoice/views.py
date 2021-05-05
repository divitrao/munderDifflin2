from django.shortcuts import render
from django.core.mail import  send_mail,EmailMessage
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import  canvas
from reportlab.lib.pagesizes import  letter
from reportlab.platypus import  Table , SimpleDocTemplate , TableStyle
import  os
from pathlib import  Path
BASE_DIR = Path(__file__).resolve().parent.parent


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
            ink_quantity = request.POST.get('quatity_ink', None)
            context['ink_quantity'] = ink_quantity
            price_of_ink_pens = request.POST.get('costing_ink', None)
            print(f'ink quantity {ink_quantity} and  price of ink pen {price_of_ink_pens} and type is {type(ink_quantity)}')
            context['price_of_ink_pens'] = price_of_ink_pens

            ballPen_quantity = request.POST.get('quatity_ball',None)
            context['ballPen_quantity'] = ballPen_quantity
            ballPen_price = request.POST.get('costing_ball', None)
            context['ballPen_price'] = ballPen_price

            pilotPen_quantity = request.POST.get('quatity_pilot',None)
            context['pilotPen_quantity'] = pilotPen_quantity
            pilotPen_price = request.POST.get('costing_pilot', None)
            context['pilotPen_price'] = pilotPen_price

            # def info_table():



            def form(path):
                my_canvas = canvas.Canvas(path,pagesize=letter)
                # doc = SimpleDocTemplate('simple_table.pdf',pagesize = letter)
                # my_canvas.drawString(30,750,price_of_ink_pens)

                my_canvas.drawImage('logo.jpg',20,680,width=100,height=100)
                my_canvas.setFont('Helvetica',30)
                my_canvas.drawString(145,750,"DUNDER DIFFLIN pen corp. LTD.")
                my_canvas.setFont('Helvetica',30)
                my_canvas.drawString(180,650,"Products Bought from us")
                flowables = []


                data = [
                    ['pen type bought', 'quantity bought', 'price per piece', 'total cost']
                ]
                if int(ink_quantity)>0:
                    data.append(['ink_pen_model_001',ink_quantity,int(price_of_ink_pens)/int(ink_quantity),price_of_ink_pens])
                if int(ballPen_quantity)>0:
                    data.append(['ball_pen_model_001',ballPen_quantity,int(ballPen_price)/int(ballPen_quantity),ballPen_price])

                if int(pilotPen_quantity)>0:
                    data.append(['pilot_pen_model_001',pilotPen_quantity,int(pilotPen_price)/int(pilotPen_quantity),pilotPen_price])


                total_price_of_buyed_product = '₹'+ str(int(price_of_ink_pens) + int(ballPen_price) + int(pilotPen_price))
                tableStyle = TableStyle([
                    ('ALIGN', (0, 0), (-1, -1), "CENTER"),
                    ('FONTSIZE', (0, 0), (-1, -1), 13),
                    # ('ALIGN', (0, 7), (0, 7), "CENTER"),
                    ('TOPPADDING', (0, 0), (-1, -1), 15),
                    ('RIGHTPADDING', (0, 0), (-1, -1), 10)
                ])
                tb1 = Table(data)
                tb1.setStyle(tableStyle)
                tb1.wrapOn(my_canvas,100,200)
                tb1.drawOn(my_canvas,100,500)
                my_canvas.drawString(180,400,'total price is ')
                my_canvas.drawString(400,400,total_price_of_buyed_product)
                # flowables.append(tb1)
                # doc.build(flowables)

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
        # file_path = r"C:\Users\divit\PycharmProjects\dunder_difllin\penwebsite\invoices.pdf"
        file_path = os.path.join(BASE_DIR,'invoices.pdf')
        # file_path = r'in'
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
        emails.attach('invoice copy',file2.read(),'application/pdf')
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


