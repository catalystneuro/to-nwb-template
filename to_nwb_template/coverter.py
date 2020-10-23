from nwb_conversion_tools import NWBConverter
from .data_interface import TemplateDataInterface


class TemplateNWBConverter(NWBConverter):

    # Modular data interfaces
    data_interface_classes = {
        'TemplateDataInterface': TemplateDataInterface,
    }

    def __init__(self, input_data):
        super().__init__(**input_data)
