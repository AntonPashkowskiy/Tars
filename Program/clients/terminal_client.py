#!/usr/bin/env python3
import argparse


def _parse_args():
    parser = argparse.ArgumentParser(prog='TARS')
    subparsers = parser.add_subparsers(help='For detail command information use: command --help')

    #create setting command
    create_setting_parser = subparsers.add_parser('create_setting', help='command for settings creating')
    create_setting_parser.add_argument('-k', '--key', type=str, required=True, help='setting key')
    create_setting_parser.add_argument('-v', '--value', type=str, required=True, help='setting value')

    #read settings parser 
    read_setting_parser = subparsers.add_parser('read_setting', help='command for settings reading')
    read_setting_parser.add_argument('-k', '--key', type=str, help='setting key')
    read_setting_parser.add_argument('-ks', '--keys', type=str, nargs='+', help='setting keys')

    #update settings parser
    update_setting_parser = subparsers.add_parser('update_setting', help='command for settings updating')

    #delete settings parser
    delete_setting_parser = subparsers.add_parser('delete_setting', help='command for settings deleting')

    #import settings parser
    import_settings_parser = subparsers.add_parser('import_settings', help='command for settings importing')

    #export settings parser
    export_settings_parser = subparsers.add_parser('export_settings', help='command for settings exporting')

    #read log parser
    read_log_parser = subparsers.add_parser('read_log', help='command for event log reading')

    #restore state by log parser
    restore_bylog_parser = subparsers.add_parser('restore', help='command for file system restoring by event log records')

    #create rule command
    create_rule_parser = subparsers.add_parser('create_rule', help='command for rule creating')
    create_rule_parser.add_argument('-t', '--target-dir', type=str, required=True, help='path to target directory')
    create_rule_parser.add_argument('--is-dir', action='store_true', default=False, help='rule for directories only')
    create_rule_parser.add_argument('--event-types', type=str, choices=['FILE_CREATED'\
        , 'FILE_NAME_CHANGED', 'FILE_CONTENT_CHANGED', 'FILE_INCLUDED', 'FILE_EXCLUDED'\
        , 'FILE_DELETED', 'DIRECTORY_REPLACED', 'DIRECTORY_DELETED', 'FILE_METADATA_CHANGED'],\
         nargs='+', required=True, help='types of watched file system events')
    create_rule_parser.add_argument('--content-types', type=str, choices=['ARCHIVE'\
        , 'NOTE', 'DOCUMENT', 'BOOK', 'AUDIO', 'VIDEO', 'BINARY', 'SYSTEM', 'IMAGE']\
        , nargs='+', required=True, help='types of watched content types')
    create_rule_parser.add_argument('--name-template', type=str, help='file name template regex/string')
    create_rule_parser.add_argument('--extention-template', type=str, help='file extention template regex/string')
    create_rule_parser.add_argument('--max-size', type=int, help='file max size constraint') 
    create_rule_parser.add_argument('--min-size', type=int, help='file min size constraint')
    create_rule_parser.add_argument('--action-type', type=str, choices=['DELETE_FILE' \
        , 'RENAME_FILE', 'REPLACE_FILE', 'GROUP_BY_MUSIC_BAND', 'GROUP_BY_MUSIC_GENRE' \
        , 'GROUP_BY_MUSIC_ALBUM', 'GROUP_BY_SUBJECT', 'GROUP_BY_LANGUAGE', 'GROUP_BY_GENRE'\
        , 'GROUP_BY_AUTHOR', 'IGNORE'], required=True, help='determine action type')
    create_rule_parser.add_argument('--is-permanent', action='store_true', default=False, help='is permanently delete file')
    create_rule_parser.add_argument('--target-path', type=str, required=True, help='destination replacing path')

    #read rule parser 
    read_rule_parser = subparsers.add_parser('read_rule', help='command for rule reading')

    #update rule parser
    update_rule_parser = subparsers.add_parser('update_rule', help='command for rule updating')

    #delete rule parser
    delete_rule_parser = subparsers.add_parser('delete_rule', help='command for rule deleting')

    #import rule parser
    import_rules_parser = subparsers.add_parser('import_rules', help='command for rule importing')

    #export rule parser
    export_rules_parser = subparsers.add_parser('export_rules', help='command for rule exporting')

    #execute action parser
    execute_actions_parser = subparsers.add_parser('execute_action', help='command for immeditely action executing')

    #start monitor parser
    start_monitor_parser = subparsers.add_parser('start_monitor', help='command for monitor starting')

    #stop monitor parser
    stop_monitor_parser = subparsers.add_parser('stop_monitor', help='command for monitor stoping')     

    parser.add_argument('--version', action='version', version='%(prog)s 0.5')

    return parser.parse_args()


def _get_command_json_string(arguments):
    pass


def main():
    args = _parse_args()
    pass


if __name__ == "__main__":
    main()