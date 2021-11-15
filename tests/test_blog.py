import unittest
from app.models import Blog, User
from app import db


class BlogTest(unittest.TestCase):
    def setUp(self):
        self.user_charles = User(username='annalis', password='Ann123', email='ann@gmail.com')
        self.new_blog = Blog(id=1, title='Blog test', content='This is a test blog', user_id=self.user_annalis.id)

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title, 'Test')
        self.assertEquals(self.new_blog.content, 'This is a test blog')
        self.assertEquals(self.new_blog.user_id, self.user_annalis.id)

    def test_save_blog(self):
        self.new_blog.save()
        self.assertTrue(len(Blog.query.all()) > 0)

    def test_get_blog(self):
        self.new_blog.save()
        got_blog = Blog.get_blog(1)
        self.assertTrue(get_blog is not None)