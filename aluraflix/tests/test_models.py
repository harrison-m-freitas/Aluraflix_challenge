from django.test import TestCase

from aluraflix.models import Video, Category


class VideoModelTestCase(TestCase):
    def setUp(self):
        self.video = Video(
            title="Video Testing without category",
            description="Video Testing without category",
            url="https://testing.com",
        )
        
        self.category = Category(
            title="Testing Category",
            color="Blue"
        )
        
        self.video_with_category = Video(
            title="Video Testing with category",
            description="Video Testing with category",
            url="https://testingCategory.com",
            category_id = self.category
        )
        
    
    def test_default_attributes(self):
        "Test default attributes of the model Video"
        self.assertEqual(self.video.title, "Video Testing without category")
        self.assertEqual(self.video.description, "Video Testing without category")
        self.assertEqual(self.video.url, "https://testing.com")
        self.assertEqual(self.video.category_id.id, 1)

    def test_video_add_category(self):
        "Test create video"
        self.assertEqual(self.video_with_category.title, "Video Testing with category")
        self.assertEqual(self.video_with_category.description, "Video Testing with category")
        self.assertEqual(self.video_with_category.url, "https://testingCategory.com")
        self.assertEqual(self.video_with_category.category_id.id, self.category.id)


class CategotyModelTestCase(TestCase):
    def setUp(self):
        self.category = Category(
            title="Testing Category",
            color="Blue"
        )
        self.category_default = Category.objects.get(pk=1)
        
    
    def test_default_category(self):
        "Test default category create"
        self.assertEqual(self.category_default.title, "LIVRE")
        self.assertEqual(self.category_default.color, "WHITE")
        
    def test_category_add_category(self):
        "Test create category"
        self.assertEqual(self.category.title, "Testing Category")
        self.assertEqual(self.category.color, "Blue")