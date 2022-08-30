# from django.shortcuts import render
# from watchlist_app.models import Movie
# from django.http import JsonResponse,HttpResponse
# import json

# def movie_list(request):
#     movies = Movie.objects.all()
#     print ("Movie =====  :  ",list(movies.values()))
#     data = {
#         'movies': list(movies.values())
#     }
#     # return JsonResponse(data)
#     return HttpResponse(json.dumps(data))


# def movie_details(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     data = {
#         'name': movie.name,
#         'description': movie.description,
#         'active': movie.active
#     }
#     return JsonResponse(data)
