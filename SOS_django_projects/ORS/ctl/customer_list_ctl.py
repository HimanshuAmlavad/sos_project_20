from django.shortcuts import render
from service.service.CustomerService import CustomerService
from .BaseCtl import BaseCtl

class CustomerListCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['customer_id'] = requestForm.get('customerId',"")
        # self.form['page_no'] = int(requestForm.get('page_no', 1) or 1)
        # self.form['page_size'] = int(requestForm.get('page_size', 5) or 5)


    def display(self, request, params={}):
        self.form["page_no"] = 1
        page_list = self.get_service().search(self.form)
        return render(request, self.get_template(), {'pageList':page_list, 'form': self.form})

    def submit(self, request, params={}):
        operation = request.POST.get('operation', '')
        page_no = int(self.form.get('page_no', 1))

        if operation == 'next':
            page_no += 1
        if operation == 'previous':
            page_no = max(1, page_no - 1)
        if operation == 'search':
            page_no = 1

        self.form['page_no'] = page_no
        page_list = self.get_service().search(self.form)
        return render(request, self.get_template(), {'pageList': page_list, 'form': self.form})

    def get_service(self):
        return CustomerService()

    def get_template(self):
        return 'ors/customerlist.html'