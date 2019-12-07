def map_keys_and_values_from_object(obj):
    columns = []
    values = []

    for key in obj.keys():
        columns.append(key)
        values.append(obj[key])

    return {"columns": columns, "values": values}