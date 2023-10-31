conta = str(input("Introduz a conta (2 + 3): "));

conta_divida = conta.split(" ");

historico = [];

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
historico.append(str(conta) + " = " + str(resultado));

op = str(input("Introduz H se quiser ver o histórico: "));
if op == "H" or op == "h":
    print(historico);