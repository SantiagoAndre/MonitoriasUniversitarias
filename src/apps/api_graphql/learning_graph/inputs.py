from graphene import ID
from graphene import Int
from graphene import String
from graphene import Boolean
from graphene import DateTime
from graphene import InputObjectType

class CreateLearningLineInput(InputObjectType):
    name = String(required=True)
    description = String(required=True)
class UpdateLearningLineInput(InputObjectType):
    id = ID(required=True)
    name = String(required=False)
    description = String(required=False)



class CreateSubjectInput(InputObjectType):
    name = String(required=True)
    description = String(required=True)
class UpdateSubjectInput(InputObjectType):
    id = ID(required=True)
    name = String(required=False)
    description = String(required=False)