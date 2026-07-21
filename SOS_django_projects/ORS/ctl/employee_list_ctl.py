from pydoc import pager

from django.shortcuts import render, redirect
from service.service.EmployeeService import EmployeeService
from .BaseCtl import BaseCtl

class EmployeeListCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['employee_id'] = requestForm.get('employeeId')
        self.form['page_number'] = int(requestForm.get('page_number', 1) or 1)


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
            self.form['page_number'] = int(request.POST['pageNumber'])
            self.form['page_number'] -= 1
        if request.POST.get('operation', '') == "search":
            self.form['page_number'] = 1

        drone_list = self.get_service().search(self.form)
        self.form['list'] = drone_list
        return render(request, self.get_template(), {'form': self.form})

    def get_service(self):
        return EmployeeService()

    def get_template(self):
        return 'ors/employeelist.html'