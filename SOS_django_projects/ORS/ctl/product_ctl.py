from django.shortcuts import render

from ORS.ctl.BaseCtl import BaseCtl
from ORS.utility.HtmlUtility import HtmlUtility
from service.models import  Product
from service.service.ProductService import ProductService
from service.utility.DataValidator import DataValidator


class ProductCtl(BaseCtl):

    def preload(self, request):
        category_list = [
            "Electronics",
            "Clothing",
            "Food",
            "Furniture",
            "Books",
            "Sports",
            "Beauty",
            "Grocery",
            "Automobile",
            "Stationery"
        ]
        # print("Preload category:", repr(self.form.get("category")))
        self.preload_data["category_select"] = HtmlUtility.get_list_from_list(
            "category",
            self.form.get("category"),
            category_list,
        )
        # Also make preload available under form for templates using `form.preload_data`
        self.form["preload_data"] = self.preload_data
        return self.preload_data

    # Populate Form from HTTP Request
    def request_to_form(self, request):
        self.form["id"] = int(request.get("id", 0) or 0)
        print('R2F =====================>', self.form["id"])
        self.form["product_id"] = request.get("productId", 0)
        self.form["price"] = request.get("price", "")
        self.form["product_name"] = request.get("productName", "")
        self.form["quantity"] = request.get("quantity", "")
        print("Manager Name =================>", repr(self.form["quantity"]))
        self.form["category"] = request.get("category", "")

    # Populate Form from Model
    def model_to_form(self, obj):
        if obj == None:
            return
        self.form["id"] = obj.id
        # print('M2F======================>', self.form["id"])
        self.form["product_id"] = obj.product_id
        self.form["price"] = obj.price
        self.form["product_name"] = obj.product_name
        self.form["quantity"] = obj.quantity
        self.form["category"] = obj.category
        print('M2F======================>', self.form["category"])


    # Convert form into module
    def form_to_model(self, obj):
        pk = int(self.form.get("id", 0))
        if pk > 0:
            obj.id = pk
        print('F2M======================>', obj.id)
        obj.product_id = int(self.form.get("product_id", 0))
        obj.price = self.form.get("price", "")
        obj.product_name = self.form.get("product_name", "")
        obj.quantity = self.form.get("quantity", "")
        obj.category = self.form.get("category", "")
        return obj

    # Validate form
    def input_validation(self):
        super().input_validation()
        inputError = self.form["inputError"]
        if DataValidator.isNull(self.form["product_id"]):
            inputError["product_id"] = "Product Id is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["price"]):
            inputError["price"] = "Price is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["product_name"]):
            inputError["product_name"] = "Product Name is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["quantity"]):
            inputError["quantity"] = "quantity is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["category"]):
            inputError["category"] = "Category is required"
            self.form["error"] = True
        return self.form["error"]

    # Display Role page
    def display(self, request, params={}):
        if params["id"] > 0:
            product = self.get_service().get(params["id"])
            self.model_to_form(product)
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Submit Role page
    def submit(self, request, _params={}):
        product = self.form_to_model(Product())
        self    .get_service().save(product)
        if int(self.form["id"]) > 0:
            self.form["id"] = product.id
        self.form["error"] = False
        self.form["message"] = "Data is saved"
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Template html of Role page
    def get_template(self):
        return "ors/product.html"

    # Service of Role
    def get_service(self):
        return ProductService()
