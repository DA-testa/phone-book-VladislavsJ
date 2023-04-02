def hash_phone_number(phone_number):
    half_length = len(phone_number) // 2
    if len(phone_number) % 2 == 1:
        left_half = phone_number[:half_length]
        right_half = phone_number[-half_length-1::-1]
        middle_digit = phone_number[half_length]
        hashed_value = int(left_half) * (int(right_half) + int(middle_digit)) % 10
    else:
        left_half = phone_number[:half_length]
        right_half = phone_number[half_length:]
        hashed_value = int(left_half) * int(right_half) % 10
    return hashed_value

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = [[] for i in range(10)]
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            hashed_value = hash_phone_number(str(cur_query.number))
            hashed_contacts = contacts[hashed_value]
            for i in range(len(hashed_contacts)):
                if hashed_contacts[i].number == cur_query.number:
                    hashed_contacts[i].name = cur_query.name
                    break
            else: # otherwise, just add it
                hashed_contacts.append(cur_query)
        elif cur_query.type == 'del':
            hashed_value = hash_phone_number(str(cur_query.number))
            hashed_contacts = contacts[hashed_value]
            for j in range(len(hashed_contacts)):
                if hashed_contacts[j].number == cur_query.number:
                    hashed_contacts.pop(j)
                    break
        else:
            response = 'not found'
            hashed_value = hash_phone_number(str(cur_query.number))
            hashed_contacts = contacts[hashed_value]
            for contact in hashed_contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
