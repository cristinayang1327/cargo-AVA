cargo= ["gerente" , "analista" , "estagiario"]
cargo_funcionario = input ("qual o cargo?")
dia_semana = input ("dia?")
if cargo_funcionario =="gerente":
    print ("acesso irrestrito")

else:
    if dia_semana not in ("sabado","domingo"):
        print ("pode entrar")
    else:

        print ("acesso negado")
        