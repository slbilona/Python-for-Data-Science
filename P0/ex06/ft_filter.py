def ft_filter(function, object: any):
    return [x for x in object if function(x)]
