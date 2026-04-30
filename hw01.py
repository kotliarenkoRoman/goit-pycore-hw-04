EMPTY_DATA = ("--", "--")

def total_salary(filepath: str) -> tuple:
    total_salary_amount = 0
    total_users = 0
    
    try:
        with open(filepath, 'r') as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                _, salary = line.strip().split(',')
                total_salary_amount += int(salary.strip())
                total_users +=  1
        
        # check is empty file and no users rows found
        if total_users == 0: 
            return EMPTY_DATA

        return (total_salary_amount, int(total_salary_amount /total_users))
    
    except FileNotFoundError as e:
        print(str(e))
        return EMPTY_DATA
    except ValueError as e:
        print(f"Invalid data format: {e}")
        return EMPTY_DATA

# function usage
filepath = './data/salary_list.txt'
total, average = total_salary(filepath)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")