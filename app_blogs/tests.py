from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from app_blogs.models import Blog, Comment, Like


# class BlogModelTests(TestCase):
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(
#             username="testuser", email="test@mail.com", password="testpass"
#         )
#         self.blog = Blog.objects.create(
#             title = "Test Blog",
#             author = self.user,
#             content = "This is a test blog"
#         )
        
#     def test_blog_creation(self):
#         self.assertEqual(str(self.blog), "Test Blog..............")
#         self.assertEqual(self.blog.total_likes(), 0)
#         self.assertEqual(self.blog.total_comments(), 0)
    
#     def test_blog_get_absolute_url(self):
#         self.assertEqual(self.blog.get_absolute_url(), reverse("blog_detail", args=[str(self.blog.id)]))


# class CommentModelTests(TestCase):
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(
#             username="testuser", email="test@mail.com", password="testpass"
#         )
#         self.blog = Blog.objects.create(
#             title = "Test Blog",
#             author = self.user,
#             content = "This is a test blog"
#         )
#         self.comment = Comment.objects.create(
#             blog = self.blog,
#             content = "test comment",
#             user = self.user
#         )
        
#     def test_commenting_on_blog(self):
#         self.assertEqual(str(self.comment), 
#                          f'Comment by {self.user} on {self.blog.title[:100]}')

# class LikeModelTest(TestCase):
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(username='testuser', password='testpass')
#         self.blog = Blog.objects.create(title="Test Blog", author=self.user, content="Test Content")
#         self.like = Like.objects.create(blog=self.blog, user=self.user)
    
#     def test_like_on_blog(self):
#         self.assertEqual(str(self.like), f"{self.user} likes {self.blog.title[:100]}")
        
        




class AppBlogModelsTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@mail.com", password="testpass"
        )
        cls.blog = Blog.objects.create(
            title = "Test Blog",
            author = cls.user,
            content = "This is a test blog"
        )
        cls.comment = Comment.objects.create(
            blog = cls.blog,
            content = "test comment",
            user = cls.user
        )
        cls.like = Like.objects.create(blog=cls.blog, user=cls.user)
    
    # tests for models
    def test_blog_creation(self):
        self.assertEqual(str(self.blog), "Test Blog..............")
        self.assertEqual(self.blog.total_likes(), 1)
        self.assertEqual(self.blog.total_comments(), 1)
    
    def test_blog_get_absolute_url(self):
        self.assertEqual(self.blog.get_absolute_url(), reverse("blog_detail", args=[str(self.blog.id)]))

    def test_commenting_creation(self):
        self.assertEqual(str(self.comment), 
                         f'Comment by {self.user} on {self.blog.title[:100]}')
    
    def test_like_creation(self):
        self.assertEqual(str(self.like), f"{self.user} likes {self.blog.title[:100]}")
        

class AppBlogViewsTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@mail.com",
            password="testpass"
        )
        cls.blog = Blog.objects.create(
            title = "Test Blog",
            author = cls.user,
            content = "This is a test blog"
        ) 
    
    def test_blog_list_view(self):
        response = self.client.get(reverse("blog_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Blog")
        self.assertTemplateUsed(response, "blogs/blog_list.html")
        
    def test_blog_detail_view(self):
        response = self.client.get(reverse("blog_detail", args=[str(self.blog.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Blog")
        self.assertTemplateUsed(response, "blogs/blog_detail.html")
        
    def test_blog_create_view(self):
        self.client.login(email=self.user.email, password = "testpass")
        response = self.client.post(reverse("blog_create"), {
            "title": "New Blog",
            "content": "New Blog Content"
        })    
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Blog.objects.count(), 2)
        # self.assertTemplateUsed(response, "blog/blog_create.html")
        #  when redirect, no template is rendered
        
    def test_blog_edit_view(self):
        self.client.login(email=self.user.email, password="testpass")
        response = self.client.post(reverse("blog_edit", args=[str(self.blog.id)]), {
            "title": "Updated Blog Title",
            "content": "Updated Blog Content"
        })
        self.assertEqual(response.status_code, 302)
        self.blog.refresh_from_db()
        self.assertEqual(self.blog.title, "Updated Blog Title")
        
    def test_blog_delete_view(self):
        self.client.login(email=self.user.email, password="testpass")
        response = self.client.post(reverse("blog_delete", args=[str(self.blog.id)]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Blog.objects.count(), 0)
 
 
    # i thought there are 2 blogs in the database as one is self.blog, another is created with test_blog_create_view function
    # There will be only one blog in database . The Reason is -
        
    #         Test Isolation
    # Test Isolation: Django’s test framework runs each test in a separate transaction. When one test modifies the database (like creating or deleting objects), those changes don’t persist to other tests unless they’re using the same database transaction.

    # Database Reset: After each test method completes, the database is rolled back to its previous state. So, when test_blog_delete_view runs, it starts with a clean slate unless setUpTestData has created the objects.
    
    def test_like_blog(self):
        self.client.login(email=self.user.email, password="testpass")
        response = self.client.post(reverse('blog_detail', args=[str(self.blog.id)]), {'like': 'like'})
        self.assertEqual(Like.objects.count(), 1)
        
    def test_comment_blog(self):
        self.client.login(email=self.user.email, password="testpass")
        response = self.client.post(reverse('blog_detail', args=[str(self.blog.id)]), {
            'content': 'This is a comment'
        })
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.first().content, "This is a comment")