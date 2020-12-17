def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('show_customer_all', '/Customer')
    config.add_route('show_customer_column', '/Customer/{columnName}')
    config.add_route('show_customer_filtered_rows', '/Customer/{columnName}/{rowFilter}')
