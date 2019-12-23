def tag(name, *content, cls=None, **attrs):
    """
    生成一个活多个HTML标签
    :param name:
    :param content:
    :param clas:
    :param attrs:
    :return:
    """
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


if __name__ == '__main__':
    print(tag('br'))
    print(tag('p', 'hello', id=33, cls='sidebar'))
    print(tag(name='img',cls='img'))
