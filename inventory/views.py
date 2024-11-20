from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Drug, StockLog

def scan_barcode(request):
    if request.method == 'POST':
        barcode = request.POST.get('barcode')
        name = request.POST.get('name')  # For new drug entry
        batch_number = request.POST.get('batch_number')
        expiration_date = request.POST.get('expiration_date')
        quantity = int(request.POST.get('quantity', 0))

        try:
            # Lookup the drug in the database
            drug = Drug.objects.get(barcode=barcode)
            # Update quantity for existing drug
            drug.quantity += quantity
            drug.save()
            
            # Log the stock update
            StockLog.objects.create(drug=drug, action='in', quantity=quantity)
        except Drug.DoesNotExist:
            if all([name, batch_number, expiration_date, quantity]):
                # Create a new drug entry
                drug = Drug.objects.create(
                    barcode=barcode,
                    name=name,
                    batch_number=batch_number,
                    expiration_date=expiration_date,
                    quantity=quantity,
                )
                # Log the stock addition
                StockLog.objects.create(drug=drug, action='in', quantity=quantity)
            else:
                context = {
                    'error': True,
                    'message': "Drug not found, and required fields are missing for new entry."
                }
                return render(request, 'inventory/scan_result.html', context)

        # Redirect to the drug list page after successful submission
        return redirect('drug_list')
    
    return render(request, 'inventory/scan_barcode.html')

def drug_list(request):
    drugs = Drug.objects.all()  # Fetch all drugs from the database
    return render(request, 'inventory/drug_list.html', {'drugs': drugs})