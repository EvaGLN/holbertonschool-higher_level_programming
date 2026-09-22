#!/usr/bin/env python3
"""Serializing and Deserializing with XML"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """take Python dictionary and filename as parameters.
    serialize dictionary into XML and save it to filename."""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    ET.ElementTree(root).write(filename)


def deserialize_from_xml(filename):
    """take filename as parameter, read XML data from that file
    and return a deserialized Python dictionary."""
    root = ET.parse(filename).getroot()
    return {child.tag: child.text for child in root}
