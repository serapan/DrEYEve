def obj_to_dict(obj):
    d = obj.__dict__
    if 'date' in d:
        d['date'] = str(d['date'])
    d.pop('_sa_instance_state', None)
    return d

def list_of_obj_to_dict(list_of_obj):
    return [obj_to_dict(obj) for obj in list_of_obj]

def sql_row_to_dict(columns, row):
    d = {columns[i]: row[i] for i in range(0, len(columns))}
    if 'date' in d:
        d['date'] = str(d['date'])
    return d

def list_of_sql_rows_to_dict(columns, list_of_rows):
    return [sql_row_to_dict(columns, row) for row in list_of_rows]

def list_of_floats_to_list_of_percentages(list_of_floats):
    total_count = sum(list_of_floats)
    result = [round(list_of_floats[i]/total_count, 4) for i in range(0, len(list_of_floats) - 1)]
    result.append(round(1.0-sum(result), 4))
    return result