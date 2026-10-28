#!/usr/bin/python3
"""Creating a Simple Templating Program"""
import logging


def generate_invitations(template, attendees):
    """generates personalized invitation files"""
    if (not isinstance(template, str)
            or not isinstance(attendees, list)
            or not all(isinstance(a, dict) for a in attendees)):
        logging.error('Invalid input: template must be a string '
                      'and attendees a list of dictionaries.')
        return
    if not template:
        logging.error('Template is empty, no output files generated.')
        return
    if not attendees:
        logging.error('No data provided, no output files generated.')
        return
    for number, attendee in enumerate(attendees, start=1):
        filename = f'output_{number}.txt'
        content = template
        for key in ('name', 'event_title', 'event_date', 'event_location'):
            value = attendee.get(key)
            if value is None:
                value = 'N/A'
            content = content.replace('{' + key + '}', str(value))
        try:
            with open(filename, 'w') as file:
                file.write(content)
        except OSError as error:
            logging.error(f'Error writing {filename}: {error}')
