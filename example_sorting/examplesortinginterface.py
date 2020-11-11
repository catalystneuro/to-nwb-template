"""Authors: Cody Baker and Ben Dichter."""
import spikeextractors as se

from nwb_conversion_tools.basesortingextractorinterface import BaseSortingExtractorInterface


class ExampleSortingInterface(BaseSortingExtractorInterface):
    """An example RecordingInterface class."""

    SX = se.NumpySortingExtractor

    def __init__(self, **input_args):
        self.sorting_extractor = se.example_datasets.toy_example()[1]  # self.SX(**input_args)

    def get_metadata(self):
        """Return as much auto-populated metadata as possible."""
        se_metadata = dict(
        )
        return se_metadata
