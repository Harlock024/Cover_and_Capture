import graphene
import graphql_jwt

import albumCovers.schema
import users.schema

class Query(users.schema.Query,albumCovers.schema.Query, graphene.ObjectType):
    pass

class Mutation(users.schema.Mutation, albumCovers.schema.mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
