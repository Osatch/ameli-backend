from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ExtractionSerializer
from . import ameli
import os

def accueil(request):
    return HttpResponse(
        "<h1>Bienvenue sur l'API Ameli 🩺</h1>"
        "<p>Utilisez <code>/api/launch/</code> (POST) pour lancer l'extraction.</p>"
        "<p>Envoyez les champs : <code>profession</code> (string), "
        "<code>departements</code> (liste ex: [\"13\", \"75\"]), "
        "<code>option</code> (1 ou 2).</p>"
    )

@api_view(['POST'])
def lancer_script(request):
    serializer = ExtractionSerializer(data=request.data)

    if serializer.is_valid():
        profession = serializer.validated_data['profession']
        departements = serializer.validated_data['departements']
        option = serializer.validated_data['option']

        try:
            chemin_fichier = ameli.lancer_extraction(profession, departements, option)
            nom_fichier = os.path.basename(chemin_fichier)
            url_fichier = request.build_absolute_uri('/media/' + nom_fichier)

            return Response({
                "status": "success",
                "message": "Extraction terminée avec succès.",
                "url": url_fichier
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "status": "error",
                "message": f"Une erreur est survenue : {str(e)}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
