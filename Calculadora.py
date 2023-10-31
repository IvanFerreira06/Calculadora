conta = str(input("Introduz a conta (2 + 3): "));

conta_divida = conta.split(" ");

match conta_divida[1]:
    case "+":
        resultado = float(conta_divida[0]) + float(conta_divida[2]);
    case "-":
        resultado = float(conta_divida[0]) - float(conta_divida[2]);
    case "*":
        resultado = float(conta_divida[0]) * float(conta_divida[2]);
    case "/":
        resultado = float(conta_divida[0]) / float(conta_divida[2]);

print(f"{conta} = {resultado}");