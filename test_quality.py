# Качество рекомендаций также можно оценить выборочно: посмотрев, что рекомендации книг в целом адекватны, по авторам, названиям. 
# Пример кода для этого приведён ниже.

def display_items(item_ids):

    item_columns_to_use = ["item_id", "author", "title", "genre_and_votes", "average_rating", "ratings_count"]
    
    items_selected = items.query("item_id in @item_ids")[item_columns_to_use]
    items_selected = items_selected.set_index("item_id").reindex(item_ids)
    items_selected = items_selected.reset_index()
    
    display(items_selected)
    
print("Онлайн-события")
display_items(event_item_ids)
print("Офлайн-рекомендации")
display_items(recs_offline)
print("Онлайн-рекомендации")
display_items(recs_online)
print("Рекомендации")
display_items(recs_blended)