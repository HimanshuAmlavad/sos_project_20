from ORSAPI.rest.BaseRestCtl import BaseRestCtl
from service.Serializers import LibrarySerializers
from service.models import Library
from service.service.LibraryService import LibraryService
from service.utility.DataValidator import DataValidator


class LibraryRestCtl(BaseRestCtl):
    def get_model(self):
        return Library

    def get_service(self):
        return LibraryService()

    def get_serializer_class(self):
        return LibrarySerializers

    def input_validation(self, data):
        errors = {}

        library_id = data.get("libraryId", "")
        library_name = data.get("libraryName", "")
        address = data.get("address", "")
        total_books = data.get("totalBooks", 0)
        contact_no = data.get("contactNo", "")

        if DataValidator.isNull(library_id):
            errors["libraryId"] = "Library Id cannot be null"
        elif not DataValidator.isMaxLength(library_id, 50):
            errors["libraryId"] = "Name cannot exceed 50 characters"

        if DataValidator.isNull(library_name):
            errors["libraryName"] = "Library Name cannot be null"
        elif not DataValidator.isMaxLength(library_name, 100):
            errors["libraryName"] = "Library Name cannot exceed 100 characters"

        if DataValidator.isNull(address):
            errors["address"] = "address cannot be null"
        elif not DataValidator.isMaxLength(address, 250):
            errors["address"] = "address cannot exceed 250 characters"

        if DataValidator.isNull(total_books):
            errors["totalBooks"] = "Total Books cannot be null"
        elif not DataValidator.isInteger(total_books):
            errors["totalBooks"] = "Enter only Integers"

        if DataValidator.isNull(contact_no):
            errors["contactNo"] = "Contact No. cannot be null"
        elif not DataValidator.isMaxLength(contact_no, 10):
            errors["contactNo"] = "Contact No. cannot exceed 10 characters"

        return errors
