from nwb_conversion_tools.basedatainterface import BaseDataInterface
from nwb_conversion_tools.utils import get_base_schema, get_schema_from_hdmf_class
from . import schema
import pynwb
from pynwb import NWBFile
from datetime import datetime
import importlib.resources as pkg_resources
import json
import uuid


class TemplateEcephysDataInterface(BaseDataInterface):

    @classmethod
    def get_input_schema(cls):
        with pkg_resources.open_text(schema, 'input_schema_ecephys.json') as f:
            input_schema = json.load(f)
        return input_schema

    def __init__(self, **input_args):
        super().__init__(**input_args)

    def get_metadata_schema(self):
        metadata_schema = get_base_schema()
        metadata_schema['properties']['Ecephys'] = get_base_schema(tag='Ecephys')
        metadata_schema['properties']['Ecephys']['properties']['Device'] = get_schema_from_hdmf_class(pynwb.device.Device)
        metadata_schema['properties']['Ecephys']['properties']['ElectrodeGroup'] = get_schema_from_hdmf_class(pynwb.ecephys.ElectrodeGroup)
        metadata_schema['properties']['Ecephys']['properties']['ElectricalSeries_raw'] = get_schema_from_hdmf_class(pynwb.ecephys.ElectricalSeries)
        metadata_schema['properties']['Ecephys']['properties']['ElectricalSeries_processed'] = get_schema_from_hdmf_class(pynwb.ecephys.ElectricalSeries)

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
                Ecephys=dict(
                    Device=dict(name='Device_ecephys'),
                    ElectrodeGroup=dict(
                        name='ElectrodeGroup',
                        description='no description',
                        location='unknown',
                        device='Device_ecephys'
                    )
                )
            )

        return metadata

    def convert_data(self, nwbfile: NWBFile, metadata_dict: dict,
                     stub_test: bool = False):
        raise NotImplementedError('This should be implemented')
