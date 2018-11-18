idade = int(input("Informe a sua idade: "))

if(idade <= 0):
    print("A sua idade não pode ser menor ou igual a 0")
elif(idade > 150):
    print("A sua idade não pode ser superior a 150 anos!")
elif(idade < 18):
    print("Você precisa ter mais do que 18 anos!")
else:
    print("Você foi registrado com sucesso!")
