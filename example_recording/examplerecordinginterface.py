"""Authors: Cody Baker and Ben Dichter."""
import spikeextractors as se
import numpy as np

from nwb_conversion_tools.baserecordingextractorinterface import BaseRecordingExtractorInterface


class ExampleRecordingInterface(BaseRecordingExtractorInterface):
    """An example RecordingInterface class."""

    RX = se.NumpyRecordingExtractor

    def __init__(self, **input_args):
        self.recording_extractor = se.example_datasets.toy_example()[0]  # self.RX(**input_args)

    def get_metadata(self):
        """Return as much auto-populated metadata as possible."""
        re_metadata = dict(
            Ecephys=dict(
                # This specifies a subset of the channels from the recording
                subset_channels=list(range(self.recording_extractor.get_num_channels())),
                Device=[
                    dict(
                        description="Description of the device."
                    )
                ],
                ElectrodeGroup=[
                    dict(
                        name=f'NameOfElectrodeGroup{n+1}',
                        description=f"Description of electrodes on ElectrodeGroup{n+1}."
                    )
                    for n, _ in enumerate(np.unique(self.recording_extractor.get_channel_groups()))
                ],
                Electrodes=[
                    dict(
                        name='CustomElectrodeColumn',
                        description="Description of optional electrode column.",
                        data=list(range(self.recording_extractor.get_num_channels()))
                    ),
                    dict(
                        name='group',
                        description="A reference to the ElectrodeGroup this electrode is a part of.",
                        data=list(self.recording_extractor.get_channel_groups())
                    ),
                    dict(
                        name='group_name',
                        description="The name of the ElectrodeGroup this electrode is a part of.",
                        data=[f"NameOfElectrodeGroup{n+1}" for n in self.recording_extractor.get_channel_groups()]
                    )
                ],
                ElectricalSeries=dict(
                    name='ElectricalSeries',
                    description="raw acquisition traces"
                )
            )
        )
        return re_metadata
