from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	




# Create Add Record Form


class AddRecordForm(forms.ModelForm):
   
    erp_Id = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="ERP ID")
    Name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={  "class": "form-control"}), label="Name")
    Address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={  "class": "form-control"}), label="Address")
    District = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={  "class": "form-control"}), label="District")
    City = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={  "class": "form-control"}), label="City")
    State = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={  "class": "form-control"}), label="State")
    Pin = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={  "class": "form-control"}), label="Pin")
    Phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={  "class": "form-control"}), label="Phone")
    Vdiscountpercent = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={  "class": "form-control"}), label="Vdiscountpercent")
    Email = forms.EmailField(required=True, widget=forms.TextInput(attrs={  "class": "form-control"}), label="Email")
    Popsstrata = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Popsstrata")
    Businesstype = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Businesstype")
    Warehouse_Type = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={  "class": "form-control"}), label="Warehouse Type")
    Warehouse_Category = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={  "class": "form-control"}), label="Warehouse Category")
    Prefix_To_Billno = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Prefix To Billno")
    Suffix_To_Billno = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Suffix To Billno")
    Prefix_To_Creditno = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Prefix To Creditno")
    Suffix_To_Creditno = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Suffix To Creditno")
    Prefix_To_Debitno = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Prefix To Debitno")
    Suffix_To_Debitno = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Suffix To Debitno")
    Prefix_To_Salereturnno = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Prefix To Salereturnno")
    Suffix_To_Salereturnno = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Suffix To Salereturnno")
    Prefix_Challan_Number = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Prefix Challan Number")
    Suffix_Challan_Number = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Suffix Challan Number")
    Warehouse_Label = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Warehouse Label")
    
    Default_Credit_Limit = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Default Credit Limit")
    Default_Credit_Period = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Default Credit Period")
    Default_Minimum_Order_Value = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Default Minimum Order Value")
    Subzone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Subzone")
    Parent_Warehouse = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Parent Warehouse")
    Currency = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Currency")
    QR_Code_Image = forms.ImageField(required=False, widget=forms.widgets.FileInput(attrs={"class": "form-control"}), label="QR Code Image")
    Warehouse_TIN = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Warehouse TIN")
    PAN_no = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="PAN no")
    FSSAI_no = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="FSSAI no")
    Warehouse_CST = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Warehouse CST")
    GSTIN = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="GSTIN")
    Warehouse_LBT_no = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Warehouse LBT no")
    Jurisdiction = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Jurisdiction")
    Country_WMS = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Country_WMS")
    Tenant_WMS = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Tenant_WMS")
    Category_WMS = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Category_WMS")
    Address_type_WMS = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Address_type_WMS")
    Address_line2_WMS = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Address_line2_WMS")
    Status_WMS = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Status_WMS")
    Zone_code_WMS = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Zone_code_WMS")
    Lat_WMS = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Lat_WMS")
    Long_WMS = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={ "class": "form-control"}), label="Long_WMS")


    class Meta:
        model = Record
        exclude = ("user",)



