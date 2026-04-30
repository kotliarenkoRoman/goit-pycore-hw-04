def get_cats_info(filepath: str) -> dict:
    try:
        cats_list = []
        with open(filepath, 'r') as fh:
            for line in fh:
                line = line.strip() # check empty string
                if not line:
                    continue
                cat_id, name, age = line.split(',')
                cats_list.append({
                        'id': cat_id.strip(),
                        'name': name.strip(),
                        'age': age.strip() 
                })
        return cats_list        
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return [{}]            

cats_info = get_cats_info("./data/cats_dfile.txt")
print(cats_info)
