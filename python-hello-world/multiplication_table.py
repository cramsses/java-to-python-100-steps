

def print_mult_table(table=5, start=1, end=10):
    for i in range(start, end+1):
        #print(str(table)+' X '+str(i)+' = ' +str(table*i))
        print(f"{table} X {i} = {table*i}")

#def print_mult_table(table):
#    print_mult_table(table,1,10)


print_mult_table()
print_mult_table(6)
print_mult_table(7,31,40)