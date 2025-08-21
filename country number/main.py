country_code={'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'
}
print("code for India is", country_code['India'])
print("code for Australia is", country_code['Australia'])
print("code for Nepal is", country_code['Nepal'])
print("code for USA is", country_code.get('USA', 'Not Found'))
print("code for UK is", country_code.get('UK', 'Not Found'))
