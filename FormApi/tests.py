# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.test import TestCase
import FormApi.Constant
from django.test.client import RequestFactory
import requests


class FormApiCases(TestCase):	
	def setUp(self):
		ISTESTMODE = True
		self.factory = RequestFactory()
	def test_FillData(self):
		input = json.dumps({Constant.Username:"abhishek",
					Constant.Email:"abhishektiwari981996@gmail.com",
					Constant.Phone:"9998705087"})
		response = self.client.post("/FillData/",input,Constant.content_type)
		print(response)
		self.assertEqual(response.status_code,200)