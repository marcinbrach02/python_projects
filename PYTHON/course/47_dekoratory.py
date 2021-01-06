# def get_message(message: str) -> str:
#     return f'Wiadomość z systemu: {message}'
#
# def get_db_message(message: str) ->str:
#     return f'Wiadomość bazy: {message}'
#
#
# def get_formated_message(message: str) -> str:
#     return '<em>{}<em>'.format(get_message(message))
#
#
# def get_db_formated_message(message: str) -> str:
#     return '<em>{}<em>'.format(get_db_formated_message(message))
#
#
# print(get_message('test'))
# print(get_formated_message('sss'))



def get_decorated_message(original_function):
    def decorated_function(message: str):
        message = original_function(message)
        return f'<em>{message}</em>'
    return decorated_function

def tag_decorator_factory(tag):
    def decorator(original_function):
        def decorated_function(message):
            message = original_function(message)
            return f'<{tag}>{message}</{tag}>'
        return decorated_function
    return decorator


# @get_decorated_message == get_decorated_message(get_decorated_message(get_message))
# @get_decorated_message
# @get_decorated_message

@tag_decorator_factory('p')
@tag_decorator_factory('em')
def get_message(message: str) -> str:
    return f'Wiadomość z systemu: {message}'

print(get_message('test'))


# print(get_message('test'))
# get_message = get_decorated_message(get_decorated_message(get_message))
# print(get_message('test'))


#@router('/user/<id>')
#def get_user(id -> int):





