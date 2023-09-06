from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record


def home(request):
	records = Record.objects.all()
	# Check to see if logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In!")
			return redirect('home')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again...")
			return redirect('home')
	else:
		return render(request, 'home.html', {'records':records})



def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')





from django.shortcuts import render, redirect
from .forms import AddRecordForm






def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})



def customer_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')



def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')


def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
	
# Adding forgot password
def search(request):
    return render(request, 'search.html')



def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')

# *******************************************************************************************

import csv
from django.http import HttpResponse
from .models import Record

def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="records.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'id', 'Erp_Id', 'Name', 'Address',
		'District', 'City', 'State', ' Pin', 'Phone', 'Vdiscountpercent', ' Email', 
		'Popsstrata', 'Businesstype', ' Warehouse_Type', ' Warehouse_Category', 'Prefix_To_Billno', 'Suffix_To_Billno', 
		'Prefix_To_Creditno', 'Suffix_To_Creditno', 'Prefix_To_Debitno', 'Suffix_To_Debitno', 'Prefix_To_Salereturnno', 
		'Suffix_To_Salereturnno', 'Prefix_Challan_Number', 'Suffix_Challan_Number', 'Warehouse_Label', 'Area_Pin_Code', 
		'Default_Credit_Limit', 'Default_Credit_Period', 'Default_Minimum_Order_Value', 'Subzone', 'Parent_Warehouse', 
		'Currency', 'QR_Code_Image', 'Warehouse_TIN', 'PAN_no', 'FSSAI_no', ' Warehouse_CST', 'GSTIN', 'Warehouse_LBT_no', 
		'Jurisdiction', 'Country_WMS', 'Tenant_WMS', 'Category_WMS', 'Address_type_WMS', 'Address_line2_WMS', 'Status_WMS', 
		'Zone_code_WMS', 'Lat_WMS', 'Long_WMS'
		   
    ])

    records = Record.objects.all()  # Replace YourRecordModel with your actual model name

    for record in records:
        writer.writerow([
            record.id,record.erp_Id, record.Name, record.Address, record.District, record.City,
			record.State, record.Pin, record.Phone, record.Vdiscountpercent, record.Email, record.Popsstrata,
			record.Businesstype, record.Warehouse_Type, record.Warehouse_Category, record.Prefix_To_Billno, record.Suffix_To_Billno,
			record.Prefix_To_Creditno, record.Suffix_To_Creditno, record.Prefix_To_Debitno, record.Suffix_To_Debitno,
			record.Prefix_To_Salereturnno, record.Suffix_To_Salereturnno, record.Prefix_Challan_Number, record.Suffix_Challan_Number,
			record.Warehouse_Label,record.Default_Credit_Limit, record.Default_Credit_Period, record.Default_Minimum_Order_Value,
			record.Subzone, record.Parent_Warehouse, record.Currency, record.QR_Code_Image, record.Warehouse_TIN, record.PAN_no, 
			record.FSSAI_no, record.Warehouse_CST, record.GSTIN, record.Warehouse_LBT_no, record.Jurisdiction, record.Country_WMS,
			record.Tenant_WMS, record.Category_WMS, record.Address_type_WMS, record.Address_line2_WMS,
			record.Status_WMS, record.Zone_code_WMS, record.Lat_WMS,record.Long_WMS  # Add all other fields here
        ])

    return response
