from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps


@receiver(post_migrate)
def init_category_instance(sender, *args, **kwargs):
    if sender.name == "aluraflix":
        CategoryModel = apps.get_model("aluraflix", "Category")
        
        if not CategoryModel.objects.exists():
            CategoryModel.objects.create(
                title="LIVRE",
                color="WHITE"
            )