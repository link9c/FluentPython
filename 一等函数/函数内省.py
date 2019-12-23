from inspect import signature


def clip(text: str, max_length: 'int>0' = 80) -> str:
    """
    :param text:
    :param max_length:
    :return:
    """
    end = None
    if len(text) > max_length:
        space_before = text.rfind(' ', 0, max_length)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_length)
            if space_after >= 0:
                end = space_after
    if end is None:
        end = len(text)
    return text[:end].rstrip()


if __name__ == '__main__':
    print(clip.__defaults__)
    print(clip.__code__)
    print(clip.__code__.co_varnames)
    print(clip.__code__.co_argcount)
    print(clip.__annotations__)
    sig = signature(clip)
    print(str(sig))
    for name, param in sig.parameters.items():
        print(param.kind, ':', name, '=', param.default)
