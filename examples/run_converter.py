from to_nwb_template import TemplateNWBConverter


# Get input schema: useful to get the structure of input data (source data and
# conversion options)
input_schema = TemplateNWBConverter.get_input_schema()

# Instantiate converter: input data should be passed in compliance with the schema
input_data = {
    "source_data": {
        "path_raw": "path_to/file_raw.h5",
        "path_processed": "path_to/file_processed.h5"
    },
    "conversion_options": {
        "add_raw": True,
        "add_processed": True
    }
}
converter = TemplateNWBConverter(input_data)

# Get metadata schema: useful to get the structure of metadata
metadata_schema = converter.get_metadata_schema()

# Get metadata: metadata should be passed in compliance with the schema
metadata_dict = converter.get_metadata()

# Run conversion: can be saved to file or returned as an object
nwbfile = converter.run_conversion(metadata_dict, save_to_file=False)
