import requests
from bs4 import BeautifulSoup

URL_TEST = 'https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub'
URL = 'https://docs.google.com/document/d/e/2PACX-1vTER-wL5E8YC9pxDx43gk8eIds59GtUUk4nJo_ZWagbnrH0NFvMXIw6VWFLpf5tWTZIT9P9oLIoFJ6A/pub'


def decode_entries(entries: list[dict]) -> str:
    ''' Takes a list of codified entries from a parsed document and reorder the characters to
        reveal a secret message.
    '''
    # first sort the incoming data entries
    entries = sorted(entries, key=lambda item: (item['x'], item['y']))
    # it looks like the letters came in standing on one end, rotate 90 degrees
    entries = sorted(rotate_left(entries), key=lambda item: (item['x'], item['y']))
    # fill in all the blank entries with space chars (' ')
    entries = fill_entries(entries)
    # send a converted message back
    return convert_message(entries)


def fill_entries(entries):
    ''' Since the empty space is not denoted in any of the entries,
        we need to find where this happens and add an entry for each.

        add a new entry with x = x, y = y, char = ' ' for each occurrence and return the new list
    '''
    row = 0
    col = 0
    max_col = max(entry['y'] for entry in entries)
    new_entries = []

    for entry in entries:
        e_row = entry['x']
        e_col = entry['y']

        while row < e_row:
            # fill out to the end of the row if it ends with whitespace.
            while col <= max_col:
                new_entry = {'x': row, 'y': col, 'char': ' '}
                new_entries.append(new_entry)
                col += 1
            row += 1
            col = 0
        while col < e_col:
            new_entry = {'x': row, 'y': col, 'char': ' '}
            new_entries.append(new_entry)
            col += 1

        # advance to the next column
        col += 1

    if new_entries:
        entries += new_entries

    return sorted(entries, key=lambda item: (item['x'], item['y']))


def rotate_left(entries):
    """
    Rotates a flat list of {'x', 'y', 'char'} entries 90 degrees counterclockwise.

    Args:
        entries (list): List of dictionaries with keys 'x', 'y', and 'char'.

    Returns:
        list: Rotated list of dictionaries with transformed 'x' and 'y'.
    """
    if not entries:
        return []

    max_y = max(entry['y'] for entry in entries)

    rotated = []
    for entry in entries:
        new_x = max_y - entry['y']
        new_y = entry['x']
        rotated.append({
            'x': new_x,
            'y': new_y,
            'char': entry['char']
        })

    return rotated


def convert_message(entries: list[dict]) -> None:
    '''
    '''
    message = ''
    row = 0
    col = 0
    # used to fill out an entry row if the original had trailing empty space
    max_col = max(entry['y'] for entry in entries)

    for entry in entries:
        e_row = entry['x']
        e_col = entry['y']

        while row < e_row:
            while col <= max_col:
                message += ' '
                col += 1
            message += '\n'
            row += 1
            col = 0
        while col < e_col:
            message += ' '
            col += 1

        message += entry['char']

    return message


def read_public_google_doc(url: str) -> str:
    """
    Fetches and returns the text content from a publicly published Google Doc.

    Args:
        url (str): The public "published to web" URL of the Google Doc.

    Returns:
        str: The extracted plain text content of the document.
    """
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch document. Status code: {response.status_code}")

    soup = BeautifulSoup(response.text, 'html.parser')
    # Google Docs published HTML puts the content in <div class="doc-content">
    content_div = soup.find('div', class_='doc-content')
    if not content_div:
        raise Exception("Could not find document content in the HTML.")

    # Extract the document
    raw_lines = [line.strip() for line in content_div.stripped_strings]
    # Skip the headers
    # headers = raw_lines[:4]
    data_lines = raw_lines[4:]

    # Confirm that the file is in the expected format x val, char, y val
    if len(data_lines) % 3 != 0:
        raise Exception("Unexpected data format. Expected 3 points of data per entry")

    entries = []
    # Parse the entries from the document to get the character mappings
    for i in range(0, len(data_lines), 3):
        try:
            x = int(data_lines[i])
            char = data_lines[i + 1]
            y = int(data_lines[i + 2])
            entries.append({'x': x, 'y': y, 'char': char})
        # catch any issues with data formatting
        except ValueError as e:
            raise Exception(f"Error parsing data at index {i}: {e}")

    return entries


def main():
    ''' Reads a google doc with a message coded in x,y coordinates, and prints the message
    '''
    entries = read_public_google_doc(URL)
    message = decode_entries(entries)
    print(message)


if __name__ == '__main__':
    main()
