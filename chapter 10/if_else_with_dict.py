# a={1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9}
odd_even={i:('even' if i%2==0 else 'odd') for i in range(1,11)}

print(odd_even)