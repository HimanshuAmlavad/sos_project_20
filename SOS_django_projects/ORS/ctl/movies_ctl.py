from django.shortcuts import render

from ORS.ctl.BaseCtl import BaseCtl
from ORS.utility.HtmlUtility import HtmlUtility
from service.models import Movie
from service.service.MovieService import MovieService
from service.utility.DataValidator import DataValidator

class MovieCtl(BaseCtl):

    def preload(self, request):
        status_list = ["Released",
                       "Upcoming",
                       "Now Showing",
                       "Archived",
                       "Cancelled"]
        # print("Preload status:", repr(self.form.get("status")))
        self.preload_data["status_select"] = HtmlUtility.get_list_from_list(
            "status",
            self.form.get("status"),
            status_list,
        )
        # Also make preload available under form for templates using `form.preload_data`
        self.form["preload_data"] = self.preload_data
        return self.preload_data

    # Populate Form from HTTP Request
    def request_to_form(self, request):
        self.form["id"] = int(request.get("id", 0) or 0)
        # print('R2F =====================>', self.form["id"])
        self.form["movie_id"] = request.get("movieId", 0)
        self.form["movie_code"] = request.get("movieCode", "")
        self.form["movie_name"] = request.get("movieName", "")
        # print('R2F =====================>', self.form["movie_name"])
        self.form["director_name"] = request.get("directorName", "")
        self.form["genre"] = request.get("genre", "")
        self.form["status"] = request.get("status", "")

    # Populate Form from Model
    def model_to_form(self, obj):
        if obj == None:
            return
        self.form["id"] = obj.id
        # print('M2F======================>', self.form["id"])
        self.form["movie_id"] = obj.movie_id
        self.form["movie_code"] = obj.movie_code
        self.form["movie_name"] = obj.movie_Name
        print('M2F======================>', self.form["movie_name"])
        self.form["director_name"] = obj.director_name
        self.form["genre"] = obj.genre
        self.form["status"] = obj.status
        # print('M2F======================>', self.form["status"])

    # Convert form into module
    def form_to_model(self, obj):
        pk = int(self.form.get("id", 0))
        if pk > 0:
            obj.id = pk
        print('F2M======================>', obj.id)
        obj.movie_id = int(self.form.get("movie_id", 0))
        obj.movie_code = self.form.get("movie_code", "")
        obj.movie_Name = self.form.get("movie_name", "")
        print('F2M======================>', obj.movie_Name)
        obj.director_name = self.form.get("director_name", "")
        obj.genre = self.form.get("genre", "")
        obj.status = self.form.get("status", "")
        return obj

    # Validate form
    def input_validation(self):
        super().input_validation()
        inputError = self.form["inputError"]
        if DataValidator.isNull(self.form["movie_id"]):
            inputError["movie_id"] = "Movie Id is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["movie_code"]):
            inputError["movie_code"] = "Movie Code is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["movie_name"]):
            inputError["movie_name"] = "Movie Name is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["director_name"]):
            inputError["director_name"] = "Director Name is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["genre"]):
            inputError["genre"] = "Genre is required"
            self.form["error"] = True
        if DataValidator.isNull(self.form["status"]):
            inputError["status"] = "Status is required"
            self.form["error"] = True
        return self.form["error"]

    # Display Role page
    def display(self, request, params={}):
        if params["id"] > 0:
            movie = self.get_service().get(params["id"])
            self.model_to_form(movie)
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Submit Role page
    def submit(self, request, _params={}):
        movie = self.form_to_model(Movie())
        self.get_service().save(movie)
        if int(self.form["id"]) > 0:
            self.form["id"] = movie.id
        self.form["error"] = False
        self.form["message"] = "Data is saved"
        return render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )

    # Template html of Role page
    def get_template(self):
        return "ors/movie.html"

    # Service of Role
    def get_service(self):
        return MovieService()
