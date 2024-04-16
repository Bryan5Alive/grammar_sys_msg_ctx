params = {
    'use_sys_message': True,
    'use_ctx': True,
}


def get_comment_block(lines, marker):
    found_marker = False
    result = ''
    for line in lines:
        if line.strip() == marker:
            found_marker = True
            continue
        if found_marker:
            if not line.startswith('#'):
                break
            else:
                result += line[2:] + '\n'

    return result.rstrip('\n')


def state_modifier(state):
    if 'grammar_string' in state and state['grammar_string']:
        lines = state['grammar_string'].split('\n')

        custom_system_message_result = get_comment_block(lines, '# grammar_sys_msg:') if params.get('use_sys_message', False) else None
        context_result = get_comment_block(lines, '# grammar_ctx:') if params.get('use_ctx', False) else None

        if custom_system_message_result:
            if ('custom_system_message' in state) and state['custom_system_message']:
                state['custom_system_message'] += '\n\n' + custom_system_message_result + '\n'
            else:
                state['custom_system_message'] = custom_system_message_result + '\n'

        if context_result:
            if ('context' in state) and state['context']:
                state['context'] += '\n\n' + context_result + '\n'
            else:
                state['context'] = context_result + '\n'

    return state
