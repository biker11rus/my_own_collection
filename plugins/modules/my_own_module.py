#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: This is my test module

version_added: "1.0.0"

description: This is my longer description explaining my test module.

options:
    path:
        description: Full path and name.
        required: true
        type: str
    content:
        description: Content file
        required: false
        type: str
        default: ""
extends_documentation_fragment:
    - my_namespace.my_collection.my_doc_fragment_name

author:
    - Ruslan Khozyainov Netology
'''

EXAMPLES = r'''
# Create a file
- name: Creating a file with content
  my_namespace.my_collection.my_test:
    path: '/tmp/file.txt'
    content: 'some content'

'''

RETURN = r'''

'''

from os import stat
from ansible.module_utils.basic import AnsibleModule

def file_exist(path):
    try:
        stat(path)
        return False
    except FileNotFoundError:
        return True

def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=False, default="")
    )

    result = dict(
        changed=False,
        original_message='',
        message=''
    )

   
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        result['changed'] = file_exist(module.params['path'])
        module.exit_json(**result)

    if file_exist(module.params['path']):
      with open(module.params['path'], 'w') as new_file:
          new_file.write(module.params["content"])
      result['changed'] = True
      result['original_message'] = 'File {path} succesfully created'.format(path = module.params['path'])
      result['message'] = 'file created'
    else:
      result['original_message'] = 'File {path} already exist'.format(path = module.params['path'])
      result['message'] = 'File already exist' 
     
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()

