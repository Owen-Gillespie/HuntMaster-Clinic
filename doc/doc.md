# Documentation

## Modules.json fields

### General fields:
**url:** A string with the url for this module.  ie. /content/demo

**target:** A string with the url for the target module that this module links to

**data:** A dictionary with additional data fields depending on the type of module.  More info below

### Data fields

content
-------
**html:** A string containing the html for the page

gps
---
**x_coordinate:** the x-coordinate of the trigger location

**y_coordinate:** the y-coordinate of the trigger location

find
----
**object_name:** the name of the object being looked for in the picture

match
-----
**image_filename:** the filename of the image that the user is trying to match with their uploaded image.

qr
--
**html:** A string containing the html for the page