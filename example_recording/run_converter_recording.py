"""Authors: Cody Baker."""
from examplenwbconverter import ExampleNWBConverter
from pathlib import Path

# General location information for the session
example_path = Path("D:/ExampleNWBConversion")
example_session_id = example_path.stem
nwbfile_path = example_path / f"{example_session_id}.nwb"

device_description = "Optional description of the recording device."

# There is one input argument key per data interface, each corresponding to the parts of the data we want to convert
input_args = dict(
    ExampleRecording=dict(),
    # TODO: add below
    # ExampleSorting=dict(
    #     folder_path=example_path
    # ),
    # ExampleLFP=dict(
    #     folder_path=example_path
    # ),
)

example_converter = ExampleNWBConverter(**input_args)

# Auto-populates as much metadata as possible
metadata = example_converter.get_metadata()

# Add specific info for this session
metadata['NWBFile'] = dict(
    experimenter="Experimenter Name",
    session_description="This describes the experiment used to make the dataset."
)
metadata['Ecephys']['Device'][0].update(
    description="Optional description of the recording device."
)

# All of these subject fields are optional but recommended, if known
metadata['Subject'] = dict(
    species="Rattus norvegicus domestica",  # this should always be the scientific name for the species
    genotype="Wild type",
    sex="male",
    weight="250-350g"
)

# Run the conversion; for a large dataset, consider passing the "stub_test=True"
# option to ensure the output NWBFile looks OK
example_converter.run_conversion(nwbfile_path=str(nwbfile_path.absolute()), metadata_dict=metadata)
