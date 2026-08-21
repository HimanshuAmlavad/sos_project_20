from django.shortcuts import render

from service.service.BankAccountService import BankAccountService

from .BaseCtl import BaseCtl

class BankAccountListCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['account_number'] = requestForm.get('accountNumber',"")


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
        return BankAccountService()

    def get_template(self):
        return 'ors/bankaccountlist.html'