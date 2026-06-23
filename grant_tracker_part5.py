# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: GrantTracker
def delete_record(record_id, collection_name):
    if record_id not in records:
        print(f"Ошибка: запись с ID {record_id} в коллекции '{collection_name}' не найдена.")
        return False
    
    del records[collection_name][record_id]
    
    # Удаляем связанные документы из папки 'documents' если они привязаны к удаленной записи
    if collection_name in ['applications', 'deadlines']:
        doc_folder = f"documents/{collection_name}/{record_id}"
        import os
        if os.path.exists(doc_folder):
            try:
                for filename in os.listdir(doc_folder):
                    file_path = os.path.join(doc_folder, filename)
                    if os.path.isfile(file_path):
                        os.remove(file_path)
            except PermissionError as e:
                print(f"Ошибка при удалении файлов для записи {record_id}: {e}")
    
    # Удаляем запись из списка активных задач (если применимо)
    if collection_name == 'applications':
        active_tasks = [task for task in active_tasks if task['id'] != record_id]
        
    print(f"Запись с ID {record_id} успешно удалена из коллекции '{collection_name}'.")
    return True
