import os

def calcular_iva_por_fora(valor_base, aliquota_cbs, aliquota_ibs):
    """Calcula o imposto baseado no novo modelo de IVA (CBS + IBS) 'por fora'."""
    aliquota_total = (aliquota_cbs + aliquota_ibs) / 100
    valor_imposto = valor_base * aliquota_total
    valor_final = valor_base + valor_imposto
    return valor_imposto, valor_final

def calcular_icms_por_dentro(valor_base, aliquota_icms):
    """Calcula o imposto baseado no modelo antigo de ICMS 'por dentro'."""
    aliquota_decimal = aliquota_icms / 100
    # Fórmula do cálculo por dentro: Valor / (1 - Alíquota)
    valor_final = valor_base / (1 - aliquota_decimal)
    valor_imposto = valor_final - valor_base
    return valor_imposto, valor_final

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        limpar_tela()
        print("=" * 45)
        print("  CALCULADORA DE IMPOSTOS INDIRETOS (PYTHON) ")
        print("=" * 45)
        print("[1] Calcular Novo IVA (CBS + IBS - Por Fora)")
        print("[2] Calcular ICMS Tradicional (Por Dentro)")
        print("[0] Sair")
        print("-" * 45)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "0":
            print("\nEncerrando a calculadora. Até logo!")
            break
            
        if opcao not in ["1", "2"]:
            input("\nOpção inválida! Pressione Enter para tentar novamente...")
            continue
            
        try:
            valor_base = float(input("\nDigite o valor base do produto/serviço (R$): "))
            if valor_base <= 0:
                raise ValueError
        except ValueError:
            input("\nValor inválido! Insira um número maior que zero. Pressione Enter...")
            continue
            
        if opcao == "1":
            try:
                cbs = float(input("Digite a alíquota da CBS (Federal) (%): "))
                ibs = float(input("Digite a alíquota do IBS (Estadual/Municipal) (%): "))
                
                imposto, total = calcular_iva_por_fora(valor_base, cbs, ibs)
                
                print("\n" + "-"*30)
                print(f"Valor Base:    R$ {valor_base:,.2f}")
                print(f"Total Impostos: R$ {imposto:,.2f} ({cbs+ibs}%)")
                print(f"VALOR FINAL:   R$ {total:,.2f}")
                print("-"*30)
            except ValueError:
                print("\nAlíquotas inválidas!")
                
        elif opcao == "2":
            try:
                icms = float(input("Digite a alíquota do ICMS (%): "))
                if icms >= 100:
                    print("\nA alíquota do cálculo por dentro não pode ser maior ou igual a 100%!")
                    input("\nPressione Enter para continuar...")
                    continue
                    
                imposto, total = calcular_icms_por_dentro(valor_base, icms)
                
                print("\n" + "-"*30)
                print(f"Valor Base:    R$ {valor_base:,.2f}")
                print(f"ICMS embutido: R$ {imposto:,.2f} ({icms}%)")
                print(f"VALOR FINAL:   R$ {total:,.2f}")
                print("-"*30)
            except ValueError:
                print("\nAlíquota inválida!")
                
        input("\nPressione Enter para voltar ao menu...")

if __name__ == "__main__":
    main()
