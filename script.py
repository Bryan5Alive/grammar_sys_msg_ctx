def custom_generate_chat_prompt(user_input, state, **kwargs):
    if 'grammar_string' in state and state['grammar_string']:
        lines = state['grammar_string'].split('\n')
        found_marker = False
        system_message = ''

        for line in lines:
            if line.strip() == '# grammar_sys_msg:':
                found_marker = True
                continue
            if found_marker:
                if not line.startswith('#'):
                    break
                else:
                    system_message += line[2:] + '\n'

        system_message = system_message.rstrip('\n')

        if system_message:
            if 'custom_system_message' in state:
                state['custom_system_message'] += '\n\n' + system_message
            else:
                state['custom_system_message'] = system_message

    return
