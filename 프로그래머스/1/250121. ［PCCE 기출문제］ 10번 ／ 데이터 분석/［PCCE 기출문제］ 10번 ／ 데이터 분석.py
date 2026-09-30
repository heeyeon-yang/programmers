def solution(data, ext, val_ext, sort_by):
    cols = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    
    idx_ext = cols[ext]
    idx_sort = cols[sort_by]
    
    filtered_data = [row for row in data if row[idx_ext] < val_ext]
    filtered_data.sort(key = lambda x: x[idx_sort])
    
    return filtered_data