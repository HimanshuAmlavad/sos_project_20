import logging
from abc import ABC, abstractmethod
from service.utility.DataValidator import DataValidator
from django.core.paginator import Paginator
from django.db import models as db_models

logger = logging.getLogger(__name__)


class DuplicateValueError(Exception):
    pass


class BaseDAO(ABC):

    def get(self, pk):
        try:
            return self.get_model().objects.get(id=pk)
        except self.get_model().DoesNotExist:
            logger.warning("%s.get() pk=%s not found", self.__class__.__name__, pk)
            return None
            # return


    def get_all(self):
        return self.get_model().objects.all()

    def _check_unique_keys(self, obj):
        unique_keys = self.get_Unique()
        errors = []
        if not unique_keys:
            return
        for key in unique_keys:
            value = getattr(obj, key)
            qs = self.get_model().objects.filter(**{key: value})
            if obj.id:
                qs = qs.exclude(id=obj.id)
            if qs.exists():
                errors.append(f"{key}='{value}' already exists")
        if errors:
            raise DuplicateValueError("; ".join(errors))

    def save(self, obj):
        is_new = obj.id == 0
        if is_new:
            obj.id = None
        self._check_unique_keys(obj)
        obj = self.populate(obj)
        obj.save()
        logger.info(
            "%s.save() %s pk=%s",
            self.__class__.__name__,
            "inserted" if is_new else "updated",
            obj.id,
        )

    def delete(self, pk):
        obj = self.get(pk)
        if obj:
            obj.delete()
            logger.info("%s.delete() pk=%s deleted", self.__class__.__name__, pk)

    def find_by_unique_key(self, pk):
        return self.get(pk)


    def search(self, params):
        page_no = int(params.get("page_no", 1))
        page_size = int(params.get('page_size', 0))

        query = self.get_model().objects.all()

        if (page_size == 0):
            return query

        query = self.get_where_conditions(query, params)

        paginator = Paginator(query, page_size)

        page_obj = paginator.get_page(page_no)

        params["has_next"] = page_obj.has_next()
        params["has_previous"] = page_obj.has_previous()
        params["index"] = (page_no - 1) * page_size

        return page_obj

    @abstractmethod
    def get_model(self):
        pass

    @abstractmethod
    def get_Unique(self):
        return None

    @abstractmethod
    def populate(self, obj):
        return None

    @abstractmethod
    def get_where_conditions(self, query, params):
        pass