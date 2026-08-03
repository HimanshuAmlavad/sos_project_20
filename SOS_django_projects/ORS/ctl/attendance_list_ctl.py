from django.shortcuts import render

from service.service.AttendanceService import AttendanceService
from .BaseCtl import BaseCtl

class AttendanceListCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['student_name'] = requestForm.get('studentName')
        self.form['page_number'] = int(requestForm.get('page_number', 1) or 1)


    def display(self, request, params={}):
        self.form["page_number"] = 1
        page_list = self.get_service().search(self.form, page_number=1)
        return render(request, self.get_template(), {'pageList':page_list, 'form': self.form})

    def submit(self, request, params={}):
        operation = request.POST.get('operation', '')
        page_number = int(self.form.get('page_number', 1))

        if operation == 'next':
            page_number += 1
        if operation == 'previous':
            page_number = max(1, page_number - 1)
        if operation == 'search':
            page_number = 1

        self.form['page_number'] = page_number
        page_list = self.get_service().search(self.form, page_number=page_number)
        return render(request, self.get_template(), {'pageList': page_list, 'form': self.form})

    def get_service(self):
        return AttendanceService()

    def get_template(self):
        return 'ors/attendancelist.html'