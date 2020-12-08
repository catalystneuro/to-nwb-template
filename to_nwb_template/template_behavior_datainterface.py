from nwb_conversion_tools.basedatainterface import BaseDataInterface
from nwb_conversion_tools.utils import get_base_schema, get_schema_from_hdmf_class
from . import schema
import pynwb
from pynwb import NWBFile
from datetime import datetime
import importlib.resources as pkg_resources
import json
import uuid


class TemplateBehaviorDataInterface(BaseDataInterface):

    @classmethod
    def get_input_schema(cls):
        with pkg_resources.open_text(schema, 'input_schema_behavior.json') as f:
            input_schema = json.load(f)
        return input_schema

    def __init__(self, **input_args):
        super().__init__(**input_args)

    def get_metadata_schema(self):
        metadata_schema = get_base_schema()
        metadata_schema['properties']['Behavior'] = get_base_schema(tag='Behavior')
        metadata_schema['properties']['Behavior']['properties']['Device'] = get_schema_from_hdmf_class(pynwb.device.Device)

        return metadata_schema

    def get_metadata(self, metadata):
        """Auto-fill as much of the metadata as possible."""

        if not metadata:
            # initiate metadata
            metadata = dict(
                NWBFile=dict(
                    session_description='session description',
                    identifier=str(uuid.uuid4()),
                    session_start_time=datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'),
                ),
                Behavior=dict(
                    Device=dict(name='Device_behavior'),
                )
            )

        return metadata

    def convert_data(self, nwbfile: NWBFile, metadata_dict: dict,
                     stub_test: bool = False):
        raise NotImplementedError('This should be implemented')
