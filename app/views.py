from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.views import ModelView
from flask_appbuilder.widgets import ListBlock, ShowBlockWidget
from wtforms.validators import NumberRange
from datetime import datetime
from . import appbuilder, db
from .models import Person


class ProductPubView(ModelView):
    datamodel = SQLAInterface(Person)
    validators_columns = {
        'birthday': [NumberRange(min=1900, max=datetime.now().year, message='Year is not in range')]
    }
    # base_permissions = ["can_list", "can_show"]
    list_widget = ListBlock
    show_widget = ShowBlockWidget

    # label_columns = {"photo_img": "Photo"}
    #
    list_columns = ["id", "name", "birthday"]
    search_columns = ["id", "name", "birthday"]

    # show_fieldsets = [
    #     ("Summary", {"fields": ["name", "price_label", "photo_img", "product_type"]}),
    #     ("Description", {"fields": ["description"], "expanded": True}),
    # ]


class ProductView(ModelView):
    datamodel = SQLAInterface(Person)
    validators_columns = {
        'birthday': [NumberRange(min=1900, max=datetime.now().year, message='Year is not in range')]
    }


# class ProductTypeView(ModelView):
#     datamodel = SQLAInterface(ProductType)
#     related_views = [ProductView]
#

db.create_all()
appbuilder.add_view(ProductPubView, "Our people", icon="fa-folder-open-o")
appbuilder.add_view(
    ProductView, "List of people", icon="fa-folder-open-o", category="Management"
)
appbuilder.add_separator("Management")
# appbuilder.add_view(
#     ProductTypeView, "List Product Types", icon="fa-envelope", category="Management"
# )
