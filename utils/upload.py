import os
import shutil

def therapy_document_path(instance, filename):
    therapydocument = instance.therapydocument
    therapydocument_id = instance.therapydocument.id
    doctor_id = therapydocument.doctor.id
    return f'doctors/{doctor_id}/therapydocument/{filename}'

def doc_delete_path(document):
    path = os.path.abspath(os.path.join(document.path, '..'))
    print(path)
    shutil.rmtree(path)

def therapy_delete_path(document):
    path = os.path.abspath(os.path.join(document.path, '../..'))
    print(path)
    shutil.rmtree(path)