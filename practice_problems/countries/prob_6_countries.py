""" There is at least one country name that contains another country name. Find all of these cases. """

found = []


with open('countries.txt', 'r') as f:
    countries = f.read().splitlines()
    for i in range(len(countries)):
        for j in range(i + 1, len(countries)):
            if countries[i] in countries[j]:
                found.append((countries[i], countries[j]))

print(found)
print(len(found))

            
        
        




        

            

        
    