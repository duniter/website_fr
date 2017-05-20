#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import re

def replace(original_file, placeholder_start, placeholder_end,
            replace_file, target_file=None):
    """
    This function will replace in original_file what is between starting
    placeholder and ending placeholder by the
    content of replace_file. It will save it as target_file if provided, or
    in original_file otherwise.
    No backslash must be used in the placeholders except in order to escape
    Result will be put in triple backquotes.
    :param original_file Source that must be modified:
    :param placeholder_start String starting the position to replace:
    :param placeholder_start String ending the position to replace:
    :param replace_file File to include at placeholder position:
    :param target_file Destination where the complete file must be stored.
    Facultative, will be replaced by original_file if not provided:
    :return:
    """
    if target_file is None:
        target_file = original_file

    with open(original_file, 'r') as my_original_file:
        original_content = my_original_file.read()

    with open(replace_file, 'r') as my_replace_file:
        #we keep placeholders to be able to replay the process several times
        replace_content = placeholder_start.replace('\\','') + "\n\n```\n" + my_replace_file.read() + "\n```\n\n" + placeholder_end.replace('\\','')

    regex = placeholder_start + r'(.*)' + placeholder_end
    new_content = re.sub(regex, replace_content, original_content, flags=re.DOTALL)

    with open(target_file, 'w') as my_target_file:
        my_target_file.write(new_content)

print("Will start replace")
replace('content/pages/wiki/devenir-membre.md', '\[//\]: # \(BeginLicense\)', '\[//\]: # \(EndLicense\)', 'content/files/licence_g1.txt')
print("Replace completed")
