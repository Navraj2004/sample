def find_s(training_data):
    
    h = training_data[0][:-1]
    
    for example in training_data:
        if example[-1] == "yes":
            for i in range(len(h)):
                if(h[i]!=example[i]):
                    h[i] = "?"
                
    return h

training_data = [
    ['sunny','warm','normal','strong','yes'],
    ['sunny','warm','high','strong','yes'],
    ['rainy','cold','high','strong','no'],
    ['sunny','warm','high','strong','yes']
]
print("h")
h = find_s(training_data)
print(h)
 
