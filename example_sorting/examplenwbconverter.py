"""Authors: Cody Baker and Ben Dichter."""
from nwb_conversion_tools import NWBConverter
from examplesortinginterface import ExampleSortingInterface


class ExampleNWBConverter(NWBConverter):
    """Primary conversion class for the Example dataset."""

    data_interface_classes = dict(
        ExampleSorting=ExampleSortingInterface,
        # TODO: add below
        # ExampleSorting=neuroscopedatainterface.NeuroscopeSortingInterface,
        # ExampleLFP=NeuroscopeLFPInterface
    )
