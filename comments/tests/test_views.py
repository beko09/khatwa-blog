from django.test import TestCase ,Client
from django.urls import resolve,reverse
from posts.models import Category, Post
from comments.models import Comment
from django.contrib.auth.models import User
from time import timezone
import json
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.post_list_url = reverse('posts:post_list')
        self.post_detail_url = reverse('posts:post_detail', args=['test'])
        self.user = User.objects.create(
            username='beko09',
            email='b@gmail.com',
            password= 'test',
            )
        self.number_of_post = 10
        self.test = Post.objects.create(
            user= self.user,
            title='test',
            description='test',
            content='some test',
            publish = '2020-2-2',
        )
        for post_id in range(self.number_of_post):
            Post.objects.create(
                user= self.user,
                title= f'test - {post_id}',
                description= f'test - {post_id}',
                content= f'some test -{post_id}',
                publish = '2020-2-2',
            )

    def test_post_list_GET(self):
        response = self.client.get(self.post_list_url)
        self.assertEquals(response.status_code, 200)
        # self.assertTrue('is_paginated' in response.context)  +'?page=2'
        # self.assertTrue(response.context['is_paginated'] == True)
        # self.assertTrue(len(response.context['posts']) == 3)
        self.assertTemplateUsed(response, 'post/post_list.html')


    # def test_pagination_post_list_is_ten(self):
    #     response = self.client.get(self.post_list_url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue('is_paginated' in response.context)
    #     self.assertTrue(response.context['is_paginated'] == True)
    #     self.assertTrue(len(response.context['posts']) == 10)

    def test_post_detail_GET(self):
        response = self.client.get(self.post_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'post/post_detail.html')

    def test_post_detail_add_comment(self):
        Comment.objects.create(
            user=self.user,
            content="hello",
            content_type_id = self.test.id
        )
        response = self.client.post(self.post_detail_url, {
            'content':'hello'
        })

        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.Comment.expenses.first().content, 'hello')
    