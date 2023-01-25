# from django.db import IntegrityError
# from django.test import TestCase
# from django.urls import reverse
# from rest_framework.test import APITestCase
# from django .utils import timezone
# from cards.models import BankCard
# import  json
#
#
#
# class BankCardApiTestCase(APITestCase):
#     def test_get(self, fake=None) -> None:
#       self._base_api_url = '/api/v1'
#       self._news = BankCard.objects.create(
#           cardHolder='Iluxa',
#           expirationDate='2003-10-21',
#           balance=6.34,
#           lastFourDigigts=6523,
#
#       )
#     def test_list_only_active (self) -> None:
#         BankCard.objects.create(
#             cardHolder='Iluxa',
#             expirationDate='2003-10-21',
#             balance=6.34,
#             lastFourDigigts=6523,
#
#         )
#
#         response = self.client.get(self._api_url + 'BankCard/')
#         assert response.status_code == 200
#         assert len(json.loads(response.content)) == 1
#         assert json.loads(response.content)[0]['BankCard_cardHolder'] == 'Заголовок новости'
#
#     def test_unique_BankCard(self) -> None:
#         with self.assertRaises(IntegrityError):
#             BankCard.objects.create(
#                 cardHolder='Iluxa',
#                 expirationDate='2003-10-21',
#                 balance=6.34,
#                 lastFourDigigts=6523,
#
#             )
#
#     def test_method_str(self) -> None:
#         assert getattr(BankCard, '__str__', None) is not None
#
