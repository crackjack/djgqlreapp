from graphene_django import DjangoObjectType
import graphene
from .models import College

class CollegeSchema(DjangoObjectType):
	class Meta:
		model = College

class Query(graphene.AbstractType):
	colleges = graphene.List(CollegeSchema)

	@graphene.resolve_only_args
	def resolve_colleges(self):
		return College.objects.all()

