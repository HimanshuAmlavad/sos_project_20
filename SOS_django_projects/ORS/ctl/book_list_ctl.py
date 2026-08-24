from django.shortcuts import render

from service.service.BookService import BookService
from .BaseCtl import BaseCtl



class BookListCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['book_title'] = requestForm.get('bookTitle',"")
        self.form['page_number'] = int(requestForm.get('page_number', 1) or 1)
        self.form['page_size'] = int(requestForm.get('page_size', 5) or 5)


    def display(self, request, params={}):
        self.form["page_number"] = 1
        page_list = self.get_service().search(self.form, page_number=1)
        return render(request, self.get_template(), {'pageList':page_list, 'form': self.form})

    def submit(self, request, params={}):
        operation = request.POST.get("operation","")
        page_number = int(request.POST.get('page_number',1))

        if operation == "next":
            # print('Next ========>',self.form['page_number'])
            page_number += 1
        if request.POST.get('operation', '') == "previous":
            self.form['page_number'] -= 1
        if request.POST.get('operation', '') == "search":
            self.form['page_number'] = 1

        page_list = self.get_service().search(self.form,  page_number=page_number)
        return render(request, self.get_template(), {'pageList': page_list, 'form': self.form})

    def get_service(self):
        return BookService()

    def get_template(self):
        return 'ors/booklist.html'