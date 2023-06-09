from rest_framework import serializers

from .models import HomeAppliances, HomeAppliancesModel, Edibles, EdiblesModel, Clothes, ClothesModel

class HomeAppliancesDetail(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = HomeAppliancesModel
        fields = ('model', 'count', 'Description', 'url')

class HomeAppliancesSerializer(serializers.ModelSerializer):
    model_type = serializers.SerializerMethodField()
    homeAppliances = HomeAppliancesDetail(many=True)

    class Meta:
        model = HomeAppliances
        fields = ('model_type', 'home_appliance_type', 'is_available', 'homeAppliances')

    def get_model_type(self, obj):
        return obj.get_model_type_display()

class HomeAppliancesDetailSerializer(serializers.ModelSerializer):

    homeApplianceImage = serializers.ImageField()

    class Meta:
        model = HomeAppliancesModel
        fields = ('model', 'count', 'price', 'discount', 'homeApplianceImage', 'Description')

class HomeAppliancesPostSerializer(serializers.ModelSerializer):

    model_type = serializers.SerializerMethodField()
    homeAppliances = HomeAppliancesDetailSerializer(many=True)

    class Meta:
        model = HomeAppliances
        fields = ('model_type', 'home_appliance_type', 'is_available', 'homeAppliances')

    def get_model_type(self, obj):
        return obj.get_model_type_display()

class EdiblesListDetail(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = EdiblesModel
        fields = ('mark', 'taste', 'Description', 'url')

class EdiblesSerializer(serializers.ModelSerializer):
    model_type = serializers.SerializerMethodField()
    edible = EdiblesListDetail(many=True)

    class Meta:
        model = Edibles
        fields = ('model_type', 'edible_type', 'is_available', 'edible')

    def get_model_type(self, obj):
        return obj.get_model_type_display()

class EdiblesDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = EdiblesModel
        fields = ('mark', 'taste', 'price', 'discount', 'edibleImage', 'Description')

class EdiblesDetailSerializerForPost(serializers.ModelSerializer):

    class Meta:
        model = EdiblesModel
        fields = ('mark', 'taste', 'price', 'discount', 'edibleImage', 'Description')

class EdiblesPostSerializer(serializers.ModelSerializer):

    edible = EdiblesDetailSerializerForPost(many=True)
    model_type = serializers.SerializerMethodField()

    class Meta:
        model = Edibles
        fields = ('model_type', 'edible_type', 'is_available', 'edible')

    def get_model_type(self, obj):
        return obj.get_model_type_display()

class ClothesListDetail(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ClothesModel
        fields = ('size', 'color', 'count', 'Description', 'url')

class ClothesSerializer(serializers.ModelSerializer):
    model_type = serializers.SerializerMethodField()
    clothe = ClothesListDetail(many=True)

    class Meta:
        model = Clothes
        fields = ('model_type', 'clothe_type', 'is_available', 'clothe')

    def get_model_type(self, obj):
        return obj.get_model_type_display()

class ClothesDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClothesModel
        fields = ('size', 'color', 'count', 'price', 'discount', 'category_image', 'Description')

class ClothesDetailSerializerPosts(serializers.ModelSerializer):

    class Meta:
        model = ClothesModel
        fields = ('size', 'color', 'count', 'price', 'discount', 'Description')


class ClotheDetailSerializerForPost(serializers.ModelSerializer):

    model_type = serializers.SerializerMethodField()
    clothe = ClothesDetailSerializerPosts(many=True)

    class Meta:
        model = Clothes
        fields = ('model_type', 'clothe_type', 'is_available', 'clothe')

    def get_model_type(self, obj):
        return obj.get_model_type_display()