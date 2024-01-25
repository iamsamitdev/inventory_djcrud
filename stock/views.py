from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

# from django.http import HttpResponse

# ฟังก์ชัน product แสดงรายการสินค้าทั้งหมด
def index(request):
    products = Product.objects.all()
    # html = "<html><body>Home page</body></html>"
    #return HttpResponse(html)
    return render(request, 'frontend/index.html', {'products': products})


# ฟังก์ชันเพิ่มสินค้า
def create_product(request):
    if request.method == 'POST':

        # รับค่าจากฟอร์ม
        product_name = request.POST['product_name']
        product_detail = request.POST['product_detail']
        product_barcode = request.POST['product_barcode']
        product_qty = request.POST['product_qty']
        product_price = request.POST['product_price']
        product_image = request.POST['product_image']
        product_status = request.POST['product_status']
        
        # print(product_name, product_detail, product_barcode, product_qty, product_price, product_image, product_status)

        # สร้าง object Product
        product = Product(
            product_name=product_name,
            product_detail=product_detail,
            product_barcode=product_barcode,
            product_qty=product_qty,
            product_price=product_price,
            product_image=product_image,
            product_status=product_status
        )

        # บันทึกข้อมูลลงฐานข้อมูล
        product.save()

        # redirect กลับไปหน้าแรก
        return redirect('index')
    else:
        return render(request, 'frontend/create_product.html')


# ฟังก์ชันแก้ไขสินค้า
def update_product(request, product_id):
    # ค้นหาสินค้าที่ต้องการแก้ไข
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        
        # รับค่าจากฟอร์ม
        product.product_name = request.POST['product_name']
        product.product_detail = request.POST['product_detail']
        product.product_barcode = request.POST['product_barcode']
        product.product_qty = request.POST['product_qty']
        product.product_price = request.POST['product_price']
        product.product_image = request.POST['product_image']
        product.product_status = request.POST['product_status']

        # อัพเดทข้อมูล
        product.save()

        # redirect กลับไปหน้าแรก
        return redirect('index')
    else:
        return render(request, 'frontend/update_product.html', {'product': product})


# ฟังก์ชันลบสินค้า
def delete_product(request, product_id):
    # ค้นหาสินค้าที่ต้องการลบ
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        # ลบสินค้า
        product.delete()

        # redirect กลับไปหน้าแรก
        return redirect('index')
    else:
        return render(request, 'frontend/delete_product.html', {'product': product})

def about(request):
    return render(request, 'frontend/about.html')


def contact(request):
    return render(request, 'frontend/contact.html')