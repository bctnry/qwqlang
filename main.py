
def qwq_dbi_conv(source_str):
    cmd_list = source_str.split()
    current_index_counter = 0
    current_stack = []
    for i, cmd in enumerate(cmd_list):
        if cmd == 'qwq':
            current_index_counter += 1
        elif cmd == 'qnq':
            current_stack.append(str(current_index_counter))
            current_index_counter = 0
        elif cmd == 'qxq':
            if current_index_counter != 0:
                current_stack.append(str(current_index_counter))
                current_index_counter = 0
            application_res = ''.join(['(', current_stack[-1], ' ', current_stack[-2], ')'])
            del current_stack[-2:]
            current_stack.append(application_res)
        elif cmd == 'qaq':
            if current_index_counter != 0:
                current_stack.append(str(current_index_counter))
                current_index_counter = 0
            abstraction_res = ''.join(['λ', current_stack[-1]])
            del current_stack[-1]
            current_stack.append(abstraction_res)
    return current_stack[-1]
