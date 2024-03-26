import argparse

from taxi_gcp.core import collect


# TODO: USAR CLICK PARA CRIAR A INTERFACE DE LINHA DE COMANDO
def main():
    parser = argparse.ArgumentParser(
        description="Taxi GCP: pacote para integração com o GCP",
        epilog="Use com sabedoria!",
    )

    parser.add_argument(
        "subcommand",
        type=str,
        help="Subcomando a ser executado",
        choices=(
            "collect",
            "send-bucket",
            "send-bq",
            "list-bucket",
            "read-bq",
            "transform",
            "create-dash-table",
            "read-dash-table",
        ),
    )

    parser.add_argument(
        "path_data",
        type=str,
        help="Caminho dos arquivos a serem coletados ou diretório.",
    )

    args = parser.parse_args()

    # Tratamento específico para o comando 'collect'
    if args.subcommand == "collect":
        try:
            collected_files, path_data = collect(args.path_data)
            print(f"Coletados {len(collected_files)} arquivos de: {path_data}")
            for file in collected_files:
                print(file)
        except Exception as e:
            print(f"Erro ao executar {args.subcommand}: {e}")
    else:
        # # Estrutura preparada para expansão para outros comandos
        # if args.subcommand == "send-bucket":
        try:
            # Aqui podemos invocar outros comandos conforme necessário
            # Por exemplo: globals()[args.subcommand](args.path_data)
            print(f"Subcomando {args.subcommand} ainda não implementado.")
        except KeyError:
            print(f"Subcomando {args.subcommand} não implementado")
        except Exception as e:
            print(f"Erro ao executar {args.subcommand}: {e}")


if __name__ == "__main__":
    main()
