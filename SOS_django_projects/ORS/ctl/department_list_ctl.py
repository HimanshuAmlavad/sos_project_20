from django.shortcuts import render

from service.service.DepartmentService import DepartmentService
from .BaseCtl import BaseCtl


class DepartmentListCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['department_code'] = requestForm.get('departmentCode')
        self.form['department_name'] = requestForm.get('departmentName')
        self.form['page_number'] = int(requestForm.get('page_number', 1) or 1)

    def display(self, request, params={}):
        self.form['page_number'] = 1
        page_list = self.get_service().search(self.form, page_number=1)
        return render(
            request,
            self.get_template(),
            {'pageList': page_list, 'form': self.form}
        )

    def submit(self, request, params={}):
        page_number = int(self.form.get('page_number', 1))

        if request.POST.get('operation') == 'next':
            page_number += 1
        if request.POST.get('operation') == 'previous':
            page_number = max(1, page_number - 1)
        if request.POST.get('operation') == 'search':
            page_number = 1

        self.form['page_number'] = page_number
        page_list = self.get_service().search(self.form, page_number=page_number)
        self.form['list'] = page_list
        return render(request, self.get_template(), {'pageList': page_list, 'form': self.form})

    def get_service(self):
        return DepartmentService()

    def get_template(self):
        return 'ors/departmentlist.html'