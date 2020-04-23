##import os
##import shutil
##
##def task_document_path(instance, filename):
##  task = instance.task
##   task_id = instance.task.id
##   block = task.block
##  project_id = block.project.id
##  return f'projects/{project_id}/tasks/{task_id}/{filename}'
##
##def doc_delete_path(document):
##  path = os.path.abspath(os.path.join(document.path, '..'))
##  print(path)
##  shutil.rmtree(path)
##
##def task_delete_path(document):
##  path = os.path.abspath(os.path.join(document.path, '../..'))
##  print(path)
##  shutil.rmtree(path)