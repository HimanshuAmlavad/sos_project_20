from django.shortcuts import render, redirect

from service.service.DroneService import DroneService
from .BaseCtl import BaseCtl



class DroneListCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['drone_id'] = requestForm.get('droneId')
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
        return render(request, self.get_template(), {'pageList':page_list,'form': self.form})

    def get_service(self):
        return DroneService()

    def get_template(self):
        return 'ors/dronelist.html'