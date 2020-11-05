"""Authors: Cody Baker and Ben Dichter."""
from nwb_conversion_tools import NWBConverter
from examplerecordinginterface import ExampleRecordingInterface


class ExampleNWBConverter(NWBConverter):
    """Primary conversion class for the GrosmarkAD dataset."""

    data_interface_classes = dict(
        ExampleRecording=ExampleRecordingInterface,
        # TODO: add below
        # ExampleSorting=neuroscopedatainterface.NeuroscopeSortingInterface,
        # ExampleLFP=NeuroscopeLFPInterface
    )
