from nwb_conversion_tools import NWBConverter, dict_deep_update
from .template_ecephys_datainterface import TemplateEcephysDataInterface
from .template_ophys_datainterface import TemplateOphysDataInterface
from .template_behavior_datainterface import TemplateBehaviorDataInterface
from . import schema

import importlib.resources as pkg_resources
import json


class TemplateNWBConverter(NWBConverter):

    # Modular data interfaces
    data_interface_classes = {
        'TemplateEcephysDataInterface': TemplateEcephysDataInterface,
        'TemplateOphysDataInterface': TemplateOphysDataInterface,
        'TemplateBehaviorDataInterface': TemplateBehaviorDataInterface
    }

    @classmethod
    def get_input_schema(cls):
        """Get input schema from data interfaces and from generic source"""
        # Get specific input schemas from data interfaces
        input_schema = super(TemplateNWBConverter, cls).get_metadata()

        # Get generic input schema
        with pkg_resources.open_text(schema, 'input_schema_generic.json') as f:
            input_schema_generic = json.load(f)

        # Update specific input schema with generic schema
        input_schema['properties'] = dict_deep_update(
            input_schema['properties'],
            input_schema_generic['properties']
        )

        return input_schema

    def __init__(self, input_data):
        super().__init__(**input_data)

    def get_metadata(self):
        """Auto-fill as much of the metadata as possible. Must comply with metadata schema."""
        metadata = super().get_metadata()

        return metadata
