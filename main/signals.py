##from django.db.models.signals import post_delete, post_save
##from django.dispatch import receiver
##
##from main.models import TaskDocument, Task, Project, Block
##from utils.upload import task_delete_path, doc_delete_path
##
##
##@receiver(post_delete, sender=Task)
##def task_deleted(sender, instance, **kwargs):
##   if instance.docs.count() > 0:
##       for doc in instance.docs:
##           task_delete_path(document=doc.document)
##
##
##@receiver(post_delete, sender=TaskDocument)
##def taskdoc_deleted(sender, instance, **kwargs):
##  doc_delete_path(document=instance.document)
##
##
##@receiver(post_save, sender=Project)
##def block_create(sender, instance, **kwargs):
##  Block.objects.create(project=instance, name='Done tasks', type_of=1)
##  Block.objects.create(project=instance, name='To do tasks', type_of=2)
##  Block.objects.create(project=instance, name='Delayed tasks', type_of=3)
