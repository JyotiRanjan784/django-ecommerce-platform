from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import razorpay

# Create your views here.
def index(request):
    allProds = []
    cats = Product.objects.values('category', 'id')
    categories = {item['category'] for item in cats}
    for cat in categories:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = ceil(n / 4)
        allProds.append([prod, list(range(1, nSlides)), nSlides])
    return render(request, 'shop/index.html', {'allProds': allProds})

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
        return render(request, 'shop/contact.html', {'thank': True})
    return render(request, 'shop/contact.html', {'thank': thank})

def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId')

        email = request.POST.get('email')
        if not orderId or not email:
            return JsonResponse([], safe=False)
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if order.exists():
                updates_qs = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in updates_qs:
                    updates.append({
                        'text': item.update_desc,
                        'time': str(item.timestamp)
                    })
                return JsonResponse([updates, order[0].items_json], safe=False)
            return JsonResponse([], safe=False)
        except Exception as e:
            print(e)
            return JsonResponse([], safe=False)
    return render(request, 'shop/tracker.html')

def searchMatch(query, item):
    query = query.lower().strip()

    if not query:
        return False

    if query in item.product_name.lower():
        return True

    if query in item.category.lower():
        return True

    if query in item.subcategory.lower():
        return True

    if query in item.desc.lower():
        return True

    return False

def search(request):
    query = request.GET.get('search', '').strip()
    allProds = []
    if query:
        products = Product.objects.all()
        prod = [
            item for item in products
            if searchMatch(query, item)
        ]
        n = len(prod)
        nSlides = ceil(n / 4)
        if n > 0:
            allProds.append([
                prod,
                list(range(1, nSlides)),
                nSlides
            ])
    return render(
        request,
        'shop/search.html',
        {
            'allProds': allProds,
            'query': query
        }
    )

def productView(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/prodView.html', {'product': product[0]})

def checkout(request):
    if request.method == "POST":
        import json
        items_json = request.POST.get('items_json', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')

        if not items_json or items_json == "{}":
            return redirect('checkout')

        items = json.loads(items_json)
        amount = 0

        for item in items.values():
            amount += item['qty'] * item['price']

        order = Orders(
            items_json=items_json,
            name=name,
            amount=amount,
            email=email,
            address=address,
            city=city,
            state=state,
            zip_code=zip_code,
            phone=phone
        )
        order.save()

        update = OrderUpdate(
            order_id=order.order_id,
            update_desc='The order has been placed successfully'
        )
        update.save()

        return redirect(f'/shop/payment/?order_id={order.order_id}')

    order_id = request.GET.get('order_id')
    return render(request, 'shop/checkout.html', {
        'thank': bool(order_id),
        'order_id': order_id
    })

def payment(request):
    order_id = request.GET.get('order_id')

    if not order_id:
        return HttpResponse("Order ID is missing")

    try:
        order = Orders.objects.get(order_id=order_id)
    except Orders.DoesNotExist:
        return HttpResponse("Order not found")

    client = razorpay.Client(
        auth=(
            settings.RAZORPAY_KEY_ID,
            settings.RAZORPAY_KEY_SECRET
        )
    )

    amount_paise = int(order.amount * 100)

    razorpay_order = client.order.create({
        "amount": amount_paise,
        "currency": "INR",
        "receipt": str(order.order_id)
    })

    order.razorpay_order_id = razorpay_order["id"]
    order.payment_status = "Pending"
    order.save()

    context = {
        "key": settings.RAZORPAY_KEY_ID,
        "amount": amount_paise,
        "amount_rupees":order.amount,
        "order_id": razorpay_order["id"],
        "name": order.name,
        "email": order.email,
        "phone": order.phone,
    }
    return render(
        request,
        "shop/payment.html",
        context
    )

def payment_success(request):
    return HttpResponse("Payment Done Successfully ✅")


@csrf_exempt
def payment_success(request):

    if request.method != "POST":
        return HttpResponse("Invalid request method")

    razorpay_payment_id = request.POST.get(
        "razorpay_payment_id"
    )

    razorpay_order_id = request.POST.get(
        "razorpay_order_id"
    )

    razorpay_signature = request.POST.get(
        "razorpay_signature"
    )

    # Make sure all values were received
    if not all([
        razorpay_payment_id,
        razorpay_order_id,
        razorpay_signature
    ]):
        return HttpResponse(
            "Payment verification failed: missing payment data"
        )

    try:
        # Find our Django order using the Razorpay Order ID
        order = Orders.objects.get(
            razorpay_order_id=razorpay_order_id
        )

    except Orders.DoesNotExist:
        return HttpResponse(
            "Payment verification failed: order not found"
        )

    client = razorpay.Client(
        auth=(
            settings.RAZORPAY_KEY_ID,
            settings.RAZORPAY_KEY_SECRET
        )
    )

    try:
        # Verify Razorpay signature
        client.utility.verify_payment_signature({
            "razorpay_order_id": order.razorpay_order_id,
            "razorpay_payment_id": razorpay_payment_id,
            "razorpay_signature": razorpay_signature,
        })

        # Store payment details
        order.razorpay_payment_id = razorpay_payment_id
        order.razorpay_signature = razorpay_signature

        # Check payment status from Razorpay
        payment = client.payment.fetch(
            razorpay_payment_id
        )

        payment_status = payment.get("status")

        if payment_status == "captured":

            order.payment_status = "Paid"
            order.save()

            return render(
                request,
                "shop/payment_success.html",
                {
                    "order": order
                }
            )

        elif payment_status == "authorized":

            # Capture the authorized payment
            client.payment.capture(
                razorpay_payment_id,
                int(order.amount * 100)
            )

            order.payment_status = "Paid"
            order.save()

            return render(
                request,
                "shop/payment_success.html",
                {
                    "order": order
                }
            )

        else:

            order.payment_status = "Failed"
            order.save()

            return HttpResponse(
                f"Payment was not captured. Status: {payment_status}"
            )

    except razorpay.errors.SignatureVerificationError:

        order.payment_status = "Failed"
        order.save()

        return HttpResponse(
            "Payment verification failed: invalid signature"
        )

    except Exception as e:

        print("RAZORPAY ERROR:", e)

        return HttpResponse(
            "Payment processing failed"
        )
