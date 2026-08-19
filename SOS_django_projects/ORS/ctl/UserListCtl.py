from django.shortcuts import render
from .BaseCtl import BaseCtl
from service.service.UserService import UserService
from service.service.RoleService import RoleService
from ORS.utility.HtmlUtility import HtmlUtility


class UserListCtl(BaseCtl):

    def preload(self, request):
        role_list = RoleService().search({})
        gender_list = ["Male", "Female"]
        self.preload_data["role_select"] = HtmlUtility.get_list_from_beans(
            "role_id",
            int(self.form.get("role_id") or 0),
            role_list,
        )
        self.preload_data["gender_select"] = HtmlUtility.get_list_from_list(
            "gender", self.form.get("gender"), gender_list
        )
        return self.preload_data

    def request_to_form(self, requestForm):
        self.form["firstName"] = requestForm.get("firstName", "")
        self.form["lastName"] = requestForm.get("lastName", "")
        self.form["login"] = requestForm.get("login", "")
        self.form["mobileNumber"] = requestForm.get("mobileNumber", "")
        self.form["gender"] = requestForm.get("gender", "")
        self.form["role_id"] = requestForm.get("role_id", "")
        self.form["page_number"] = int(requestForm.get("page_number", 1))
        self.form["page_size"] = int(requestForm.get("page_size", 5) or 5)

    def display(self, request, params={}):
        self.page_list = self.get_service().search(self.form, page_number=1)
        res = render(
            request,
            self.get_template(),
            {"pageList": self.page_list, "form": self.form, "preload_data": self.preload(request)},
        )
        return res

    def submit(self, request, params={}):
        self.request_to_form(request.POST)
        page_number = self.form.get("page_number", 1)
        self.page_list = self.get_service().search(self.form, page_number=page_number)
        res = render(
            request,
            self.get_template(),
            {
                "pageList": self.page_list,
                "form": self.form,
                "preload_data": self.preload(request),
            },
        )
        return res

    def get_template(self):
        return "ors/UserList.html"

    def get_service(self):
        return UserService()
