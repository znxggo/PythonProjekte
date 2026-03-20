def format_record(record_type, **fields):
    print("=== " + record_type.upper() + " ===")
    print("  key          : value")
    print("====")




format_record("user",    name="Alice", age=30, role="admin")
format_record("product", name="Widget", price=9.99, in_stock=True)
format_record("order",   id=1042, total=29.97, status="shipped", items=3)