from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform

# https://github.com/encode/django-rest-framework/blob/master/rest_framework/serializers.py
class WatchListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WatchList
        fields = "__all__"
    
    
# HyperlinkedModelSerializer = https://www.django-rest-framework.org/api-guide/serializers/#hyperlinkedmodelserializer    
class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
# class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    #watchlist = serializers.StringRelatedField(many=True)
    
    # https://www.django-rest-framework.org/api-guide/relations/#hyperlinkedrelatedfield
    # watch-detail = urls.py path('<int:pk>', WatchDetailAV.as_view(), name='watch-detail'),
    # watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="watch-detail")

    class Meta:
        model = StreamPlatform
        fields = "__all__"


# # https://www.django-rest-framework.org/api-guide/serializers/#validators
# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short!")

# # https://www.django-rest-framework.org/tutorial/1-serialization/#creating-a-serializer-class
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title and Description should be different!")
#         else:
#             return data

#     # def validate_name(self, value):
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError("Name is too short!")
#     #     else:
#     #         return value