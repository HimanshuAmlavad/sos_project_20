from django.shortcuts import render

from ORS.ctl.BaseCtl import BaseCtl
from ORS.utility.HtmlUtility import HtmlUtility
from service.models import Book
from service.service.BookService import BookService
from service.utility.DataValidator import DataValidator

class BookCtl(BaseCtl):

    def preload(self, request):
        status_list = ["Available",
                       "Issued",
                       "Reserved",
                       "Damaged",
                       "Lost"]
        # print("Preload status:", repr(self.form.get("status")))
        self.preload_data["status_select"] = HtmlUtility.get_list_from_list(
            "status",
            self.form.get("status"),
            status_list,
        )
        # Also make preload available under form for templates using `form.preload_data`
        self.form["preload_data"] = self.preload_data
        return self.preload_data

    # Populate Form from HTTP Request
    def request_to_form(self, request):
        self.form["id"] = request.get("id", 0)
        # print('R2F =====================>', self.form["id"])
        self.form["book_id"] = request.get("bookId", 0)
        self.form["book_code"] = request.get("bookCode", "")
        self.form["book_title"] = request.get("bookTitle", "")
        print('R2F =====================>', self.form["book_title"])
        self.form["category"] = request.get("category", "")
        self.form["status"] = request.get("status", "")

    # Populate Form from Model
    def model_to_form(self, obj):
        if obj == None:
            return
        self.form["id"] = obj.id
        # print('M2F======================>', self.form["id"])
        self.form["book_id"] = obj.book_id
        self.form["book_code"] = obj.book_code
        self.form["book_title"] = obj.book_title
        print('M2F======================>', self.form["book_title"])
        self.form["category"] = obj.category
        self.form["status"] = obj.status
        # print('M2F======================>', self.form["status"])

    # Convert form into module
    def form_to_model(self, obj):
        pk = int(self.form.get("id", 0))
        if pk > 0:
            obj.id = pk
        print('F2M======================>', obj.id)
        obj.book_id = int(self.form.get("book_id", 0))
        obj.book_code = self.form.get("book_code", "")
        obj.book_title = self.form.get("book_title", "")
        print('F2M======================>', obj.book_title)
        obj.category = self.form.get("category", "")
        obj.status = self.form.get("status", "")
        return obj

    # Validate form
    def input_validation(self):
        super().input_validation()
        inputError = self.form["inputError"]
        if DataValidator.isNull(self.form["book_id"]):
            inputError["book_id"] = "Book Id is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["book_code"]):
            inputError["book_code"] = "Book Code is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["book_title"]):
            inputError["book_title"] = "Book Title is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["category"]):
            inputError["category"] = "Category is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["status"]):
            inputError["status"] = "Status is required"
            self.form["error"] = True
        return self.form["error"]

    # Display Book page
    def display(self, request, params={}):
        if params["id"] > 0:
            book = self.get_service().get(params["id"])
            self.model_to_form(book)
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Submit Book page
    def submit(self, request, _params={}):
        book = self.form_to_model(Book())
        self.get_service().save(book)
        if int(self.form["id"]) > 0:
            self.form["id"] = book.id
        self.form["error"] = False
        self.form["message"] = "Data is saved"
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Template html of Book page
    def get_template(self):
        return "ors/book.html"

    # Service of Book
    def get_service(self):
        return BookService()
