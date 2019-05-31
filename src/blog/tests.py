from django.test import TestCase
from blog.models import Article

# Create your tests here.


class ArticleTest(TestCase):
    def create_article(self,
                       title='This is the title of an article',
                       content='This is the content of an article'):
        return Article.objects.create(title=title, content=content)

    def setUp(self):
        self.blog = self.create_article()

    def test_blog_creation(self):
        self.assertTrue(isinstance(self.blog, Article))

    def test_blog_is_active_by_default(self):
        self.assertTrue(self.blog.active)

    def test_blog_str(self):
        blog = self.create_article()
        self.assertEqual(self.blog.__str__(), blog.title)

    def test_blog_get_absolute_url(self):
        self.assertEqual('/blog/{}/'.format(self.blog.id), self.blog.get_absolute_url())

