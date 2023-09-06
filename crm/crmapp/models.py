
from django.db import models


# Create your models here.


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    erp_Id = models.CharField(max_length=50)
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    District = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Pin = models.PositiveBigIntegerField(max_length=20)
    Phone = models.PositiveBigIntegerField()
    Vdiscountpercent = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Popsstrata = models.CharField(max_length=100)
    Businesstype = models.CharField(max_length=100)
    Warehouse_Type = models.CharField(max_length=100)
    Warehouse_Category = models.CharField(max_length=100)
    Prefix_To_Billno = models.CharField(max_length=100)
    Suffix_To_Billno = models.CharField(max_length=100)
    Prefix_To_Creditno = models.CharField(max_length=100)
    Suffix_To_Creditno = models.CharField(max_length=100)
    Prefix_To_Debitno = models.CharField(max_length=100)
    Suffix_To_Debitno = models.CharField(max_length=100)
    Prefix_To_Salereturnno = models.CharField(max_length=100)
    Suffix_To_Salereturnno = models.CharField(max_length=100)
    Prefix_Challan_Number = models.CharField(max_length=100)
    Suffix_Challan_Number = models.CharField(max_length=100)
    Warehouse_Label = models.CharField(max_length=100)
    Default_Credit_Limit = models.CharField(max_length=100)
    Default_Credit_Period = models.CharField(max_length=100)
    Default_Minimum_Order_Value = models.CharField(max_length=100)
    Subzone = models.CharField(max_length=100)
    Parent_Warehouse = models.CharField(max_length=100)
    Currency = models.CharField(max_length=100)
    QR_Code_Image = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    Warehouse_TIN = models.CharField(max_length=100)
    PAN_no = models.CharField(max_length=100)
    FSSAI_no = models.CharField(max_length=100)
    Warehouse_CST = models.CharField(max_length=100)
    GSTIN = models.CharField(max_length=100)
    Warehouse_LBT_no = models.CharField(max_length=100)
    Jurisdiction = models.CharField(max_length=100)
    Country_WMS= models.CharField(max_length=100)
    Tenant_WMS = models.CharField(max_length=100)
    Category_WMS= models.CharField(max_length=100)
    Address_type_WMS= models.CharField(max_length=100)
    Address_line2_WMS = models.CharField(max_length=100)
    Status_WMS= models.CharField(max_length=100)
    Zone_code_WMS= models.CharField(max_length=100)
    Lat_WMS = models.CharField(max_length=100)
    Long_WMS= models.CharField(max_length=100)
    
    
    



   

    def __str__(self):
        return f"{self.Name} ({self.erp_Id})"

    
    


