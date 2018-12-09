from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Item


class TestViews(TestCase):
    

    def test_get_home_page(self):
        """ is the page up and running sattus_code 404 or 200 """
        page = self.client.get("/todo") # targetting homepage

        
    def test_template_used(self):
        """ is the right template used? """
        page = self.client.get("/todo") # targetting homepage
        self.assertTemplateUsed(page, "todo_list.html")

    def test_add_item_page(self):
        """ test with both of the above assert commands"""
        page = self.client.get("/add") # targetting homepage
        self.assertEqual(page.status_code, 200)  # 200 means no errors 
        self.assertTemplateUsed(page, "item_form.html")
        
        
    def test_get_edit_item_page(self):
        item = Item(name = "Create a test")
        item.save()
        
        page = self.client.get("/edit/{}".format(item.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")
        
        
    def test_get_edit_page_for_item_that_does_not_exist(self):
        page = self.client.get("/edit/18")
        self.assertEqual(page.status_code, 404)
        
    def test_post_create_an_item(self):
        response = self.client.post("/add", {"name": "Create a test"})
        item = get_object_or_404(Item, pk=1)
        self.assertFalse(item.done, False)
        
    def test_post_edit_an_item(self):
        item = Item(name="Create a test")
        item.save()
        id = item.id
        
        response = self.client.post("/edit/{}".format(id), {"name": "A different name"})
        item = get_object_or_404(Item, pk=id)
        
        self.assertEqual("A different name", item.name)
        
        
    def test_toggle_status(self):
        item = Item(name="Create a test")
        item.save()
        id = item.id
        
        repsonse = self.client.post("/toggle/{}".format(id))
        
        item = get_object_or_404(Item, pk=id)
        self.assertEqual(item.done, True)