name = 'Sammi Aldhi Yanto'
age = 19

print('nama saya ' + name + 'umur saya ' + str(age))
print('nama saya %s usia saya %d' % (name, age))
print('nama saya {} usia saya {}'.format(name, age))
print('nama saya {1} usia saya {0}'.format(age, name))

siswa = {
    'nim': '1',
    'name': 'sam',
    'call': 'dev',
    'age' : 19,
    'ipk': 4.0
}
print('my name is {name}, with age {age}, you can call me {call} and my ipk {ipk}'.format(**siswa))

# gud
print(f'my name is {name} age {age}')