import re

def parse_encoded_string(encoded_string):
    # Define a regular expression pattern to match the encoded string
    pattern = r'([^0]+)0*([^0]+)0*([^0]+)'

    # Use re.match to search for the pattern at the beginning of the string
    match = re.match(pattern, encoded_string)

    if match:
        # Extract the matched groups and create a dictionary
        first_name, last_name, id = match.groups()
        parsed_data = {
            "first_name": first_name,
            "last_name": last_name,
            "id": id
        }
        return parsed_data
    else:
        # Handle cases where the input does not match the expected format
        return None

# Example
encoded_string = "John000Doe000123"
parsed_data = parse_encoded_string(encoded_string)

if parsed_data:
    print(parsed_data)
else:
    print("Invalid input format.")
