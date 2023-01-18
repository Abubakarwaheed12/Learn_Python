# w ,a , +r 
# write 
# append
# +r is sy hum read b aor write b kar sakty han 
with open('file.txt' , 'r+') as f:
    f.seek(len(f.read()))
    f.write('\nhello i am abu bakar waheed')
    # read and write method
    with open('file.txt' , 'r') as ff:
        print(ff.read())