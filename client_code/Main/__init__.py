from ._anvil_designer import MainTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.tables import app_tables
from anvil import tableau

from trexjacket.api import get_dashboard

class Main(MainTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)