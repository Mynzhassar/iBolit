import os
import shutil

def therapy_document_path(instance, filename):
    doctor = instance.doctor
    doctor_id = doctor.id
    order_id = doctor.order.id
    return f'orders/{order_id}/doctors/{doctor_id}/{filename}'

def doc_delete_path(document):
    path = os.path.abspath(os.path.join(document.path, '..'))
    print(path)
    shutil.rmtree(path)


def therapy_delete_path(document):
    path = os.path.abspath(os.path.join(document.path, '../..'))
    print(path)
    shutil.rmtree(path)
