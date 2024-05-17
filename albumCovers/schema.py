import graphene 
from graphene_django import DjangoObjectType
from albumCovers.models import AlbumCover, Vote
from users.schema import UserType
from graphql import GraphQLError
from .spotify_utils import obtener_portada_album


class AlbumCoverType(DjangoObjectType):
    class Meta:
        model = AlbumCover

class VoteType(DjangoObjectType):
    class Meta:
        model = Vote

class Query(graphene.ObjectType):
    album_covers = graphene.List(AlbumCoverType)
    votes = graphene.List(VoteType)
    
    def resolve_album_covers(self, info, **kwargs):
        return AlbumCover.objects.all()
    
    def resolve_votes(self, info, **kwargs):
        return Vote.objects.all()
    
class CreateAlbumCover(graphene.Mutation):
    id = graphene.Int()
    Artist = graphene.String()
    albumName = graphene.String()
    cover_url = graphene.String()
    posted_by = graphene.Field(UserType)

    class Arguments:
        albumName = graphene.String()
        Artist = graphene.String()

    def mutate(self, info, albumName, Artist):
        user = info.context.user or None

        cover_url=obtener_portada_album(Artist,albumName)
        if not cover_url:
            raise GraphQLError('No se pudo encontrar la portada del álbum')

        album_cover = AlbumCover(
            Artist=Artist,
            albumName=albumName,
            cover_url=cover_url,
            posted_by=user)
        album_cover.save()

        return CreateAlbumCover(
            id=album_cover.id,
            albumName=album_cover.albumName,
            Artist=album_cover.Artist,
            cover_url=cover_url,
            posted_by=user)
    

class CreateVote(graphene.Mutation):
    user = graphene.Field(UserType)
    album_cover = graphene.Field(AlbumCoverType)

    class Arguments:
        AlbumCover_id = graphene.Int()

    def mutate(self, info, AlbumCover_id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('You must be logged  to vote!')
        
        album_cover = AlbumCover.objects.filter(id=AlbumCover_id).first()
        if not album_cover:
            raise Exception('That album cover does not exist!')

        Vote.objects.create(
            user=user,
            album_cover=album_cover,
            )
    
        return CreateVote( user=user,album_cover=album_cover)
class Mutation(graphene.ObjectType):
    create_album_cover = CreateAlbumCover.Field()
    create_vote = CreateVote.Field()
