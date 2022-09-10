def make_vcard_body(first_name, last_name, phone, *args, **kwargs):
    vcard_body = [
        'BEGIN:VCARD',
        'VERSION:2.1',
        f'N:{last_name};{first_name}',
        f'FN:{first_name} {last_name}',
        f'TEL;MOBILE;VOICE:{phone}',
        'REV:1',
        'END:VCARD'
    ]
    # if args:
    #     vcard_body += [
    #         f'EMAIL;PREF;INTERNET:{args[0]}',
    #     ]
    return vcard_body


def write_vcard_file(f, vcard):
    with open(f, 'w') as f:
        f.writelines([l + '\n' for l in vcard])
