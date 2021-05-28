with open('referat.txt', 'r', encoding='utf-8') as ref:
    symbols = 0
    words = 0   
    for line in ref:
        symbols += len(line)
        words += len(line.split())
print(symbols); print(words)
    
with open('referat2.txt', 'a', encoding='utf-8') as ref2:
    with open('referat2.txt', 'w', encoding='utf-8') as ref3:
        void = ''
        ref3.write(void) 
    with open('referat.txt', 'r', encoding='utf-8') as ref:
        content = ref.read().replace('.', '!')
    ref2.write(content)

